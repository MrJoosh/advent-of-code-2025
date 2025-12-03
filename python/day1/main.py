DIAL_START = 50


def main(input_file_path: str) -> int:
    """
    Main function to calculate the password from the input file.
    """
    password: int = 0
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        position = DIAL_START
        for rot in input_file.read().split("\n"):
            dir = rot[:1]
            distance = int(rot[1:])

            position, num_zeros = rotate_dial(position, dir, distance)
            password += num_zeros
    return password


def rotate_dial(start: int, direction: str, distance: int) -> tuple[int, int]:
    """
    Helper function to calculate the new position of the dial after the specified rotation
    """
    if direction == "L":
        result = start - distance
        num_zeros = ((start - 1) // 100) - ((result - 1) // 100)
    elif direction == "R":
        result = start + distance
        num_zeros = (result // 100) - (start // 100)
    else:
        raise ValueError(f"Invalid direction: {direction}")
    return result % 100, num_zeros


if __name__ == "__main__":
    print(f"Test: {main('test.txt')}")
    print(f"Main: {main('input.txt')}")
