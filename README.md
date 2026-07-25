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

Describe the Skyline Problem and the purpose of the project in general terms

---

## Problem Statement

Describe the Skyline Problem in detail.

What is given? what is the desired output? why is this problem challenging?

---

## Solution Approach

Explain the algorithm in words and from a high-level view

Talk about the divide-and-conquer strategy, recursive subdivision, and the merge process

---

## Algorithm Description

Describe the algorithm step-by-step.

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
└── test_cases/                        # Additional test inputs and outputs
    ├── test1_input.txt
    ├── test1_output.txt
    ├── test2_input.txt
    ├── test2_output.txt
    ├── test3_input.txt
    ├── test3_output.txt
    ├── test4_input.txt
    ├── test4_output.txt
    ├── test5_input.txt
    └── test5_output.txt
```

---

## Input Format

Describe the expected input format.

Example:

```text
Height, LeftX, RightX
Height, LeftX, RightX
...
```

Explain each value.

---

## Output Format

Describe the output format.

Example:

```text
Height, X
Height, X
...
```

Explain what each tuple represents.

---

## Test Cases

### Test Case 1

**Purpose**

*Describe what this test verifies.*

#### Input

```text
(Add input here.)
```

#### Output

```text
(Add expected output here.)
```

---

### Test Case 2

**Purpose**

*Describe what this test verifies.*

#### Input

```text
(Add input here.)
```

#### Output

```text
(Add expected output here.)
```

---

### Test Case 3

**Purpose**

*Describe what this test verifies.*

#### Input

```text
(Add input here.)
```

#### Output

```text
(Add expected output here.)
```

---

### Test Case 4

**Purpose**

*Describe what this test verifies.*

#### Input

```text
(Add input here.)
```

#### Output

```text
(Add expected output here.)
```

---

### Test Case 5

**Purpose**

*Describe what this test verifies.*

#### Input

```text
(Add input here.)
```

#### Output

```text
(Add expected output here.)
```

---

## Edge Cases Tested

List any edge cases that were tested.


---

## Complexity Analysis

### Time Complexity

Explain the running time of the divide-and-conquer algorithm.

Overall Time Complexity:

**O(n log n)**

---

### Space Complexity

Discuss any additional memory required by the algorithm.

---

## How to Run

### Requirements

- Python 3.x
- No external libraries required

### Execution

```bash
python3 main.py
```

If command-line arguments are supported:

```bash
python3 main.py input.txt output.txt
```
