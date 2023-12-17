'''
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter
was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs
that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
Input: Twitter
Output: Twttr
'''

def main():
    inputStr = input("Input: ")
    print("Output: " + convert(inputStr))

def convert(inputStr):
    finalStr = ""
    for c in inputStr:
        l = c.lower()
        if (l != "a" and l != "e" and l != "i" and l != "o" and l != "u"):
            finalStr += c
    return finalStr

main()