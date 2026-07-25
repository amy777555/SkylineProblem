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
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        for line in file:
            # Remove any leading/trailing whitespace or newline characters
            line = line.strip()
            
            # Skip empty lines to prevent index errors
            if line:
                # Split the line into its three components based on the comma delimiter
                parts = line.split(',')
                
                # Convert the parsed strings into integers, stripping extra spaces just in case
                h = int(parts[0].strip())
                l = int(parts[1].strip())
                r = int(parts[2].strip())
                
                # Add the formatted building tuple to our list
                buildings.append((h, l, r))
                
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
    # Open the file in write mode (this will create the file if it doesn't exist)
    with open(file_path, 'w') as file:
        # Iterate through each point in the skyline result
        for h, x in skyline:
            # Write the height and x-coordinate separated by a comma and space, followed by a newline
            file.write(f"{h}, {x}\n")
