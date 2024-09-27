import datetime
from alchemy.models import Base, DBMatch, DBPlayer, PlayerKills, PlayerDeaths, WeaponKills, WeaponDeaths
from sqlalchemy import engine, create_engine, select, union_all
from sqlalchemy.orm import Session
from tenacity import retry, stop_after_attempt


engine = create_engine("sqlite:///the_line.db", echo=False)
Base.metadata.create_all(bind=engine)


@retry(stop=stop_after_attempt(5))
def add_data(data):
	with Session(engine) as session, session.begin():
		try:
			print("<<<< ADDING DATA >>>>")
			session.add_all(data)

		except:
			print("!!!! ROLLBACK !!!!")
			session.rollback()
			raise Exception


def in_db(obj, primary_key):
	with Session(engine) as session, session.begin():
		if session.query(obj).get(primary_key):
			return True


def get_weapons_by_steam64(steam_64):
	with Session(engine) as session:
		query = (
			select(WeaponKills)
			.where(WeaponKills.steam_id_64 == steam_64)
		).order_by(WeaponKills.kills.desc())

		result = session.execute(query).scalars()
		weapons = []

		for weapon in result:
			print(weapon)
			weapons.append(weapon)

		return weapons


def get_player_by_steam64(steam_64):
	with Session(engine) as session:
		query = (
			select(DBPlayer)
			.where(DBPlayer.steam_id_64 == steam_64)
		).order_by(DBPlayer.kills.desc())

		result = session.execute(query).scalars()
		players = []

		for player in result:
			players.append(player)

		return players


def get_db_weapon_stats_by_steam64(steam_64):
	with Session(engine) as session:
		query = (
			select(WeaponKills)
			.where(WeaponKills.steam_id_64 == steam_64)
		)

		result = session.execute(query).scalars()
		weapons = []

		for weapon in result:
			weapons.append(weapon)

		return weapons


def get_player_stats_by_steam64(steam_64):
	with Session(engine) as session:
		query = (
			select(DBPlayer)
			.where(DBPlayer.steam_id_64 == steam_64)
		).order_by(DBPlayer.creation_time.desc())

		result = session.execute(query).scalars()
		players = []

		for player in result:
			players.append(player)

		return players


def get_player_kills_by_steam64(steam_64):
	with Session(engine) as session:
		query = (
			select(PlayerKills)
			.where(PlayerKills.steam_id_64 == steam_64)
		)

		result = session.execute(query).scalars()
		kills = []

		for kill in result:
			kills.append(kill)

		return kills


def get_player_name_by_steam64(steam_64):
	with Session(engine) as session:
		query = (
			select(DBPlayer)
			.where(DBPlayer.steam_id_64 == steam_64)
		).order_by(DBPlayer.creation_time.desc())

		result = session.execute(query).scalars()
		name = None
		name = result.first().player

		return name


def get_coletrain():
	cole_data = get_player_by_steam64(76561198029710441)
	cole_list = []
	for d in cole_data:
		if d.player not in cole_list:
			cole_list.append(d.player)

	with Session(engine) as session:
		query = (
			select(PlayerKills)
		)

		result = session.execute(query).scalars()
		kills = []

		for kill in result:
			kills.append(kill)

		return cole_list, kills


def get_player_kills():
	with Session(engine) as session:
		query = (
			select(DBPlayer)
			.where(DBPlayer.kills > 0)
		)

		result = session.execute(query).scalars()
		players = []

		for player in result:
			players.append(player)

		return players


def get_player_kill_count(kill_count):
	with Session(engine) as session:
		query = (
			select(DBPlayer)
			.where(DBPlayer.kills >= kill_count)
		).order_by(DBPlayer.kills.desc())

		result = session.execute(query).scalars()
		players = []

		for player in result:
			players.append(player)

		return players


def get_player_kills_week():
	delta = datetime.datetime.now() - datetime.timedelta(days=7)

	with Session(engine) as session:
		query = (
			select(DBPlayer)
			.where(DBPlayer.kills > 0)
			.where(DBPlayer.creation_time > delta)
		)

		result = session.execute(query).scalars()
		players = []

		for player in result:
			players.append(player)

		return players


def get_top_killers():
	with Session(engine) as session:
		query = (
			select(DBPlayer)
		).order_by(DBPlayer.kills.desc())

		result = session.execute(query).scalars()
		top_players = []

		for player in result:
			if (len(top_players) >= 25):
				break
			else:
				top_players.append(player)

		return top_players


def get_top_week_killers():
	delta = datetime.datetime.now() - datetime.timedelta(days=7)

	with Session(engine) as session:
		query = (
			select(DBPlayer)
			.where(DBPlayer.creation_time > delta)
		).order_by(DBPlayer.kills.desc())

		result = session.execute(query).scalars()
		top_players = []

		for player in result:
			if (len(top_players) >= 10):
				break
			else:
				top_players.append(player)

		return top_players


def get_top_weapons_by_player():
	with Session(engine) as session:
		query = (
			select(WeaponKills)
		).order_by(WeaponKills.match_time.desc())

		result = session.execute(query).scalars()
		weapons = []

		for weapon in result:
			weapons.append(weapon)

		return weapons


def get_players():
	with Session(engine) as session:
		query = (
			select(DBPlayer)
		)

		result = session.execute(query).scalars()
		players = []

		for player in result:
			players.append(player)

		return players


def get_top_kill_streaks():
	with Session(engine) as session:
		query = (
			select(DBPlayer)
		).order_by(DBPlayer.kills_streak.desc())

		result = session.execute(query).scalars()
		players = []

		for player in result:
			if (len(players) >= 25):
				break
			else:
				players.append(player)

		return players
