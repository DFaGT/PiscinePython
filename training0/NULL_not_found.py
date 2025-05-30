def NULL_not_found(obj: any) -> int:
    """Prints the type of various null-like values and returns 0 if recognized, 1 otherwise."""
    # NoneType
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
        return 0
    # NaN (float)
    if isinstance(obj, float) and obj != obj:
        print(f"Cheese: {obj} {type(obj)}")
        return 0
    # False (bool)
    if isinstance(obj, bool) and obj is False:
        print(f"Fake: {obj} {type(obj)}")
        return 0
    # Zero (int)
    if isinstance(obj, int) and obj == 0:
        print(f"Zero: {obj} {type(obj)}")
        return 0
    # Empty string
    if isinstance(obj, str) and obj == "":
        print(f"Empty: {obj} {type(obj)}")
        return 0
    # Not a recognized null type
    print("Type not Found")
    return 1


def main():
    """Main function (no operation)."""
    pass


if __name__ == "__main__":
    main()
