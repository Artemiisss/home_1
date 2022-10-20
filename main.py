import names


def get_first_name():
    first_name = names.get_first_name(gender='male')
    return first_name


if __name__ == "__main__":
    first = get_first_name()
    print(f"My first name is:{first}")

