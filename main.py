import sys
from FileParser import read_input, write_output
from Skyline import skyline


def main():
    # Enforce that the user provides exactly two absolute paths in the terminal
    if len(sys.argv) != 3:
        print("Usage: python main.py <absolute_path_to_input> <absolute_path_to_output>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        buildings = read_input(input_path)
        skyline_result = skyline(buildings)
        write_output(output_path, skyline_result)

        print(f"Success! Processed {input_path} -> {output_path}")

    except FileNotFoundError:
        print(f"Error: Could not find the input file at {input_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
