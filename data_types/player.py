from dataclasses import dataclass
from data_types.player_kill import PlayerKill
from data_types.weapon_kill import WeaponKill


@dataclass
class Player:
	id: int
	player_id: int
	steam_id_64: str
	player: str
	map_id: int
	kills: int
	kills_streak: int
	deaths: int
	deaths_without_kill_streak: int
	teamkills: int
	teamkills_streak: int
	deaths_by_tk: int
	deaths_by_tk_streak: int
	nb_vote_started: int
	nb_voted_yes: int
	nb_voted_no: int
	time_seconds: int
	kills_per_minute: float
	deaths_per_minute: float
	kill_death_ratio: float
	longest_life_secs: int
	shortest_life_secs: int
	combat: int
	offense: int
	defense: int
	support: int
	most_killed: [PlayerKill] = None
	death_by: [PlayerKill] = None
	weapons: [WeaponKill] = None
	death_by_weapons: [WeaponKill] = None
