# Day 13: Sliding Window

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | [max_avg_subarray.py](./max_avg_subarray.py) | **Fixed-size Sliding Window:** Calculate the first window sum, then add the incoming element and remove the outgoing element to find the maximum average. | O(n) | O(1) |
| Variant 1 | [max_sum_subarray.py](./max_sum_subarray.py) | **Fixed-size Sliding Window:** Calculate the first window sum and update the current sum as the window moves. Track the maximum sum found. | O(n) | O(1) |
| Variant 2 | [minimum_size_subarray.py](./minimum_size_subarray.py) | **Variable-size Sliding Window:** Expand the window using the right pointer and shrink it using the left pointer while the sum is greater than or equal to the target. Track the minimum valid length. | O(n) | O(1) |

## What I Learned

- Solve contiguous subarray problems using the Sliding Window technique.
- Use a fixed-size window to find the maximum sum and maximum average.
- Use two pointers to expand and shrink a variable-size window.
- Update the window sum by adding incoming elements and removing outgoing elements.
- Track the maximum sum or minimum subarray length without recalculating the entire window.
- Use array indexing to solve problems efficiently without unnecessary extra space.

## Complexity Notes

- **Maximum Average Subarray:** `n` is the length of the input array and `k` is the window size.
- **Maximum Sum Subarray:** `n` is the length of the input array and `k` is the window size.
- **Minimum Size Subarray Sum:** `n` is the length of the input array. Each pointer moves forward at most `n` times, giving O(n) time complexity.
- **Space Complexity:** All three approaches use O(1) auxiliary space, excluding the input array.
