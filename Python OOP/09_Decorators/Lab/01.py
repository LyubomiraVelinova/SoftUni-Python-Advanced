def number_increment(numbers):

    def increase():
        return [n + 1 for n in numbers]
        # for index in range(len(numbers)):
        #     numbers[index] += 1
        # return numbers

    return increase()


print(number_increment([1, 2, 3]))