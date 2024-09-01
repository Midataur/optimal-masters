# optimal-masters
Planning your masters is easy with the magic of linear programming!

## What is this

The unimelb maths masters has a lot of different options. I was having trouble deciding what to do (and bored), so I decided to write a constraint solver that could help me out. Feel free to use it. It should be easy enough to modify it to work for other masters.

## Usage

1. Install `gurobipy` using `pip install gurobipy`.
2. Scroll through the data file and change the weights appropriately. Alternately, set `demo = True` in `main.py`.
4. Run `python main.py`.

Notes:

Prerequisites are not implemented yet, so I did a janky hack to make sure Random Processes comes after Advanced Probability. Keep this in mind if you are not starting in 2025 sem 1.
