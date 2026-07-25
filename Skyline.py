from Merge import merge_skylines


def skyline(buildings):
    """
    Find the outer skyline formed by a list of buildings using
    a divide-and-conquer algorithm.

    Each building is represented as:
        (height, left_x, right_x)

    The returned skyline is represented as:
        [(height, x), ...]

    Parameters:
        buildings: A list of building tuples.

    Returns:
        A list of skyline strips represented as (height, x).
    """

    # An empty building list produces an empty skyline.
    if not buildings:
        return []

    # Base case
    # One building forms a two-point skyline.
    if len(buildings) == 1:
        height, left_x, right_x = buildings[0]

        return [
            (height, left_x),
            (0, right_x)
        ]

    # Divide the buildings into two approximately equal halves.
    midpoint = len(buildings) // 2

    left_buildings = buildings[:midpoint]
    right_buildings = buildings[midpoint:]

    # Recursively construct the skyline for each half.
    left_skyline = skyline(left_buildings)
    right_skyline = skyline(right_buildings)

    # Combine the two smaller skylines.
    return merge_skylines(left_skyline, right_skyline)
