class Player:
    def __init__(self, player_dict):
        self.name = player_dict.get("name", "Unknown")
        self.age = player_dict.get("age", 0)
        self.position = player_dict.get("position", "Unknown")
        self.team = player_dict.get("team", "Unknown")

    def __repr__(self):
        return f"Player(name={self.name}, age={self.age}, position={self.position}, team={self.team})"
class Player:
    def __init__(self, player_dict):
        self.name = player_dict.get("name", "Unknown")
        self.age = player_dict.get("age", 0)
        self.position = player_dict.get("position", "Unknown")
        self.team = player_dict.get("team", "Unknown")

    def __repr__(self):
        return f"Player(name={self.name}, age={self.age}, position={self.position}, team={self.team})"

kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age": 32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

players = [
    kevin, jason, kyrie,
    {
        "name": "Damian Lillard", 
        "age": 33, 
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age": 32, 
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age": 16, 
        "position": "P", 
        "team": "en"
    }
]

new_team = []

for player_dict in players:
    new_team.append(Player(player_dict))

for player in new_team:
    print(player)
