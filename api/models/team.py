from app import db
from api.models.player import Player

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teamname = db.Column(db.String(50), unique=True)
    logoUri = db.Column(db.String(100))
    players = db.relationship('Player',backref="team")

    def __repr__(self):
        team_dict = {
            'Team Name': self.teamname,
            'Logo URI': self.logoUri,
            'Players': self.players
        }
        return str(team_dict)
