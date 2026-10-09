# Day 09: Two Pointers — Reverse String

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Primary** | [Reverse_String.py](./Reverse_String.py) | Use two pointers from both ends of the character array. Swap the characters and move the left pointer forward and the right pointer backward until they meet. | O(n) | O(1) |
| Variant 1 | [Reverse_String_II.py](./Reverse_String_II.py) | Iterate through the string in steps of `2k`. Reverse the first `k` characters of each block using two pointers. | O(n) | O(n) |
| Variant 2 | [Reverse_Vowels_of_a_String.py](./Reverse_Vowels_of_a_String.py) | Use two pointers and skip non-vowel characters. Swap characters only when both pointers point to vowels. | O(n) | O(n) |
| Variant 3 | [Reverse_Words_in_a_String_III.py](./Reverse_Words_in_a_String_III.py) | Split the sentence into words, reverse each word individually using two pointers, and join the words back together in the original order. | O(n) | O(n) |
| Variant 4 | [Reverse_Prefix_of_Word.py](./Reverse_Prefix_of_Word.py) | Find the first occurrence of the given character and reverse the prefix from index `0` to that position using two pointers. | O(n) | O(n) |

## What I Learned

- Two pointers can reverse a character array in-place by swapping elements from opposite ends.
- `left+=1` moves the left pointer forward, while `right-=1` moves the right pointer backward.
- The condition `left<right` ensures that swapping stops when the pointers meet or cross.
- Python strings are immutable, so converting a string into a list allows individual characters to be swapped.
- `min(i+k-1,len(s)-1)` prevents the right pointer from going beyond the string boundary.
- The `in` and `not in` operators can be used to check whether a character belongs to a set of vowels.
- The same two-pointer reversal logic can be reused for strings, prefixes, individual words, and selected characters.
- `"".join(s)` converts a list of characters back into a string, while `" ".join(words)` combines words with spaces.

## Edge Case I Initially Missed

When reversing a prefix, the given character may not exist in the word. In that case, the original word must be returned unchanged. Similarly, when reversing a string in `k`-sized blocks, the last block may contain fewer than `k` characters, so the right pointer must stay within the string boundaries.

## Key Takeaway

The main lesson is the **two-pointer swap pattern**. Instead of creating a separate reversed array, we can swap elements from opposite ends and gradually move inward. By changing the starting and ending positions, this pattern can solve multiple string problems.