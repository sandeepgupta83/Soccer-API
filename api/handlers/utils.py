class Utils:

    @staticmethod
    def serialize_team_list(team_obj_list):
        return list(map(Utils.serialize_team, team_obj_list))

    @staticmethod
    def serialize_team(team_obj):
        return {
            'Team ID': team_obj.id,
            'Team Name': team_obj.teamname,
            'Logo URI': team_obj.logoUri,
            'Players': Utils.serialize_player_list(team_obj.players)
        }

    @staticmethod
    def serialize_player_list(player_obj_list):
        return list(map(Utils.serialize_player,player_obj_list))

    @staticmethod
    def serialize_player(player_obj):
        return {
            'Player ID': player_obj.id,
            'First Name': player_obj.first_name,
            'Last Name': player_obj.last_name,
            'Image URI': player_obj.imageUri,
            'Team': {
                'Team ID': player_obj.team_id,
                'Team Name': player_obj.team.teamname
            }
        }
