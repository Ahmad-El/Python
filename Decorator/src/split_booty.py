import functional_purse as fp


def spllit_booty(*args: dict[str, int]):
    purse: dict[str, int] = {}
    purses: list[dict[str, int]] = []
    total = 0
    for arg in args:
        total += get_value(arg)
    for _ in range(3):
        purses.append(fp.empty(purse))
    if total == 0:
        return tuple(purses)
    remainder = int(total % 3)
    min_value = int(total / 3)

    for _ in range(min_value):
        purses[0] = fp.add_ingot(purses[0])
        purses[1] = fp.add_ingot(purses[1])
        purses[2] = fp.add_ingot(purses[2])

    for i in range(remainder):
        purses[i] = fp.add_ingot(purses[i])

    return tuple(purses)


def get_value(purse: dict[str, int]):
    if purse.get("gold_ingots") is None:
        return 0
    return purse.get("gold_ingots")


if __name__ == "__main__":
    print(spllit_booty({"gold_ingots": 3}, {"gold_ingots": 2}, {"apples": 10}))
