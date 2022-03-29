# Assignment Week 5: Caesar Cipher
[Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher) or Caesar Shift is one of the most widely known encryption techniques. Each letter of a plain text is replaced by another letter down the alphabet. The transformation can be presented by the plain and the shifted alphabet.

|   |||||||||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Plain  |A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
| Cipher |Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|

The cipher alphabet is shifted for example by 2 letters to the right.  More precisely, the alphabet is rotated 2 letters to the right as the `Y` and the `Z` are inserted in the first two positions of the cipher alphabet. The number of shifts (here 2) is called the key.

If you want to encrypt a letter, search the letter in the plain alphabet and replace it with the corresponding letter from the cipher alphabet. For example an A becomes a Y, an H becomes an F.

If you want to decrypt a ciphered message, you just have to go up. Search the letter in the cipher alphabet and replace it with the corresponding letter in the plain alphabet. Thus, when decrypting the A becomes a C, the G becomes an I.

## Your Task
Implement a program, that gets a text as input and in addition a key, which is the number of shifts. 
- Implement a function `encrypt_letter()`, that gets a character and the key as input. The return value will be the encrypted character.
- Implement a function `encrypt_text()`, that gets a text and the key as input and returns the encrypted text. The function steps through the text character by character. If the character is a letter, it is first turned into it's upper equivalent, then the function `encrpyt_letter()` is called.

### Hint 1
There are two Python functions `ord()` and `chr()` which map characters to numbers (more precisly the number of the character in the [ASCII table](https://en.wikipedia.org/wiki/ASCII)). `ord()` takes a character as input and returns the number of this character in the ASCII-table. For example `ord("A")` gives back the number 65. Vice versa `chr()` gives back the character at a given position in the ASCII-table, so `chr(65)` returns the letter "A". As all characters in the table are placed next to each other in alphabetic order, this helps to shift letters. For example chr(ord("A") + 1) returns a "B". Two small issues have to be taken care for: 
- If the cipher alphabet is shifted to the right, what does this mean for the sign of the key?
- In the example above the alphabet is shifted two letters to the right. The letters "Y" and "Z" are inserted at the beginning of the alphabet. How can this big shift to the left be implemented?

### Hint 2
To check if a given character is a letter, you can use the string method `.isalpha()`. This methods returns `True` if all characters in the string are letters. If there is a character, which is not a letter, the method returns `False`. Example: `"A".isalpha()` is `True`, whereas `"2".isalpha()` returns `False`. 

### Example

    Which text should be encrypted: Python is Beautiful
    How many shifts should be taken: 5
    KTOCJI DN WZVPODAPG


# Proposed Tests
- check, if a function `encrypt_letter()` exists
- check, if a function `encrypt_text()` exists
- check if the two functions are nested
- check if the input "A", 1 becomes a "Z", not a "B"
- check other inputs