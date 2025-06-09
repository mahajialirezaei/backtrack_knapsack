# Backtrack Knapsack

A simple Python implementation of the classic 0/1 Knapsack problem using a backtracking (brute-force) search. Given a set of items, each with a weight and a value, and a knapsack with a maximum weight capacity, this program explores all possible combinations of items to find the one that maximizes total value without exceeding the capacity.

---

## Table of Contents

- [Problem Statement](#problem-statement)  
- [Approach](#approach)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Example](#example)  
- [Directory Structure](#directory-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Problem Statement

Given:
- **N** items, each with  
  - weight \( w_i \)  
  - value \( v_i \)  
- knapsack capacity **W**

Select a subset of the items such that:
1. The **sum of selected weights** ≤ **W**  
2. The **sum of selected values** is **maximized**

This is the 0/1 Knapsack variant: each item can be either taken or left.

---

## Approach

This repository uses **backtracking** (exhaustive search) to explore every subset of the N items:

1. **Decision Tree**  
   At each step \( i \), decide to:
   - **Include** item \( i \) (if it doesn’t exceed capacity)  
   - **Exclude** item \( i \)

2. **Recursive Exploration**  
   Recurse on the next item \( i+1 \) with the updated remaining capacity and accumulated value.

3. **Prune**  
   If the current weight sum exceeds **W**, that branch is abandoned.

4. **Record Best**  
   Whenever you reach the end (all items considered), compare the accumulated value to the best found so far and update if better.

**Time Complexity:** \( O(2^N) \)  
**Space Complexity:** \( O(N) \) recursion depth

---

## Features

- Simple, dependency-free Python script  
- Easy to extend to track which items were chosen  
- Prints both maximum value and the corresponding item indices  
- Demonstrates fundamental backtracking pattern  

---

## Prerequisites

- Python 3.6 or higher

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mahajialirezaei/backtrack_knapsack.git
   cd backtrack_knapsack
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

---

## Usage

Edit the `main.py` file or pass your own inputs via command line:

```bash
python main.py
```

By default, `main.py` may contain a sample set of weights, values, and capacity. To customize:

1. Open `main.py`.
2. Modify the lists:

   ```python
   values = [ /* your item values */ ]
   weights = [ /* your item weights */ ]
   max_capacity = /* your knapsack capacity */
   ```
3. Run again:

   ```bash
   python main.py
   ```

---

## Example

Suppose we have 4 items:

| Item | Weight | Value |
| ---- | ------ | ----- |
| 0    | 2      | 12    |
| 1    | 1      | 10    |
| 2    | 3      | 20    |
| 3    | 2      | 15    |

Knapsack capacity = 5

Running the script:

```bash
$ python main.py
Maximum value obtainable: 37
Items selected (0-based indices): [0, 2, 3]
```

---

## Directory Structure

```
backtrack_knapsack/
├── .idea/                # IDE configuration (PyCharm)
├── main.py               # Backtracking knapsack implementation
└── README.md             # This file
```


## 🛠 Developer

Developed by [Mohammad Amin Haji Alirezaei](https://github.com/mahajialirezaei)
Feel free to ⭐️ this repo or open an issue if you'd like to contribute or have questions!

