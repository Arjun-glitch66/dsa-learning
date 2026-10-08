# Day 08: Two Pointers

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | [Valid_Palindrome.py](./Valid_Palindrome.py) | Use two pointers from both ends. Skip non-alphanumeric characters and compare characters after converting them to lowercase. | O(n) | O(1) |
| Variant 1 | [Valid_Palindrome_2.py](./Valid_Palindrome_2.py) | Use two pointers and allow at most one character to be skipped when a mismatch is found. | O(n) | O(1) |
| Variant 2 | [Palindrome_Linked_List.py](./Palindrome_Linked_List.py) | Traverse the linked list using a pointer, store the node values in a list, and use two pointers to check whether the values form a palindrome. | O(n) | O(n) |
| Variant 3 | [Palindromic_Substrings.py](./Palindromic_Substrings.py) | Expand around every possible center. Check both odd-length palindromes using `(i, i)` and even-length palindromes using `(i, i+1)`. | O(n²) | O(1) |
| Variant 4 | [Reverse_Only_Letters.py](./Reverse_Only_Letters.py) | Convert the string into a list and use two pointers from both ends. Skip non-letter characters and swap only when both pointers are on letters. | O(n) | O(n) |

## What I Learned

- Two pointers can be used from opposite ends of a string.
- `continue` skips the current loop iteration and starts the next iteration.
- `current = current.next` moves a linked-list pointer to the next node.
- `None` is stored in the `next` field of the last linked-list node.
- Palindromic substrings can be found by expanding around a center.
- Odd-length palindromes use one center: `(i, i)`.
- Even-length palindromes use two centers: `(i, i+1)`.
- Strings are immutable in Python, so a list can be used when characters need to be swapped.

## Edge Case I Initially Missed

For palindrome problems, I initially focused on directly comparing the characters without considering non-alphanumeric characters and the need to skip them while moving the two pointers.