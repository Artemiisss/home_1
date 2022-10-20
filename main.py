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


if __name__ == "__main__":
    first = get_first_name()
    print(f"My first name is:{first}")
    second = get_second_name()
    print(f"My second name is:{second}")
    last = get_last_name()
    print(f"My last name is:{last}")
