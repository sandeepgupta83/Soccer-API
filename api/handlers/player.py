
from api.models.player import Player
from app import db


class PlayerHandler:

    @staticmethod
    def insert(fname, lname, img, team):
        player = Player(first_name=fname, last_name=lname, imageUri=img, team=team)
        db.session.add(player)
        db.session.commit()
        return player

    @staticmethod
    def read_by_id(id):
        player = Player.query.filter_by(id=id).first()
        return player


    @staticmethod
    def read_by_name(name):
        player = Player.query.filter_by(name=name).first()
        return player

    @staticmethod
    def read_by_team(team):
        players = Player.query.filter_by(team=team).all()
        return players


    @staticmethod
    def read():
        players = Player.query.all()
        return players

    @staticmethod
    def update(id, first_name=None, last_name=None, image_uri=None, team=None):

        pl = Player.query.filter_by(id=id).first()
        if first_name:
            pl.first_name = first_name

        if last_name:
            pl.last_name = last_name

        if image_uri:
            pl.imageUri = image_uri

        if team:
            pl.team = team

        db.session.commit()
        return pl

    @staticmethod
    def delete(id):
        db.session.delete(Player.query.filter_by(id=id).first())
        db.session.commit()
        return None


if __name__ == "__main__":
    # pl = PlayerHandler().read_by_team(Team.query.filter_by(id=1).first())
    # print(pl[0].team.players)
    # PlayerHandler().delete(1)
    pass
