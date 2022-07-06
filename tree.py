# This is for requesting the user input
tree_height = input("How tall is the tree: ")

# This is for converting the tree height to integer
tree_height = int(tree_height)

# This of decrementing the spaces
spaces = tree_height - 1

hashes = 1

stump_spaces = tree_height - 1

while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1

for i in range(stump_spaces):
    print(' ', end="")

print("#")
