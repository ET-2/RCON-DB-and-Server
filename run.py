import aiohttp
import asyncio
import json
import uuid
from alchemy.models import DBMatch, DBPlayer, PlayerKills, PlayerDeaths, WeaponKills, WeaponDeaths
from alchemy.database import add_data, in_db
from data_types.parse_types import parse_maps, parse_players
from tenacity import retry, stop_after_attempt


async def start():
    central = ''
    east = ''
    west = ''

    await run_matches(central, 'central', 1)
    await run_matches(east, 'east', 1)
    await run_matches(west, 'west', 1)


async def run_matches(url, server, page):
    cur_page = page
    ret_page = await get_maps(url, server, page)
    if ret_page > cur_page:
        await run_matches(url, server, ret_page)


@retry(stop=stop_after_attempt(5))
async def call_rcon(url, params):
    timeout = aiohttp.ClientTimeout(total=10)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url, params=params, verify_ssl=False) as resp:
                data = await resp.json()
                data_result = data.get('result')

                if resp.status == 200 and data_result:
                    print(f'[{resp.status}] {resp.url}')
                    return data_result

                elif resp.status != 200:
                    print(f'Response Status: {resp.status}')
    except:
        raise Exception


async def get_maps(server_url, server_name, page):
    url = f'{server_url}/api/get_scoreboard_maps'
    params = {'page': page}
    matches = await call_rcon(url=url, params=params)
    matches_result = matches.get('maps')
    matches_parsed = []
    total_data = []

    if not matches_result:
        print(f'<<<< {server_url} FINISHED UPDATES >>>>')
        return page

    if matches_result:
        matches_parsed = await parse_maps(matches_result)
        
        for match in matches_parsed:
            db_matches = []

            if in_db(DBMatch, match.id):
                continue
            
            match_url = f'{server_url}/api/get_map_scoreboard'
            match_param = {'map_id': match.id}
            players, db_data = await get_players(match_url, match_param)

            if db_data:
                total_data.extend(db_data)

            if players:
                db_match = db_matches.append(DBMatch(
                    id=match.id,
                    long_name=match.long_name,
                    creation_time=match.creation_time,
                    start=match.start,
                    end=match.end,
                    server_number=match.server_number,
                    server_name=server_name,
                    map_name=match.map_name,
                    match_json_url=match_url,
                    players=players
                    )
                )

            else:
                db_match = db_matches.append(DBMatch(
                    id=match.id,
                    long_name=match.long_name,
                    creation_time=match.creation_time,
                    start=match.start,
                    end=match.end,
                    server_number=match.server_number,
                    server_name=server_name,
                    map_name=match.map_name,
                    match_json_url=match_url
                    )
                )
            total_data.extend(db_matches)
        add_data(total_data)
        ret_page = page + 1
        return ret_page


async def get_players(url, params):
    players_rcon = await call_rcon(url=url, params=params)
    players = players_rcon.get('player_stats')
    parsed_players = await parse_players(players)
    db_players = []
    db_data = []

    if parsed_players:
        player_ids = []

        for player in parsed_players:
            if in_db(DBPlayer, player.id) or (player.id in player_ids):
                continue

            player_ids.append(player.id)


            most_killed = get_most_killed(player.most_killed, player.id)
            if most_killed:
                db_data.extend(most_killed)

            deaths_by = get_deaths_by(player.death_by, player.id)
            if deaths_by:
                db_data.extend(deaths_by)

            weapons = get_weapons(player.weapons, player.id)
            if weapons:
                db_data.extend(weapons)

            death_by_weapons = get_death_by_weapons(player.death_by_weapons, player.id)
            if death_by_weapons:
                db_data.extend(death_by_weapons)

            db_player = (DBPlayer(
                id=player.id,
                player_id=player.player_id,
                steam_id_64=player.steam_id_64,
                player=player.player,
                match_id=player.map_id,
                kills=player.kills,
                kills_streak=player.kills_streak,
                deaths=player.deaths,
                deaths_without_kill_streak=player.deaths_without_kill_streak,
                teamkills=player.teamkills,
                teamkills_streak=player.teamkills_streak,
                deaths_by_tk=player.deaths_by_tk,
                deaths_by_tk_streak=player.deaths_by_tk_streak,
                nb_vote_started=player.nb_vote_started,
                nb_voted_yes=player.nb_voted_yes,
                nb_voted_no=player.nb_voted_no,
                time_seconds=player.time_seconds,
                kills_per_minute=player.kills_per_minute,
                deaths_per_minute=player.deaths_per_minute,
                kill_death_ratio=player.kill_death_ratio,
                longest_life_secs=player.longest_life_secs,
                shortest_life_secs=player.shortest_life_secs,
                combat=player.combat,
                offense=player.offense,
                defense=player.defense,
                support=player.support
                )
            )
            db_data.append(db_player)
            db_players.append(db_player)


    return db_players, db_data


def get_most_killed(data, data_id):
    db_player_kills = []
    for item in data:
        db_player_kills.append(PlayerKills(
            playerkill_id=uuid.uuid4().time,
            player_name=item.player,
            player_id=item.player_id,
            steam_id_64=item.steam_id_64,
            victim=item.victim,
            kills=item.kill
            )
        )

    return db_player_kills


def get_deaths_by(data, data_id):
    db_deaths_by = []
    for item in data:
        db_deaths_by.append(PlayerDeaths(
            playerdeath_id=uuid.uuid4().time,
            player_name=item.player,
            player_id=item.player_id,
            steam_id_64=item.steam_id_64,
            killer=item.victim,
            kills=item.kill
            )
        )

    return db_deaths_by


def get_weapons(data, data_id):
    db_weapons = []
    for item in data:
        db_weapons.append(WeaponKills(
            weaponkill_id=uuid.uuid4().time,
            player_name=item.player,
            player_id=item.player_id,
            steam_id_64=item.steam_id_64,
            weapon=item.weapon,
            kills=item.kill
            )
        )

    return db_weapons


def get_death_by_weapons(data, data_id):
    db_death_by_weapons = []
    for item in data:
        db_death_by_weapons.append(WeaponDeaths(
            weapondeath_id=uuid.uuid4().time,
            player_name=item.player,
            player_id=item.player_id,
            steam_id_64=item.steam_id_64,
            weapon=item.weapon,
            kills=item.kill
            )
        )

    return db_death_by_weapons


if __name__=="__main__":
    asyncio.run(start())
