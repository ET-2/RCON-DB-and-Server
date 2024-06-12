from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List


class Base(DeclarativeBase):
    pass


class DBMatch(Base):
    __tablename__ = 'matches'
    id:Mapped[int] = mapped_column(primary_key=True)
    long_name:Mapped[str]
    creation_time:Mapped[str]
    start:Mapped[str]
    end:Mapped[str]
    server_number:Mapped[int]
    server_name:Mapped[str]
    map_name:Mapped[str]
    match_json_url:Mapped[str]

    def __repr__(self) -> str:
        return f'<Match_ID: {self.id}>'


class DBPlayer(Base):
    __tablename__ = 'players'
    id:Mapped[int] = mapped_column(primary_key=True)
    player_id:Mapped[int]
    steam_id_64:Mapped[str]
    player:Mapped[str]
    match_id:Mapped[int]
    creation_time:Mapped[str]
    kills:Mapped[int]
    kills_streak:Mapped[int]
    deaths:Mapped[int]
    deaths_without_kill_streak:Mapped[int]
    teamkills:Mapped[int]
    teamkills_streak:Mapped[int]
    deaths_by_tk:Mapped[int]
    deaths_by_tk_streak:Mapped[int]
    nb_vote_started:Mapped[int]
    nb_voted_yes:Mapped[int]
    nb_voted_no:Mapped[int]
    time_seconds:Mapped[int]
    kills_per_minute:Mapped[float]
    deaths_per_minute:Mapped[float]
    kill_death_ratio:Mapped[float]
    longest_life_secs:Mapped[int]
    shortest_life_secs:Mapped[int]
    combat:Mapped[int] = mapped_column(default=0)
    offense:Mapped[int] = mapped_column(default=0)
    defense:Mapped[int] = mapped_column(default=0)
    support:Mapped[int] = mapped_column(default=0)

    def __repr__(self):
        return f'<Player: {self.id} {self.player}>'


class PlayerKills(Base):
    __tablename__ = 'player_kills'
    playerkill_id:Mapped[int] = mapped_column(primary_key=True)
    player_name:Mapped[str]
    player_id:Mapped[int]
    steam_id_64:Mapped[str]
    match_id:Mapped[int]
    match_time:Mapped[str]
    victim:Mapped[str]
    kills:Mapped[int]

    def __repr__(self) -> str:
        return f'<PlayerKill: {self.player_name} killed {self.victim}: {self.kills}>'


class PlayerDeaths(Base):
    __tablename__ = 'player_deaths'
    playerdeath_id:Mapped[int] = mapped_column(primary_key=True)
    player_name:Mapped[str]
    player_id:Mapped[int]
    steam_id_64:Mapped[str]
    match_id:Mapped[int]
    match_time:Mapped[str]
    killer:Mapped[str]
    kills:Mapped[int]

    def __repr__(self) -> str:
        return f'<PlayerDeath: {self.player_name} killed by {self.killer}: {self.kills}>'


class WeaponKills(Base):
    __tablename__ = 'weapon_kills'
    weaponkill_id:Mapped[int] = mapped_column(primary_key=True)
    player_name:Mapped[str]
    player_id:Mapped[int]
    steam_id_64:Mapped[str]
    match_id:Mapped[int]
    match_time:Mapped[str]
    weapon:Mapped[str]
    kills:Mapped[int]

    def __repr__(self) -> str:
        return f'<WeaponKill: {self.player_name} with {self.weapon}: {self.kills}>'


class WeaponDeaths(Base):
    __tablename__ = 'weapon_deaths'
    weapondeath_id:Mapped[int] = mapped_column(primary_key=True)
    player_name:Mapped[str]
    player_id:Mapped[int]
    steam_id_64:Mapped[str]
    match_id:Mapped[int]
    match_time:Mapped[str]
    weapon:Mapped[str]
    kills:Mapped[int]

    def __repr__(self) -> str:
        return f'<WeaponDeath: {self.player_name} by {self.weapon}: {self.kills}>'
