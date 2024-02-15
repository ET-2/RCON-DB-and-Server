from dataclasses import dataclass


@dataclass
class Match:
	id: int
	long_name: str
	creation_time: str
	start: str
	end: str
	server_number: int
	map_name: str
