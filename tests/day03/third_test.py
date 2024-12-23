import advent.day03.third

def test_third_input():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert 161 == advent.day03.third.foo(input)

def test_day_3_pt_1_answer():
    result = 0

    with open('./advent/day03/input.txt', 'r') as file:
        total = 0
        for line in file:
            total = total + advent.day03.third.foo(line)

    assert  188116424 == total
