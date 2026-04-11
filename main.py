# Project 2 code

# Gavin Wilson
# Stefan Dedic
# Cameron Goz

import time

# Divide & Conquer (D&C) - Problem: Merge Sort
def merge(left, right):
    megred = []
    i = 0
    j = 0

    # compare elements from both halves + add to the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # add remaining elements once one is complete
    while i < len(left): # left
        merged.append(left[i])
        i += 1
    while j < len(right): # right
        merged.append(right[j])
        j += 1

    return merged
    
def mergeSort(array):
    # base: size 0 - 1 = sorted
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    # sort left and right halves
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    # merge and return
    return merge(left, right)


# Greedy Algorithm - Problem: Activity Selection Problem

def activity_selection(activities):
    # Return an empty list if no activities
    if not activities:
        return []
    # Sort activities by finish time
    activities = sorted(activities, key=lambda activity: activity[2])

    # Select the first activity
    selected_activities = [activities[0]]
    last_finish_time = activities[0][2]

    # Select next compatible activities
    for activity in activities[1:]:
        activity_name, start_time, finish_time = activity

        # We select an activity if it starts after or when the last selected activity finishes and does not overlap
        if start_time >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = finish_time

    return selected_activities


# Dynamic Programming - Problem: 0/1 Knapsack
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



# == TEST CASES ==
def DAC_test_cases():
    test_cases = [
        ("Small random array", [5, 2, 9, 1, 3]),
        ("Already sorted array", [1, 2, 3, 4, 5, 6, 7]),
        ("Reverse sorted array", [7, 6, 5, 4, 3, 2, 1]),
        ("Empty array", []),
        ("Single element", [42]),
        ("Medium random array", random.sample(range(1, 1000), 25)),
    ]
    for name, arr in test_cases:
        original = arr[:]  # keep original for display
        start_time = time.perf_counter()
        result = mergeSort(arr)
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time) * 1000

        print(f"Test: {name}")
        print(f"Input:    {original}")
        print(f"Output:   {result}")
        print(f"Time:     {elapsed_ms:.6f} ms")
        print("-" * 50)
    
# Contains tests & function calls

def DP_test_cases():
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

def greedy_test_cases():

    # small input size
    test_case_1 = [
        ("A1", 1, 4),
        ("A2", 3, 5),
        ("A3", 0, 6),
        ("A4", 5, 7),
        ("A5", 8, 9),
        ("A6", 5, 9)
    ]

    # medium input size
    test_case_2 = [
        ("A1", 1, 2),
        ("A2", 3, 4),
        ("A3", 0, 6),
        ("A4", 5, 7),
        ("A5", 8, 9),
        ("A6", 5, 9),
        ("A7", 6, 10),
        ("A8", 8, 11),
        ("A9", 2, 13),
        ("A10", 12, 14)
    ]

    # empty input (edge case)
    test_case_3 = []

    test_cases = [("Small input size ", test_case_1),
                  ("Medium input size ", test_case_2),
                  ("Edge case (empty input)", test_case_3)]
    
    test_case_count = 1

    for test_case in test_cases:
        start = time.perf_counter()
        selected_activities = activity_selection(test_case[1])
        end = time.perf_counter()

        execution_time = (end - start) * 1000 # ms
        print(f"\nTest Case {test_case_count}: {test_case[0]}")

        print("\nInput Activities:")
        for i in range(len(test_case[1])):
            print(f"{test_case[1][i]}")

        print("\nSelected Activities:")
        for n in range(len(selected_activities)):
            print(f"{selected_activities[n]}")

        print(f"Total activities selected: {len(selected_activities)}")
        print(f"Execution time: {execution_time: .6f}ms")
        print("-----------------")
        test_case_count += 1

def main():

    # This calls the D&C test cases for the Merge Sort problem
    DAC_test_cases()
    print("===========================================================")
    # This calls the Greedy test cases for Selection Algorithm problem
    greedy_test_cases()
    print("===========================================================")
    # This calls the Dynamic Programming test cases for Knapsack
    DP_test_cases()


if __name__ == "__main__":
    main()
