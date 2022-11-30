from project.hero import Hero
from project.elf import Elf
from project.wizard import Wizard
from project.knight import Knight
from project.dark_wizard import DarkWizard
from project.dark_knight import DarkKnight
from project.blade_knight import BladeKnight
from project.muse_elf import MuseElf
from project.soul_master import SoulMaster

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)

# heroes = [
#     Hero("h", 1),
#     Elf("e", 1),
#     Wizard("w", 1),
#     Knight("k", 1),
#     MuseElf("m", 1),
#     DarkWizard("dw", 1),
#     DarkKnight("dk", 1),
#     SoulMaster("sm", 1),
#     BladeKnight("bk", 1)
# ]
#
# for h in heroes:
#     print(h.__class__.__name__, h, h.__dict__)