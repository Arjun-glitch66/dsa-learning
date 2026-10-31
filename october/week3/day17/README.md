# Day 17: String — Prefix Checking & Rotation

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| Variant 1 | [words_occurs_at_prefix.py](./words_occurs_at_prefix.py) | Split the sentence into individual words, check whether each word starts with the given search word using slicing, and return the 1-based position of the first matching word. | O(N + W × P) | O(N) |
| Variant 2 | [rotate_string.py](./rotate_string.py) | Check whether both strings have equal lengths. Concatenate the original string with itself and check whether the goal string exists inside the concatenated string. | O(N) | O(N) |

## What I Learned

- Check whether a word is a prefix of another word using string slicing.
- Use `split()` to separate a sentence into individual words.
- Return the 1-based index of a matching word.
- Understand string rotation using concatenation.
- Use `s + s` to identify whether one string is a valid rotation of another.

## Complexity Notes

- **Check If a Word Occurs As a Prefix:** `N` is the sentence length, `W` is the number of words, and `P` is the length of the search word. Splitting the sentence takes O(N), and checking the prefixes takes O(W × P) in the worst case. Space is O(N) for the split words.
- **Rotate String:** `N` is the length of the strings. Concatenation and substring checking take O(N) time overall for this approach, with O(N) auxiliary space for the concatenated string.