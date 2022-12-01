numbers = map(int, input().split(", "))
# Всеки от елементите ще бъде преобразуван на int

print(filter(index for index, number in enumerate(numbers) if number % 2 == 0)
