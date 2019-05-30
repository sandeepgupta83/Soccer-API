from app import db


class Player(db.Model):

    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    imageUri = db.Column(db.String(100))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    def __repr__(self):
        player_dict = {
            'First Name': self.first_name,
            'Last Name': self.last_name,
            'Image URI': self.imageUri,
            'Team ID': self.team_id
        }
        return str(player_dict)

