# from flask_restful import Resource
from flask_restplus import Resource
from flask import request
from flask_jwt_extended import jwt_required
from api.handlers.player import PlayerHandler
from api.handlers.team import TeamHandler
from api.handlers.utils import Utils


class Player(Resource):


    def get(self,id):
        return Utils.serialize_player(PlayerHandler.read_by_id(id))

    @jwt_required
    def delete(self,id):
        PlayerHandler.delete(id)

    @jwt_required
    def put(self,id):
        if request.is_json:
            data = request.get_json()

            first_name = data.get("First Name", None)
            last_name = data.get("Last Name", None)
            image_uri = data.get("Image URI", None)
            team = None
            if "Team" in data:
                team = TeamHandler.read_by_name(data["Team"])
                if team is None:
                    return {"message": "Invalid Team Name", "type": "error"}, 400
            player = PlayerHandler.update(
                id,
                first_name=first_name,
                last_name=last_name,
                image_uri=image_uri,
                team=team
            )
            return Utils.serialize_player(player)

        else:
            return {"message": "Request requires JSON format", "type": "error"}, 400


class PlayersListByTeam(Resource):
    def get(self,id):
        return Utils.serialize_player_list(PlayerHandler.read_by_team(TeamHandler.read_by_id(id)))

class PlayersList(Resource):

    def get(self):
        return Utils.serialize_player_list(PlayerHandler.read())

    @jwt_required
    def post(self):
        if request.is_json:
            data = request.get_json()
            if "First Name" in data and "Last Name" in data and "Image URI" in data and "Team" in data:
                team = TeamHandler.read_by_name(data["Team"])
                if team:
                    player = PlayerHandler.insert(
                        data["First Name"],
                        data["Last Name"],
                        data["Image URI"],
                        team,
                    )
                    return {"message": "New Player Created", "type": "info","Player ID": player.id}, 201
                else:
                    return {"message": "Invalid Team Name", "type": "error"}, 400
            else:
                return {"message": "Invalid JSON", "type": "error"}, 400
        else:
            return {"message": "Request requires JSON format", "type": "error"}, 400


