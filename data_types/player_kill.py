from dataclasses import dataclass

@dataclass
class PlayerKill:
	player_id: int
	steam_id_64: str
	victim: str
	kill: int
