import names


def get_first_name():
    first_name = names.get_first_name(gender='male')
    return first_name


def get_second_name():
    second_name = names.get_full_name(gender='male')
    return second_name


def get_last_name():
    last_name = names.get_last_name()
    return last_name
