def decoration(func):
    def wrapper(purse: dict[str, int]):
        print("SQUEAK")
        return func(purse)

    return wrapper
