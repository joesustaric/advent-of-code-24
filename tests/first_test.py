import advent.first

def test_first_problem():
    list_one=[3,4,2,1,3,3]
    list_two=[4,3,5,3,9,3]
    expected = 11
    result = advent.first.day_one(list_one, list_two)
    assert  expected == result

def test_first_answer():
    list_one=[]
    list_two=[]

    with open('./advent/first_input.txt', 'r') as file:
        for line in file:
            split_line = line.split()
            list_one.append(int(split_line[0]))
            list_two.append(int(split_line[1]))
    expected = 1580061
    result = advent.first.day_one(list_one, list_two)
    assert  expected == result

def test_first_answer_part_two_example():
    list_one=[3,4,2,1,3,3]
    list_two=[4,3,5,3,9,3]

    expected = 31
    result = advent.first.day_one_part_two(list_one, list_two)
    assert  expected == result

def test_first_answer_part_two():
    list_one=[]
    list_two=[]

    with open('./advent/first_input.txt', 'r') as file:
        for line in file:
            split_line = line.split()
            list_one.append(int(split_line[0]))
            list_two.append(int(split_line[1]))
    expected = 23046913
    result = advent.first.day_one_part_two(list_one, list_two)
    assert  expected == result
