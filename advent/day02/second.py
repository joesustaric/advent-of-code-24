
INCREASING = 1
DECREASING = -1

ZERO_INDEX_ADJUSTMENT = 1

TOLERANCE = [1, 2, 3]

NEXT_ITEM = 1

# import pdb; pdb.set_trace()

def is_safe(data) -> bool:

    if len(data) < 2:
        return True

    last_direction = None
    report_size = len(data) - ZERO_INDEX_ADJUSTMENT

    for index in range(report_size):
        numb_1, numb_2 = data[index], data[index + NEXT_ITEM]

        if _calculate_delta(numb_1, numb_2) not in TOLERANCE:
            return False

        if _changed_direction(last_direction, numb_1, numb_2):
            return False

        last_direction = _get_direction(numb_1, numb_2)
    return True

def _changed_direction(last_direction, numb_1, numb_2) -> bool:
    direction = _get_direction(numb_1, numb_2)
    return last_direction is not None and (direction != last_direction)

def _get_direction(numb_1, numb_2) -> int:
    if (numb_2 - numb_1) > 0:
        return INCREASING
    return DECREASING

def _calculate_delta(numb_1, numb_2) -> int:
    return abs(numb_2 - numb_1)

def is_safe_pt2(data) -> bool:
    if is_safe(data):
        return True

    result = False
    for index in range(len(data)):
        copy = data.copy()
        copy.pop(index)

        if is_safe(copy):
            return True

    return result
