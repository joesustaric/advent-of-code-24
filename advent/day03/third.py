import re

def foo(input):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, input)

    p = r"\d+,\d+"
    total = 0
    
    for item in matches:
        match = re.findall(p, item)
        values = match[0].split(',')
        total += int(values[0]) * int(values[1])

    return total
