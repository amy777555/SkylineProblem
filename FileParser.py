def read_input(file_path):
    """
    Reads a comma-delimited input text file containing building dimensions.

    Expected format per line in the input file:
    H, L, R (where H = Height, L = Left x-coordinate, R = Right x-coordinate)

    Args:
        file_path (str): The absolute path to the input text file.

    Returns:
        list of tuples: A list where each tuple represents a building (H, L, R).
    """
    buildings = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            # Skip empty lines to prevent index errors
            if line:
                parts = line.split(",")

                height = int(parts[0].strip())
                left_x = int(parts[1].strip())
                right_x = int(parts[2].strip())

                buildings.append((height, left_x, right_x))

    return buildings


def write_output(file_path, skyline):
    """
    Writes the computed skyline outer shape to a comma-delimited text file.

    Expected format per line in the output file:
    h, x (where h = height, x = x-coordinate)

    Args:
        file_path (str): The absolute path to where the output file should be saved.
        skyline (list of tuples): The list of (height, x-coordinate) tuples from the algorithm.
    """
    with open(file_path, "w") as file:
        for height, x_coordinate in skyline:
            file.write(f"{height}, {x_coordinate}\n")
