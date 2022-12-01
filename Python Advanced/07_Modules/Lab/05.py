import fibonachi


while True:
    command = input()
    if command.startswith("Create Sequence "):
        n = int(command.split()[-1])
        sequence = fibonachi.create_sequence(n)
        print(sequence)
    elif command.startswith("Locate "):
        search = int(command.split()[-1])
        try:
            pos = sequence.index(search)
            print(f"The number - {search} is at index {pos}")
        except ValueError:
            print(f"The number {search} is not in the sequence")