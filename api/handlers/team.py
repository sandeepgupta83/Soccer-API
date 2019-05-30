from app import db
from api.models.team import Team
from api.handlers.utils import Utils
from flask import jsonify

class TeamHandler:
    @staticmethod
    def insert(teamname,logo_uri):

        team = Team(teamname=teamname, logoUri=logo_uri)
        db.session.add(team)
        db.session.commit()
        return team

    @staticmethod
    def read_by_id(id):
        team = Team.query.filter_by(id=id).first()
        return team

    @staticmethod
    def read_by_name(name):
        team = Team.query.filter_by(teamname=name).first()
        return team

    @staticmethod
    def read():
        teams = Team.query.all()
        return teams

    @staticmethod
    def update(id, teamname=None, logoUri=None):

        team = Team.query.filter_by(id=id).first()
        if teamname:
            team.teamname = teamname

        if logoUri:
            team.logoUri = logoUri

        db.session.commit()
        return team

    @staticmethod
    def delete(id):
        db.session.delete(Team.query.filter_by(id=id).first())
        db.session.commit()
        return None


if __name__ == "__main__":
    print(TeamHandler().read_by_id(3))
