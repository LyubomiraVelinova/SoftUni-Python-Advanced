from typing import Dict

class Player:
    name: str
    hp: int
    mp: int
    skills: Dict[str, int]
    guild: str

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        collection = [key for key, value in self.skills.items()]
        if skill_name in collection:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills_for_print = [f"==={key} – {value}" for key, value in self.skills.items()]

        # return "\n".join([f"Name: {self.name}"]+[f"Guild: {self.guild}"]+[f"HP: {self.hp}"]+[f"MP: {self.mp}"]+[a for a in skills_for_print])
        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n" + "\n".join(
            [a for a in skills_for_print]) + "\n"
