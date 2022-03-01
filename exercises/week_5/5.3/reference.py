###BEGIN SOLUTION

def palindrome(sentence):
    reverse = ""
    for letter in sentence:
        reverse = letter + reverse
    
    if reverse.lower() == sentence.lower():
        return True
    else:
        return False
    
###END SOLUTION