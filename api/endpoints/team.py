# from flask_restful import Resource
from flask_restplus import Resource
from flask import request
from flask_jwt_extended import jwt_required

from api.handlers.team import TeamHandler
from api.handlers.utils import Utils


class Team(Resource):

    def get(self, id):
        return Utils.serialize_team(TeamHandler.read_by_id(id)), 200

    @jwt_required
    def delete(self, id):
        TeamHandler.delete(id), 200

    @jwt_required
    def put(self, id):
        if request.is_json:
            data = request.get_json()
            team_name = data.get("Team Name", None)
            logo_uri = data.get("Logo URI", None)
            team = TeamHandler.update(
                id,
                teamname=team_name,
                logoUri=logo_uri
            )
            return Utils.serialize_team(team), 200

        else:
            return {"message": "Request requires JSON format", "type": "error"}, 400


class TeamsList(Resource):

    def get(self):
        if request.is_json:
            print(request.get_json())
        return Utils.serialize_team_list(TeamHandler.read()), 200

    @jwt_required
    def post(self):
        if request.is_json:
            data = request.get_json()
            if "Team Name" in data and "Logo URI" in data:
                team = TeamHandler.insert(
                    data["Team Name"],
                    data[ "Logo URI"]
                )
                return {"message": "New Team Created", "type": "info", "Team ID": team.id}, 201
            else:
                return {"message": "Invalid JSON", "type": "error"}, 400
        else:
            return {"message": "Request requires JSON format", "type": "error"}, 400

