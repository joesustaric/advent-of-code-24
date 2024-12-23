
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

        if _delta_too_much(numb_1, numb_2):
            return False

        if _changed_direction(last_direction, numb_1, numb_2):
            return False

        last_direction = _get_direction(numb_1, numb_2)
    return True

def _changed_direction(last_direction, numb_1, numb_2):
    direction = _get_direction(numb_1, numb_2)
    return last_direction is not None and (direction != last_direction)

def _get_direction(numb_1, numb_2):
    if (numb_2 - numb_1) > 0:
        return INCREASING
    return DECREASING

def _delta_too_much(numb_1, numb_2) -> bool:
    delta = _calculate_delta(numb_1, numb_2)
    return delta not in TOLERANCE

def _calculate_delta(numb_1, numb_2):
    return abs(numb_2 - numb_1)

