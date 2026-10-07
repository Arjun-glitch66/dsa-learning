# Day 07: HashMap Counting and Multiset

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | [Intersection_of_2_arrays_II.py](./Intersection_of_2_arrays_II.py) | Build a frequency dictionary for the first array. Iterate through the second array, append an element when its frequency is greater than 0, then decrement its frequency. Remove the key when its frequency becomes 0. | O(n + m) | O(n) |
| Variant 1 | [Intersection_of_2_arrays.py](./Intersection_of_2_arrays.py) | Store the elements of the first array as unique values. Iterate through the second array, and when an element is present, add it to the result and remove it to prevent duplicates. | O(n + m) | O(n) |
| Variant 2 | [Union_of_Two_Arrays.py](./Union_of_Two_Arrays.py) | Add all elements from the first array to the result, then add all elements from the second array while preserving duplicates. | O(n + m) | O(n + m) |
| Variant 3 | [Find_Common_Characters.py](./Find_Common_Characters.py) | Build character frequencies and compare the frequency of each character across all words by keeping the minimum frequency. Add each common character according to its final frequency. | O(T + k × l) | O(l) |
| Variant 4 | [Intersection_of_3_Sorted_Arrays.py](./Intersection_of_3_Sorted_Arrays.py) | Use three pointers for the sorted arrays. If all three current elements are equal, add the element and move all three pointers. Otherwise, move the pointer pointing to the smallest element. | O(n + m + k) | O(1) |