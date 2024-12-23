
NOT_DETERMINED = 0
INCREASING = 1
DECREASING = 2
SAME = 3

MIN_TOLERANCE = 1
MAX_TOLERANCE = 3

NEXT_ITEM = 1

def is_any_safe(data):
    # while the array is not safe and not at the end
    unsafe = True
    indexes_removed = []
    



def remove_first_error_from_data(data) -> list:
    old_direction = NOT_DETERMINED
    for index in range(len(data)):
        if _last_value(index, data):
            break
        numb_1, numb_2 = _get_numbers_to_compare(index, data)
        new_direction = _get_direction(numb_1, numb_2)
        delta = _calculate_delta(numb_1, numb_2)

        if _changed_direction(old_direction, new_direction):
            data.pop(index)
            return data
        elif not _delta_within_tolerance(delta):
            data.pop(index)
            return data

        old_direction = new_direction

    return data


def is_safe(data):
    old_direction = NOT_DETERMINED
    for index in range(len(data)):
        if _last_value(index, data):
            break

        numb_1, numb_2 = _get_numbers_to_compare(index, data)
        new_direction = _get_direction(numb_1, numb_2)
        delta = _calculate_delta(numb_1, numb_2)

        if _changed_direction(old_direction, new_direction):
            return False
        elif not _delta_within_tolerance(delta):
            return False

        old_direction = new_direction

    return True

def _get_numbers_to_compare(index, data) -> tuple:
    return data[index], data[index + NEXT_ITEM]

def _delta_within_tolerance(delta):
    return delta >= MIN_TOLERANCE and delta <= MAX_TOLERANCE

def _get_direction(numb_1, numb_2):
    if numb_1 < numb_2:
        return INCREASING
    elif numb_1 > numb_2:
        return DECREASING
    elif numb_1 == numb_2:
        return SAME

def _calculate_delta(numb_1, numb_2):
    if numb_1 > numb_2:
        return numb_1 - numb_2
    elif numb_1 < numb_2:
        return numb_2 - numb_1
    elif numb_1 == numb_2:
        return 0

def _last_value(index, data):
    return index + NEXT_ITEM == len(data)

def _changed_direction(old_direction, new_direction):
    if old_direction == NOT_DETERMINED:
        return False
    return new_direction != old_direction
