import os
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Api
from flask_restplus import Api

from flask_cors import CORS


from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
)

server = Flask(__name__)
CORS(server)

server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soccer.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
server.config['SECRET_KEY'] = "SOCCER_SECRET_KEY"

server.config['JWT_SECRET_KEY'] = "SOCCER_SECRET_KEY"

server.config['PROPAGATE_EXCEPTIONS'] = True


jwt = JWTManager(server)


@server.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


db = SQLAlchemy(server)


api = Api(server, prefix='/api/v1')


from api.endpoints.player import Player,PlayersList,PlayersListByTeam
from api.endpoints.team import Team,TeamsList

api.add_resource(Player,'/players/<int:id>')
api.add_resource(PlayersList, '/players')

api.add_resource(Team,'/teams/<int:id>')
api.add_resource(TeamsList, '/teams')
api.add_resource(PlayersListByTeam, '/teams/<int:id>/players')



jwt._set_error_handler_callbacks(api)





