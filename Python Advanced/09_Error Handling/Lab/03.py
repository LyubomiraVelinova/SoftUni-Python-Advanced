text = input()
try:
    times = int(input())
except:
    print("Variable times must be an integer")
else:
    print(text*times)