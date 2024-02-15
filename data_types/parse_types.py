from data_types.match import Match
from data_types.player import Player
from data_types.player_kill import PlayerKill
from data_types.weapon_kill import WeaponKill


async def parse_maps(data):
    if data:
        parsed_matches = []
        for match in data:
            match_id = match.get('id')
            if not match_id:
                continue
            parsed_matches.append(Match(
                    id=match_id,
                    long_name=match.get('long_name'),
                    creation_time=match.get('creation_time'),
                    start=match.get('start'),
                    end=match.get('end'),
                    server_number=match.get('server_number'),
                    map_name=match.get('map_name'),
                )
            )
        
        return parsed_matches

async def parse_players(data):
    if data:
        parsed_players = []
        for player in data:
            player_id = player.get('player_id')
            steam_64 = player.get('steam_id_64')
            player_name = player.get('player')
            if not (player_id or steam_64 or player):
                continue

            most_killed_list = []
            if most_killed := player.get('most_killed'):
                for k, v in most_killed.items():
                    most_killed_list.append(PlayerKill(
                            player=player_name,
                            player_id=player_id,
                            steam_id_64=steam_64,
                            victim=k,
                            kill=v,
                        )
                    )

            death_by_list = []
            if death_by := player.get('death_by'):
                for k, v in death_by.items():
                    death_by_list.append(PlayerKill(
                            player=player_name,
                            player_id=player_id,
                            steam_id_64=steam_64,
                            victim=k,
                            kill=v,
                        )
                    )
            
            weapons_list = []
            if weapons := player.get('weapons'):
                for k, v in weapons.items():
                    weapons_list.append(WeaponKill(
                            player=player_name,
                            player_id=player_id,
                            steam_id_64=steam_64,
                            weapon=k,
                            kill=v,
                        )
                    )

            death_by_weapons_list = []
            if death_by_weapons := player.get('death_by_weapons'):
                for k, v in death_by_weapons.items():
                    death_by_weapons_list.append(WeaponKill(
                            player=player_name,
                            player_id=player_id,
                            steam_id_64=steam_64,
                            weapon=k,
                            kill=v,
                        )
                    )

            parsed_players.append(Player(
                    id=player.get('id'),
                    player_id=player_id,
                    steam_id_64=steam_64,
                    player=player_name,
                    map_id=player.get('map_id'),
                    kills=player.get('kills'),
                    kills_streak=player.get('kills_streak'),
                    deaths=player.get('deaths'),
                    deaths_without_kill_streak=player.get('deaths_without_kill_streak'),
                    teamkills=player.get('teamkills'),
                    teamkills_streak=player.get('teamkills_streak'),
                    deaths_by_tk=player.get('deaths_by_tk'),
                    deaths_by_tk_streak=player.get('deaths_by_tk_streak'),
                    nb_vote_started=player.get('nb_vote_started'),
                    nb_voted_yes=player.get('nb_voted_yes'),
                    nb_voted_no=player.get('nb_voted_no'),
                    time_seconds=player.get('time_seconds'),
                    kills_per_minute=player.get('kills_per_minute'),
                    deaths_per_minute=player.get('deaths_per_minute'),
                    kill_death_ratio=player.get('kill_death_ratio'),
                    longest_life_secs=player.get('longest_life_secs'),
                    shortest_life_secs=player.get('shortest_life_secs'),
                    combat=player.get('combat'),
                    offense=player.get('offense'),
                    defense=player.get('defense'),
                    support=player.get('support'),
                    most_killed=most_killed_list,
                    death_by=death_by_list,
                    weapons=weapons_list,
                    death_by_weapons=death_by_weapons_list,
                )
            )
        
        return parsed_players