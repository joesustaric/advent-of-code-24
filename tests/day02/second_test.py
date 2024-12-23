import advent.day02.second
import pytest

# A single element report is safe
def test_detect_safe_due_to_one_reading():
    data = [234234]
    assert True == advent.day02.second.is_safe(data)

# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
def test_detect_unsafe_due_to_change_in_direction():
    data = [1, 3, 2, 4, 5]
    assert False == advent.day02.second.is_safe(data)

# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
def test_detect_unsafe_due_to_no_in_direction():
    data = [8, 6, 4, 4, 1]
    assert False == advent.day02.second.is_safe(data)

# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
def test_detect_unsafe_due_to_decrease_too_many():
    data = [9, 7, 6, 2, 1]
    assert False == advent.day02.second.is_safe(data)

# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
def test_detect_unsafe_due_to_increase_too_many():
    data = [1, 2, 7, 8, 9]
    assert False == advent.day02.second.is_safe(data)

# 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
def test_detect_safe_due_to_all_decrease_in_range():
    data = [7, 6, 4, 2, 1]
    assert True == advent.day02.second.is_safe(data)

# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
def test_detect_safe_due_to_all_increasing_in_range():
    data = [1, 3, 6, 7, 9]
    assert True == advent.day02.second.is_safe(data)

def test_second_answer():
    result = 0

    with open('./advent/day02/second_input.txt', 'r') as file:
        for line in file:
            split_line_string = line.split()
            split_line_int = [int(i) for i in split_line_string]

            if advent.day02.second.is_safe(split_line_int):
                result += 1

    assert  463 == result
