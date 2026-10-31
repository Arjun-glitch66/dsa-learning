# Day 18: Strings — Case Conversion & Last Word Length

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| Variant 1 | [lower_case.py](./to_lower_case.py) | Traverse each character. If it is an uppercase letter, convert it to lowercase using ASCII values (`ord()` and `chr()`). Otherwise, keep the character unchanged. | O(n) | O(n) |
| Variant 2 | [length_of_lastword.py](./length_of_last_word.py) | Start scanning from the end of the string. Skip trailing spaces, then count characters until another space or the beginning of the string is reached. | O(n) | O(1) |

## What I Learned

- Convert uppercase letters into lowercase using ASCII values.
- Understand the difference of 32 between uppercase and lowercase English letters in ASCII.
- Traverse strings character by character using loops.
- Use backward traversal to find the last word in a sentence.
- Skip trailing spaces before counting the last word.
- Solve string problems using basic loops and conditions without shortcut functions like `lower()` and `split()`.

## Complexity Notes

- **To Lower Case:** `n` is the length of the input string. Each character is visited once, and a new result string is constructed. Time complexity is O(n), and auxiliary space is O(n).
- **Length of Last Word:** `n` is the length of the input string. The string is scanned backwards at most once. Time complexity is O(n), and auxiliary space is O(1).