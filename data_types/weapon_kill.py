from dataclasses import dataclass

@dataclass
class WeaponKill:
	player_id: int
	steam_id_64: str
	weapon: str
	kill: int
