count = int(input())

chemicals_set = set()
for _ in range(count):
    chemical_compounds = input().split()
    for chemical in chemical_compounds:
        chemicals_set.add(chemical)

for unique_chemical in chemicals_set:
    print(unique_chemical)
