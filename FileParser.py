def read_input(file_path):
    """
    Reads a comma-delimited input file of buildings.
    Expected format per line: H, L, R
    Returns a list of tuples: [(H1, L1, R1), (H2, L2, R2), ...]
    """
    buildings = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                # Split by comma and remove extra spaces
                parts = line.split(',')
                h = int(parts[0].strip())
                l = int(parts[1].strip())
                r = int(parts[2].strip())
                buildings.append((h, l, r))
    return buildings

def write_output(file_path, skyline):
    """
    Writes the computed skyline to a comma-delimited output file.
    Expected format per line: h, x
    """
    with open(file_path, 'w') as file:
        for h, x in skyline:
            file.write(f"{h}, {x}\n")
