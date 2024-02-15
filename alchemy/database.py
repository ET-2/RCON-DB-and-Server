from alchemy.models import Base, DBMatch, DBPlayer, PlayerKills, PlayerDeaths, WeaponKills, WeaponDeaths
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///the_line.db", echo=False)

print("<<<< CREATING TABLES >>>>")
Base.metadata.create_all(bind=engine)


def add_data(data):
	with Session(engine) as session, session.begin():
		try:
			session.add_all(data)
		except:
			session.rollback()


def in_db(obj, primary_key):
	with Session(engine) as session, session.begin():
		if session.query(obj).get(primary_key):
			return True
