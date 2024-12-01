
def day_one(list_one, list_two):
    list_one.sort()
    list_two.sort()
    result = []

    for i in range(len(list_one)):
        if list_one[i] >= list_two[i]:
            result.append(list_one[i] - list_two[i])
        elif list_one[i] < list_two[i]:
            result.append(list_two[i] - list_one[i])

    return sum(result)

def day_one_part_two(list_one, list_two):

    result = []
    for item in list_one:
        if  list_two.count(item) > 0:
            result.append(item * list_two.count(item))

    return sum(result)
