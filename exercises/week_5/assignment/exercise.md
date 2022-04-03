# Assignment Week 5: Vignère Cipher

You already implemented a solution for the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
in week 3. As this cipher is quite weak, let's turn to another cipher, the
[Vignère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

Like the Caesar cipher, the Vignère cipher is a simple substitiution algorithm,
that means, each letter is replaced by another letter. In the Caesar cipher, each
letter is shifted the same number of times. And this number is the key. In Vignère
these number of shifts change from letter to letter. The number of shifts are given
by a keyword which is repeated until it matches the length of the text to be encrypted.

For simplification we assume, that only letters are encrypted and that we only have
to deal with lower case letters. Let's have a look at the following example:

- In the first line there is the clear text.
- In the second line there is the repeated keyword `random`.
- In the third line the letter from the keyword is replaced by it's position in the
  alphabet (a: 0, b: 1, c: 2, ... z: 25). As `r` is on position 17, there is a 17 in
  the first position of the third row. This postion determines how often the corresponding
  letter from the clear text has to be shifted.
- In the fourth line you can see the secret text. The first letter `p` from the clear
  text is shifted 17 times and results in `g` (as the end of the alphabet is already
  reached after 11 shifts, one starts again at the beginning of the alphabet). The second
  letter `y` is shifted 0 times as the `a` from `random` is at position 0 of the alphabet.
  Thus, this `y` is mapped to `y`. Important: The blank is not shifted as it is no
  letter. However the repetion of the keyword in line two is not influenced by that.

|             |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Clear Text  | p   | y   | t   | h   | o   | n   |     | i   | s   |     | b   | e   | a   | u   | t   | i   | f   | u   | l   |
| Keyword     | r   | a   | n   | d   | o   | m   | r   | a   | n   | d   | o   | m   | r   | a   | n   | d   | o   | m   | r   |
| Position    | 17  | 0   | 13  | 3   | 14  | 12  | 17  | 0   | 13  | 3   | 14  | 12  | 17  | 0   | 13  | 3   | 14  | 12  | 17  |
| Secret Text | g   | y   | g   | k   | c   | z   |     | i   | f   |     | p   | q   | r   | u   | g   | l   | t   | g   | c   |

## Your Task

Implement a program, that gets a text as input and in addition a keyword, which is
the number of shifts.

- Implement a function `encrypt_letter()`, that gets a character and the key as input.
  The return value will be the encrypted character.
- Implement a function `calculate_shifts()`, that gets a letter as input parameter
  and returns the position of this letter in the alphabet (starting with `a` at position 0):
- Implement a function `encrypt_text()`, that gets a text and a keyword as input and
  returns the encrypted text. This function calls both `calculate_shifts()`and `encrpyt_letter()`

### Hint 1

The function `encrypt_text()` should do the following:

- The function steps through the clear text character by character.
- A counter is required, which steps through the letters of the keyword.
- The counter determines the letter from the keyword, which defines the number of shifts.
- The counter is incremented. If the counter is bigger than the length of the keyword
  , it should be set back to 0. This can be implemented with a simple modulo operation.
- The identified character of the keyword is taken as input for the function `calculate_shifts()`
- The output of this function is the key, which is the second parameter for the function
  `encrypt_letter()`. The first parameter is the character, identified at the beginning of this list
- The function `encrypt_letter()` should only be called, if the character is a letter.

### Hint 2

To check if a given character is a letter, you can use the string method `.isalpha ()`. This methods returns `True` if all characters in the string are letters. If there
is a character, which is not a letter, the method returns `False`. Example: `"A".isalpha()`
is `True`, whereas `"2".isalpha()` returns `False`.

### Hint 3

Get both the clear text and the keyword by the `input()` function. Before you pass
these strings to `encrypt_text()` turn all letters into their lower equivalents using
`.lower()`. Finally, print the return value from `encrypt_text()`.

### Hint 4

If you want to test your programm, the keywords `a` or `Aaa` should result in the clear text.

### Example

    Which text should be encrypted: Python is Really Beautiful
    Which keyword should be used? Random
    gygkcz if fqrlyb nvahwwrll
