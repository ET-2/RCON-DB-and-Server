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


def get_weapons(player_id):
	with Session(engine) as session:
		stmt = (
			select(WeaponKills)
			.join(WeaponKills.player)
			.where(DBPlayer.id == player_id)
		)

		result = session.execute(stmt).scalars()
		weapons = []

		for weapon in result:
			weapons.append(weapon)

		return weapons


def get_player_by_steam64(steam_64):
	with Session(engine) as session:
		query = (
			select(DBPlayer)
			.join(DBPlayer.match)
			.where(DBPlayer.steam_id_64 == steam_64)
		).order_by(DBPlayer.kills.desc())

		result = session.execute(query).scalars()
		players = []

		for player in result:
			players.append(player)

		return players


def get_top_killers():
	with Session(engine) as session:
		u = union_all(
			select(DBPlayer)
			.join(DBPlayer.match)
			.where(DBMatch.server_name == 'west'),
			select(DBPlayer)
			.join(DBPlayer.match)
			.where(DBMatch.server_name == 'east'),
			select(DBPlayer)
			.join(DBPlayer.match)
			.where(DBMatch.server_name == 'central')
		).order_by(DBPlayer.kills.desc())

		stmt = select(DBPlayer).from_statement(u)
		players = session.execute(stmt).scalars()
		top_players = []
		player_64s = []

		for player in players:
			if (len(top_players) >= 25):
				break
			elif player.steam_id_64 in player_64s:
				print(player.player, player.kills)
				continue
			else:
				print(player.player, player.kills)
				top_players.append(player)
				player_64s.append(player.steam_id_64)

		return top_players


def get_top_week_killers():
	delta = datetime.datetime.now() - datetime.timedelta(days=7)

	with Session(engine) as session:
		u = union_all(
			select(DBPlayer)
			.join(DBPlayer.match)
			.where(DBMatch.server_name == 'west')
			.where(DBMatch.creation_time > delta),
			select(DBPlayer)
			.join(DBPlayer.match)
			.where(DBMatch.server_name == 'east')
			.where(DBMatch.creation_time > delta)
		).order_by(DBPlayer.kills.desc())

		stmt = select(DBPlayer).from_statement(u)
		players = session.execute(stmt).scalars()
		top_players = []
		player_64s = []

		for player in players:
			if (len(top_players) >= 10):
				break
			elif player.steam_id_64 in player_64s:
				continue
			else:
				top_players.append(player)
				player_64s.append(player.steam_id_64)

		return top_players
