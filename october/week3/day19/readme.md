# Day 19: Buddy Strings

## Folder Contents & Summary

| File | Approach | Time | Space |
| :--- | :--- | :--- | :--- |
| [buddy.py](buddy.py) | Compare both strings character by character and store the first two mismatching indices. Check whether swapping the characters at those positions makes both strings equal. | O(n) | O(1) |

## What I Learned

- Compare two strings character by character.
- Identify mismatching positions using a single loop.
- Store the first and second mismatching indices.
- Check whether swapping two characters makes the strings equal.
- Use basic conditions and variables instead of an extra list.

## Complexity Notes

- `n` is the length of the input strings.
- **Time:** O(n), because the strings are traversed once.
- **Space:** O(1), because only two index variables are used.