DIAL_START = 50


def main(input_file_path: str):
    """
    Main function to calculate the password from the input file.
    """
    password: int = 0
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        position = DIAL_START
        for rot in input_file.read().split("\n"):
            dir = rot[:1]
            distance = int(rot[1:])

            position = rotate_dial(position, dir, distance)
            if position == 0:
                password += 1
    print(f"Password: {password}")


def rotate_dial(start: int, direction: str, distance: int) -> int:
    """
    Helper function to calculate the new position of the dial after the specified rotation
    """
    if direction == "L":
        result = start - distance
    elif direction == "R":
        result = start + distance
    else:
        raise ValueError(f"Invalid direction: {direction}")
    return result % 100


if __name__ == "__main__":
    # main("test.txt")
    main("input.txt")
