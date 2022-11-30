from itertools import permutations

def possible_permutations(sequence):
    for perm in permutations(sequence):
        yield list(perm)

# def possible_permutations(list):
#     if len(list) <= 1:
#         yield list
#     else:
#         for perm in possible_permutations(list[1:]):
#             for i in range(len(list)):
#                 # nb elements[0:1] works in both string and list contexts
#                 yield perm[:i] + list[0:1] + perm[i:]

    # NOT WORKING
    # total = []
    # curent_list = list
    # n = len(curent_list)
    # while n > 0:
    #     for i in range(len(curent_list)):
    #         for j in range(len(curent_list)):
    #             num_rotation = curent_list[i]
    #             curent_list[i] = list[j]
    #             curent_list[j] = num_rotation
    #             total.append(curent_list)
    #             # yield list
    #         n -= 1
    # all_permutations = []
    # for permution in total:
    #     if permution not in all_permutations:
    #         all_permutations.append(permution)
    #
    # for p in all_permutations:
    #     yield p


[print(n) for n in possible_permutations([1, 2, 3])]
