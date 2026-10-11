# Day 01: Two Sum

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | [Two_Sum.py](./Two_Sum.py) | Build a hashmap to store each number and its index. For every element, calculate its complement (`target - nums[i]`). If the complement exists in the hashmap, return both indices. Otherwise, store the current number and its index. | O(n) | O(n) |
| Variant 1 | [Two_Sum_II.py](./Two_Sum_II.py) | Use two pointers at the beginning and end of the sorted array. If the sum is smaller than the target, move the left pointer forward. If the sum is larger, move the right pointer backward. Return the 1-based indices when the sum matches the target. | O(n) | O(1) |
| Variant 2 | [Pair_with_given_sum_in_sorted_array.py](./Pair_with_given_sum_in_sorted_array.py) | Use two pointers on the sorted array to find pairs whose sum equals the target. Increment the count and move both pointers when a pair is found. Otherwise, move the pointer based on whether the sum is smaller or larger than the target. | O(n) | O(1) |

## Key Concepts

- **Hashmap lookup:** Find complements efficiently using a dictionary.
- **Two pointers:** Solve pair-sum problems efficiently on sorted arrays.
- **Pair counting:** Count pairs with a target sum without using extra data structures.