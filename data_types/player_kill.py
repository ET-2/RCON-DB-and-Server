from dataclasses import dataclass

@dataclass
class PlayerKill:
	player: str
	player_id: int
	steam_id_64: str
	victim: str
	kill: int
