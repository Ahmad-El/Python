from specific_decoration import decoration


@decoration
def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = purse.copy()
    if "gold_ingots" in new_purse:
        new_purse["gold_ingots"] += 1
    else:
        new_purse["gold_ingots"] = 1
    return new_purse


@decoration
def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = purse.copy()
    if (new_purse.get("gold_ingots") is not None
            and new_purse.get("gold_ingots") > 0):
        new_purse["gold_ingots"] -= 1
    return new_purse


@decoration
def empty(purse: dict[str, int]) -> dict[str, int]:
    new_purse = purse.copy()
    new_purse.clear()
    new_purse["gold_ingots"] = 0
    return new_purse


if __name__ == "__main__":
    purse: dict[str:int] = {}
    purse = add_ingot(get_ingot(add_ingot(empty(purse))))
    print(purse)
