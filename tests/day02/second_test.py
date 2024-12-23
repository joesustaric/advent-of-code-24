import advent.day02.second

def test_how_many_are_safe():
    safe_1  = [7, 6, 4, 2, 1]
    unsafe_1 = [1, 2, 7, 8, 9]
    unsafe_2 = [9, 7, 6, 2, 1]
    safe_2 = [1, 3, 2, 4, 5]
    safe_3 = [8, 6, 4, 4, 1]
    safe_4 = [1, 3, 6, 7, 9]

    safe_1 = advent.day02.second.remove_first_error_from_data(safe_1)
    safe_2 = advent.day02.second.remove_first_error_from_data(safe_2)
    safe_3 = advent.day02.second.remove_first_error_from_data(safe_3)
    safe_4 = advent.day02.second.remove_first_error_from_data(safe_4)
    unsafe_1 = advent.day02.second.remove_first_error_from_data(unsafe_1)
    unsafe_2 = advent.day02.second.remove_first_error_from_data(unsafe_2)
    assert advent.day02.second.is_safe(safe_1) == True
    assert advent.day02.second.is_safe(safe_2) == True
    assert advent.day02.second.is_safe(safe_3) == True
    assert advent.day02.second.is_safe(safe_4) == True
    assert advent.day02.second.is_safe(unsafe_1) == False
    assert advent.day02.second.is_safe(unsafe_2) == False


def test_second_answer():
    result = 0

    with open('./advent/day02/second_input.txt', 'r') as file:
        for line in file:
            split_line_string = line.split()
            split_line_int = [int(i) for i in split_line_string]

            split_line_string = advent.day02.second.remove_first_error_from_data(split_line_int)
            if advent.day02.second.is_safe(split_line_string):
                result += 1

    expected = 234
    assert  expected == result
