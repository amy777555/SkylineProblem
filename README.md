# Skyline Problem
### CS 4306 – Algorithm Analysis

---

## Team Information

| Name | Email |
|--------|--------|
| Amy Ward | award62@students.kennesaw.edu |
| Brenden Toussant | btoussan@students.kennesaw.edu |
| Jordan Reid | jreid71@students.kennesaw.edu |
| Caleb Mickens | cmicken3@students.kennesaw.edu |

---

## Overview

This project is a Python implementation that calculates the outermost shape of a city's skyline formed by a collection of rectangular buildings. Given a list of building heights along with their left and right x-coordinates, the program computes the rectangular strips that define the skyline and writes them to an output file as `(height, x-coordinate)` pairs. The divide-and-conquer algorithm runs in **O(n log n)** time.

---

## Problem Statement

The outline of a city's skyline is formed by a collection of rectangular buildings when viewed from a distance. The visible portions of these buildings define the outermost shape of the skyline. Given a list of building heights and their corresponding left and right x-coordinates, the goal of this project is to design an algorithm that calculates the skyline by identifying the rectangular strips that make up its outer boundary. The resulting skyline is written to an output file as a sequence of skyline points.

---

## Solution Approach

The program first reads the input file and stores each building as a tuple in the form `(height, left_x, right_x)` within a list named `buildings`. Once all of the buildings have been loaded, the list is divided into two halves as part of the divide-and-conquer strategy. The `skyline()` function is then called recursively on each half to compute the skyline points, which are stored in `left_skyline` and `right_skyline`. Finally, the `merge_skylines()` function combines the two partial skylines into a single skyline, which is returned as the final result.

---

## Algorithm Description

The algorithm begins by reading the input file and storing each building as a tuple in the form `(height, left_x, right_x)`. If the input contains no buildings, an empty skyline is returned. If only one building is present, the algorithm returns two skyline points: one marking where the building begins and another where it returns to ground level.

For larger inputs, the list of buildings is divided into two halves. The `skyline()` function is then called recursively on each half until every recursive call reaches the base case of a single building.

After the recursive calls return, the `merge_skylines()` function combines the two partial skylines into one complete skyline. During the merge process, the algorithm compares the current skyline points from both halves, tracks the current height of each skyline, and records the maximum visible height at each x-coordinate. The `append_strip()` helper function removes redundant skyline points by ignoring duplicate height changes and replacing points that share the same x-coordinate.

Once all skyline points have been processed and merged, the completed skyline is returned and written to the output file.

---

## Pseudocode

### Skyline Algorithm

```text
SKYLINE(buildings)
    if buildings is empty
        return an empty list

     if there is only one building
        return the two skyline points for that building

    split buildings into a left half and a right half

    left_skyline = SKYLINE(left half)
    right_skyline = SKYLINE(right half)
    return MERGE_SKYLINES(left_skyline, right_skyline)
```

### Merge Algorithm

```text
APPEND_STRIP(result, height, x)

    if result is empty
        append (height, x)
        return

    previous_height, previous_x = last strip in result

    if previous_height equals height
        return

    if previous_x equals x
        replace the last strip with (height, x)
    else
        append (height, x)


MERGE_SKYLINES(left_skyline, right_skyline)

    merged_skyline = empty list

    i = 0
    j = 0

    left_height = 0
    right_height = 0

    while both skylines still contain strips

        left_strip = left_skyline[i]
        right_strip = right_skyline[j]

        if left strip occurs first
            x = left strip's x-coordinate
            update left_height
            current_height = max(left_height, right_height)
            append strip if height changed
            increment i

        else if right strip occurs first
            x = right strip's x-coordinate
            update right_height
            current_height = max(left_height, right_height)
            append strip if height changed
            increment j

        else
            x = the shared x-coordinate
            update both heights
            current_height = max(left_height, right_height)
            append strip if height changed
            increment i and j

    append any remaining strips from left_skyline
    append any remaining strips from right_skyline

    return merged_skyline
```
---

## Project Structure

```text
SkylineProject/

├── README.md                          # Project documentation
├── main.py                            # Coordinates program execution
├── Skyline.py                         # Recursive divide-and-conquer algorithm
├── Merge.py                           # Combines two skylines into one
├── FileParser.py                      # Handles input parsing and output generation
│
└── InputsOutputs/                        # Test inputs and outputs
    ├── Input1.txt
    ├── Output1.txt
    ├── Input2.txt
    ├── Output2.txt
    ├── Input3.txt
    ├── Output3.txt
    ├── Input4.txt
    ├── Output4.txt
    ├── Input5.txt
    └── Output5.txt
```

---

## Input Format

The input file will contain the heights of each building first, followed by the x-coordinates of their left edge (LeftX) and right edges (RightX) as shown below:

Example:

```text
Height, LeftX, RightX
Height, LeftX, RightX
...
```

---

## Output Format

The output file will list tuples containing the height and x-coordinate of each building's calculated rectangular strip which forms the skyline as shown:

Example:

```text
Height, X
Height, X
...
```

---

## Test Cases

### Test Case 1 — Overlapping Buildings

**Purpose**

Tests the general case where several buildings overlap, requiring the merge step to determine which portions of each building remain visible.

#### Input

```text
6, 1, 6
8, 3, 5
4, 4, 9
2, 7, 12
7, 11, 14
```

#### Output

```text
6, 1
8, 3
6, 5
4, 6
2, 9
7, 11
0, 14
```

---

### Test Case 2 — Single Building

**Purpose**

Checks the recursive base case by ensuring that one building produces only a starting point and an ending point in the skyline.

#### Input

```text
5, 2, 8
```

#### Output

```text
5, 2
0, 8
```

---

### Test Case 3 — Non-Overlapping Buildings

**Purpose**

Checks that buildings separated by empty space are represented as independent skyline segments with the skyline returning to ground level between them.

#### Input

```text
3, 1, 4
5, 6, 9
2, 11, 13
```

#### Output

```text
3, 1
0, 4
5, 6
0, 9
2, 11
0, 13
```

---

### Test Case 4 — Buildings Contained Within a Taller Building

**Purpose**

Tests a case where shorter buildings are completely covered by a taller building and should not appear in the final skyline.

#### Input

```text
10, 1, 10
6, 3, 7
8, 4, 6
```

#### Output

```text
10, 1
0, 10
```

---

### Test Case 5 — Equal Heights and Shared Boundaries

**Purpose**

Exercises the merge step when buildings share boundaries or have the same height, making sure redundant skyline points are not produced.

#### Input

```text
5, 1, 4
5, 4, 7
3, 7, 10
6, 7, 9
```

#### Output

```text
5, 1
6, 7
3, 9
0, 10
```

---

## Edge Cases Tested

- **Single building** — Confirms that the recursive base case is handled correctly.
- **Non-overlapping buildings** — Ensures that separate skyline segments are generated correctly.
- **Fully contained buildings** — Confirms that buildings completely contained within a taller building do not appear in the final skyline.
- **Overlapping buildings** — Tests the merge operation when multiple buildings overlap.
- **Adjacent buildings with equal heights** — Checks that unnecessary height changes are not added to the skyline.
- **Buildings sharing the same x-coordinate** — Verifies that simultaneous skyline changes are merged correctly.
- **Redundant skyline points** — Confirms that duplicate heights and duplicate x-coordinates are removed by `append_strip()`.

---

## Complexity Analysis

### Time Complexity

The algorithm uses a divide-and-conquer approach. It repeatedly divides the list of buildings into two halves until each recursive call contains only one building. Dividing the input in half produces approximately `log n` levels of recursion.

At each level, the skylines from the left and right halves are merged. The merge operation processes each skyline point once, so the total work performed across one level is `O(n)`.

The recurrence relation is:

```text
T(n) = 2T(n / 2) + O(n)
```

Since there are log n recursive levels and each level performs O(n) work, the overall time complexity is:

**O(n log n)**

---

### Space Complexity

The algorithm requires additional space to store the left and right building lists, the skylines produced by the recursive calls, and the final merged skyline. The number of skyline points is proportional to the number of buildings, so these lists require O(n) space.

The recursive call stack contains approximately log n active calls, requiring O(log n) stack space. The skyline lists dominate the recursion stack, so the overall space complexity is linear.

Therefore, the overall space complexity is:

**O(n)**

---

## How to Run

### Requirements

- Python 3.x
- No external libraries are required.

### Execution

Run the program from the command line by providing the absolute path to the input file followed by the desired output file.

```bash
python3 main.py /path/to/input.txt /path/to/output.txt
```

#### Example

```bash
python3 main.py InputsOutputs/Input1.txt InputsOutputs/Output1.txt
```

The program reads the building data from the input file, computes the skyline, and writes the resulting skyline points to the specified output file.
