"""
Implements the recursive divide-and-conquer portion of the skyline algorithm.

The merge step is implemented in Merge.py.
"""
from Merge import merge_skylines


# Pseudocode:
#
# SKYLINE(buildings)
#     if buildings is empty
#         return an empty list
#
#     if there is only one building
#         return the two skyline points for that building
#
#     split buildings into a left half and a right half
#
#     left_skyline = SKYLINE(left half)
#     right_skyline = SKYLINE(right half)
#
#     return MERGE_SKYLINES(left_skyline, right_skyline)


def skyline(buildings):
    """
    Find the skyline for a list of buildings.

    Each building is stored as:
        (height, left_x, right_x)

    The skyline is returned as:
        [(height, x), ...]

    Parameters:
        buildings: list of building tuples

    Returns:
        list of skyline points
    """

    # No buildings means there is no skyline.
    if not buildings:
        return []

    # A single building produces two skyline points:
    # one at its left edge and one at its right edge.
    if len(buildings) == 1:
        height, left_x, right_x = buildings[0]

        return [
            (height, left_x),
            (0, right_x)
        ]

    # Split the list into two halves.
    midpoint = len(buildings) // 2

    left_buildings = buildings[:midpoint]
    right_buildings = buildings[midpoint:]

    # Find the skyline for each half.
    left_skyline = skyline(left_buildings)
    right_skyline = skyline(right_buildings)

    # Merge both halves into one skyline.
    return merge_skylines(left_skyline, right_skyline)
