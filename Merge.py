"""
Merges two skylines produced by the recursive divide-and-conquer algorithm.

The merge operation runs in O(n) time, where n is the total number
of points in both skylines.

merge function should be called similar to the following:
left_skyline = skyline(buildings[:mid])
right_skyline = skyline(buildings[mid:])

return merge_skylines(left_skyline, right_skyline)

Pseudo Code:
MERGE(left_skyline, right_skyline)

    left_height = 0
    right_height = 0

    while both skylines still contain strips
        compare current x-coordinate

        if left strip occurs first
            update left_height
        else if right strip occurs first
            update right_height
        else
            update both heights

        current_height = max(left_height, right_height)
        append strip if height changed

    append remaining strips
    remove redundant strips
    return merged skyline
"""


def append_strip(result, height, x):
    """
    Adds a strip to the skyline while removing redundant strips.

    A strip will be considered redundant if:
        - it has the same height as the previous strip
        - or has the same x-coordinate as the previous strip

    Parameters:
    result : list
        Skyline currently being built.
    height : int
        Height of the new strip.
    x : int
        X-coordinate of the strip.
    """

    # If the skyline is empty
    if not result:
        result.append((height, x))
        return

    previous_height, previous_x = result[-1]

    # Skip redundant height changes
    if previous_height == height:
        return

    # Replace the previous point if the x-coordinate matches
    if previous_x == x:
        result[-1] = (height, x)
    else:
        result.append((height, x))


def merge_skylines(left_skyline, right_skyline):
    """
    Merge two skylines into one skyline.

    Parameters:
    left_skyline : list of tuples
        [(height, x), ...]
    right_skyline : list of tuples
        [(height, x), ...]

    Returns:
    list
        Merged skyline.

    Example:
    Left:
        [(6,1), (0,6)]

    Right:
        [(8,3), (0,5)]

    Output:
        [(6,1), (8,3), (6,5), (0,6)]
    """

    merged_skyline = []

    i = 0
    j = 0

    left_height = 0
    right_height = 0

    # Process both skylines simultaneously
    while i < len(left_skyline) and j < len(right_skyline): # i tracks the left skyline and j tracks the right skyline

        left_strip = left_skyline[i]
        right_strip = right_skyline[j]

        # Process the next strip from the left skyline
        if left_strip[1] < right_strip[1]:

            x = left_strip[1]
            left_height = left_strip[0]
            current_height = max(left_height, right_height)

            append_strip(merged_skyline, current_height, x)

            i += 1 # Increment left

        # Process the next strip from the right skyline
        elif right_strip[1] < left_strip[1]:

            x = right_strip[1]
            right_height = right_strip[0]
            current_height = max(left_height, right_height)

            append_strip(merged_skyline, current_height, x)


            j += 1 # Increment right

        # Both skylines change at the same x-coordinate
        else:

            x = left_strip[1]

            left_height = left_strip[0]
            right_height = right_strip[0]

            current_height = max(left_height, right_height)

            append_strip(merged_skyline, current_height, x)

            # Increment both left/right
            i += 1
            j += 1

    # Appends any extra strips from the left skyline
    while i < len(left_skyline):
        append_strip(
            merged_skyline,
            left_skyline[i][0],
            left_skyline[i][1]
        )
        i += 1

    # Appends any extra strips from the right skyline
    while j < len(right_skyline):
        append_strip(
            merged_skyline,
            right_skyline[j][0],
            right_skyline[j][1]
        )
        j += 1

    return merged_skyline # Return everything as the merged skyline
