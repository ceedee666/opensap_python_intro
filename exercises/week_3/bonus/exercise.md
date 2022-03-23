# Caeser Cipher extended

The bonus exercise builds upon the assignment of this week. Here is the description of this weeks exercise again:

A [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is a simple encryption technique.
The encryption using a Ceasar cipher replaces a letter in the plain text with a letter that is a fixed number down in the alphabet.
For example, with a shift of 5 the following substitutions would take place:

- a → f
- b → g
- c → h
- ...
- v → a
- w → b
- ...
- z → e

Using this substitutions a plain text can be encrypted:

- Plaintext: programming python is fun!
- Encrypted text: uwtlwfrrnsl udymts nx kzs!

Your task for the bonus exercise is to implement a Caesar cipher with a variable shift. The program should ask the user first
for a number of characters for the shift. Next the program should ask the user for a plain text sentence
and print the encrypted text. Here is an example execution of the program

```
Please enter the number of places to shift: 5
Please enter a sentence: python is fun!
The encypted sentence is: udymts nx kzs!
```

Here is another execution of the program

```
Please enter the number of places to shift: 10
Please enter a sentence: python is fun!
The encypted sentence is: zidryx sc pex!
```

And yet another one

```
Please enter the number of places to shift: 0
Please enter a sentence: python is fun!
The encypted sentence is: python is fun!
```

Your program should check, that only numbers between 0 and 25 are entered for the number of places to shift!

```
Please enter the number of places to shift: 60
You need to enter a number between 0 and 25!
```

## Hint

1. The simple solution using a dictionary will not work for this exercise. Instead you need to build the substitution dynamically.
   This can be done using the [find method](https://docs.python.org/3/library/stdtypes.html?highlight=index#str.find) and some calculations.

```
abc = "abcdefghijklmnopqrstuvw"
char_index = abc.find("f")
encrypted_char = abc[char_index + 5]
```

1. Note, that in the example above there will be an error if char_index +5 is larger then 25. You need to use the modulo (%) operator
   to take care of this situation.
1. In order to check if the user entered a number method [isdecimal()](https://docs.python.org/3/library/stdtypes.html?highlight=isdigit#str.isdecimal) can be used.
1. To avoid handling upper and lower case letters it is best to first convert the user input to lower case.
   After that you only need to take into account lower case letters. A string can be converted into lower case using the .lover() method.
   The result of the following example is: test.

```python
s = "TEST"
s = s.lower()
print(s)
```
