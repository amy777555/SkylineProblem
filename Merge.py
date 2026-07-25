"""
This is our merge algorithm that'll work with the array division algorithm
The recursive skyline() made by Amy will divide the buildings
This combines those two skylines into a single skyline.
The predicted complexity is O(n)

merge function should be called similar to the following:
leftSkyline = skyline(buildings[:mid])
rightSkyline = skyline(buildings[mid:])

return merge_skylines(leftSkyline, rightSkyline)

Pseudo Code:
MERGE(leftSkyline, rightSkyline)

    leftHeight = 0
    rightHeight = 0

    while both skylines still contain strips
        compare current x-coordinate

        if left strip occurs first
            update leftHeight
        else if right strip occurs first
            update rightHeight
        else
            update both heights

        currentHeight = max(leftHeight, rightHeight)
        append strip if height changed

    append remaining strips
    remove redundant strips
    return merged skyline
"""


def append_strip(result, height, x):
    """
    Adds a strip to the skyline while removing redundant strips.

    A strip will be considered redundant if...:
        - it has the same height as the previous strip
        - or has the same x-coordinate as the previous strip

    parameters for code:
    result : list
        Skyline currently being built.
    height : int
        Height of the new strip.
    x : int
        X-coordinate of the strip.
    """

    #if statement for empty skyline
    if not result:
        result.append((height, x))
        return

    previous_height, previous_x = result[-1]

    #if heights are the same, the "height" will not change, essentially a redundancy check
    if previous_height == height:
        return

    #if a new strip has the same x coordinates, the previous strip is overriden
    if previous_x == x:
        result[-1] = (height, x)
    else:
        result.append((height, x))


def merge_skylines(left_skyline, right_skyline):
    """
    Merge two skylines into one skyline.

    parameters:
    left_skyline : list of tuples
        [(height, x), ...]
    right_skyline : list of tuples
        [(height, x), ...]

    returns:
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

    mergedSky = []

    i = 0
    j = 0

    left_height = 0
    right_height = 0

    #will process both skylines at the same time
    while i < len(left_skyline) and j < len(right_skyline): #for following skylines, remember!! i for left, j for right

        left_strip = left_skyline[i]
        right_strip = right_skyline[j]

        #left skyline is appended first
        if left_strip[1] < right_strip[1]:

            x = left_strip[1]
            left_height = left_strip[0]
            current_height = max(left_height, right_height)

            append_strip(mergedSky, current_height, x)

            i += 1 #increment left

        #if the right skyline is appended first
        elif right_strip[1] < left_strip[1]:

            x = right_strip[1]
            right_height = right_strip[0]
            current_height = max(left_height, right_height)

            append_strip(mergedSky, current_height, x)


            j += 1 #increment right

        #else statement for if both the skylines change at the exact same x value
        else:

            x = left_strip[1]

            left_height = left_strip[0]
            right_height = right_strip[0]

            current_height = max(left_height, right_height)

            append_strip(mergedSky, current_height, x)

            #increment both left/right
            i += 1
            j += 1

    #appends any extra strips from the left skyline
    while i < len(left_skyline):
        append_strip(
            mergedSky,
            left_skyline[i][0],
            left_skyline[i][1]
        )
        i += 1

    #appends any extra strips from the right skyline
    while j < len(right_skyline):
        append_strip(
            mergedSky,
            right_skyline[j][0],
            right_skyline[j][1]
        )
        j += 1

    return mergedSky #return everything as the merged skyline
