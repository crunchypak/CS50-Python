'''
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively)
 forty-two or forty two. Otherwise output No.

 What is the Answer to the Great Question of Life, the Universe, and Everything?
'''

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").upper().strip()
    match answer:
        case "42" | "FORTY-TWO" | "FORTY TWO":
            print("Yes")
        case _:
            print("No")

main()