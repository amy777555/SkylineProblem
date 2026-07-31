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
-Describe the Skyline Problem and the purpose of the project in general terms

This project is a Python implementation intended to calculate the outermost shape of a city's skyline formed by an assortment of rectangular buildings with a timespace complexity of O(nlogn). Given a list of varying heights as well as left and right x-coordinates in the form of non-negative integers, the program will then calculate the rectangular strips which form the skyline and return them within the output file in the form of the tuple pair (h, l) where h is the height of the strip and l is the x-coordinate of the strip's left side.


---

## Problem Statement
-Describe the Skyline Problem in detail.
-What is given? what is the desired output? why is this problem challenging?

The outline of a city's skyline is formed by a collection of rectangular buildings when viewed from a distance. Each of these rectangular buildings possess a rectangular strip which form the outermost shape of the skyline buildings. The goal of this program is to design an algorithm that will calculate the rectangular strip for an inputted list of heights and x-coordinates pertaining to a set of buildings such that the skyline may be graphed.

---

## Solution Approach
-Explain the algorithm in words and from a high-level view
-Talk about the divide-and-conquer strategy, recursive subdivision, and the merge process

The program will first read the input file and organize the provided information into a list named "buildings" with each building in the list being stored as (height, left_x, right_x). Once the list has every building stored inside it, a middle point will be calculated in order to divide the list in 2 as part of our divide-and-conquer strategy. After splitting the list into two separate lists the skyline method is called on both halves in order to return the skyline points of every building in the two lists and storing them in the corresponding variables left_buildings and right_buildings. Once the skylines are calculated, they will be merged back together by the merge_skylines function and returned ___   

(Not finished)

---

## Algorithm Description
-Describe the algorithm step-by-step.

The algorithm we have implemented works by 

(Definitely Not finished)

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

Explain what each tuple represents.

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
