import re


def has_numbers(exp):
    return bool(re.search(r'\d', exp))


def get_only_numbers(exp):
    return re.sub(r'\D', '', exp)


def get_only_letters(exp):
    return re.sub(r'\d+', '', exp)
