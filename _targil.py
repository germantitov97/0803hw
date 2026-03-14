import random

def get_lucky_numbers(amount: int) -> tuple[int]:
    numbers = tuple(random.sample(range(1, 100 + 1), k=amount))
    return numbers

def input_until_lucky(lucky_numbers: tuple) -> int:
    attempts = 0
    _value_of_lucky_numbers = get_lucky_numbers(lucky_numbers)
    print(_value_of_lucky_numbers) # only for checking purposes
    while True:
        user_input = int(input("put a number: "))
        attempts += 1
        if user_input in _value_of_lucky_numbers:
            break
        else:
            continue
    print(f'you tried {attempts} attempts')
    return attempts

input_until_lucky(4)



