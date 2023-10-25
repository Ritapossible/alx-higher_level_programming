#!/usr/bin/python3
def magic_calculation(a, b):
    summ = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                summ += (a ** b) / i
        except Exception:
            summ = b + a
            break
    return (summ)
