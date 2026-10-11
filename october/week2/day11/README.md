# Day 11: Two Pointers — Merge Sorted Array

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | [Merge_Sorted_Array.py](./Merge_Sorted_Array.py) | **Brute force:** Copy the valid elements from both arrays into a new array, manually sort it using nested loops and swaps, then copy the result back into `nums1`. | O((m + n)²) | O(m + n) |
| Variant 1 | [Merge_2_Sorted_Array.py](./Merge_2_Sorted_Array.py) | Use three pointers to compare elements from both sorted arrays and place the smaller element into a result array. Copy the remaining elements after one array is exhausted. | O(m + n) | O(m + n) |
| Variant 2 | [Decompress_RLE_List.py](./Decompress_RLE_List.py) | Calculate the output size from the frequencies, create a result array and fill it by repeating each value according to its frequency. | O(n + L) | O(L) |

## What I Learned

- Merge two sorted arrays using pointers and comparisons.
- Use nested loops and swaps for a brute-force sorting approach.
- Use array indexing to fill a result array without `append()` or `pop()`.
- Decompress a run-length encoded list using frequency-value pairs.

## Complexity Notes

- **Primary:** `m` and `n` are the lengths of the valid portions of the input arrays.
- **Decompress RLE:** `n` is the input length and `L` is the total length of the decompressed output.