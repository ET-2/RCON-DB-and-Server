from alchemy.database import get_player_by_steam64, get_top_killers, get_top_week_killers


class Provider:

    def __init__(self):
    	pass


    def top_killers(self):
        players = get_top_killers()
        ret_players = []

        for player in players:
            data = dict([
                ('steam_64', player.steam_id_64),
                ('name', player.player),
                ('kills', player.kills),
            ])
            ret_players.append(data)

        return ret_players


    def week_top_killers(self):
        players = get_top_week_killers()
        ret_players = []

        for player in players:
        	data = dict([
        		('steam_64', player.steam_id_64),
        		('name', player.player),
        		('kills', player.kills),
        	])
        	ret_players.append(data)

        return ret_players


    def get_player_by_steam64(self, steam_64):
        players = get_player_by_steam64(steam_64)
        ret_players = []

        for player in players:
            data = dict([
                ('steam_64', player.steam_id_64),
                ('name', player.player),
                ('kills', player.kills),
            ])
            ret_players.append(data)

        return ret_players
