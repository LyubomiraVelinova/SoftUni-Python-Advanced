from project import *

# from 02_project import Lizard
# from 02_project import Reptile
# from 02_project import Mammal
# from 02_project import Snake
# from 02_project import Gorilla
# from 02_project import Bear


# animals = [
#     Animal("animal"),
#     Reptile("reptile"),
#     Mammal("mammal"),
#     Lizard("lizard"),
#     Snake("snake"),
#     Gorilla("gorilla"),
#     Bear("bear")
# ]
#
# for a in animals:
#     print(a.__dict__)
#     print(a.name)

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(mammal._Animal__name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(lizard._Animal__name)
