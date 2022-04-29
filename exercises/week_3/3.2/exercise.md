One of the nice features of Python is that it supports [Unicode](https://en.wikipedia.org/wiki/Unicode).
Therefore it is possible to use emojis just like other characters in strings. In this exercise
you will use this feature to build an emoji translator.

Below is a dictionary that maps English terms to Emojis (broken into multiple lines for better readability).

    {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍"
    }

<br/>

Use this dictionary to build a program that:

1. Reads a sentence from the user.
2. Replaces all the words in the sentence with the corresponding Emoji.

Below is an example execution of the program:

    Please enter a sentence: I'm so excited to learn python
    I'm so 🤩 to finally learn 🐍

<br/>

---

# Hint

Use the `.split()` method to split a sentence into its words. The result of

    sentence = "This is a test"
    words = sentence.split()
    print(words)

<br/>

is

    ["This", "is", "a", "test"]

<br/>

You should also be careful about spaces in the resulting sentence.