# Project 2 code

# MergeSort
def mergeSort():
    pass

# Dynamic Programming
# Problem: 0/1 Knapsack
# Maximize value without exceeding cap


memo = {}


def knapsack(weights, values, cap, i=0):
    # Base Case: No items left OR no capacity
    if i >= len(weights) or cap == 0:
        return 0

    # Check if already computed in memo dictionary
    if (i, cap) in memo:
        return memo[(i, cap)]

    # Choice 1: Do not take current item
    not_take = knapsack(weights, values, cap, i + 1)

    # Choice 2: Take current item, but only if it fits
    take = 0
    if weights[i] <= cap:
        take = values[i] + knapsack(weights, values, cap - weights[i], i + 1)

    # Store results for intermediate calculation
    memo[(i, cap)] = max(take, not_take)

    return memo[(i, cap)]


# Greedy Algorithm


def activitySelection():
    pass

# Contains tests & function calls


def main():
    ########## Dynamic Programming Knapsack 0/1 ##########
    print("\nDynamic Programming Test (Knapsack 0/1):\n")
    # -------- Test Case 1: Small Input --------
    weights1 = [1, 2, 3]
    values1 = [10, 15, 40]
    cap1 = 5

    memo.clear()
    print("Test 1 (Small):", knapsack(weights1, values1, cap1))
    # Expected: 55

    # -------- Test Case 2: Medium Input --------
    weights2 = [2, 3, 4, 5, 8]
    values2 = [3, 4, 5, 6, 11]
    cap2 = 5

    memo.clear()
    print("Test 2 (Medium):", knapsack(weights2, values2, cap2))
    # Expected: 7

    # -------- Test Case 3: Edge Case --------
    weights3 = []
    values3 = []
    cap3 = 10

    memo.clear()
    print("Test 3 (Edge - Empty):", knapsack(weights3, values3, cap3))
    # Expected: 0

    print()


if __name__ == "__main__":
    main()
