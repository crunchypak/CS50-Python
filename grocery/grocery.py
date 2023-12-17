'''
In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d
(which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically
by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input
case-insensitively.

apple
banana
banana
ice cream

1 APPLE
2 BANANA
1 ICE CREAM
'''
def main():
    groceries = {}
    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            break
        else:
            if (item in groceries):
                groceries[item] += 1
            else:
                groceries[item] = 1
    sorted_groceries = sorted(groceries.keys())
    #dict_print(groceries)
    #print(sorted_groceries)
    print()
    for item in sorted_groceries:
        print(f"{groceries[item]} {item}")

def dict_print(a_dict):
    for item, num in a_dict.items():
        print(f"{num} {item}")

main()
