from project.player import Player


class Guild:
    name: str

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {player.guild}"

    def kick_player(self, player_name: str):
        players_names = [player.name for player in self.players]
        player_index = players_names.index(player_name)
        current_player = self.players[player_index]

        if player_name not in players_names:
            return f"Player {player_name} is not in the guild."

        self.players.pop(player_index)
        current_player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        return f"Guild: {self.name}" + "\n" + "\n".join([p.player_info() for p in self.players])
