import random
import string


def get_random_int(number_of_digits: int = 9) -> str:
    """Метод возвращает рандомное число с длиной <number_of_digits> символов."""
    digits = string.digits
    new_random_int = "".join(random.choices(digits, k=number_of_digits))
    return new_random_int.lstrip("0").ljust(number_of_digits, random.choice(digits))
