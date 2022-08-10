# Reading the file and printing the lines in alphabetical order.
with open("name.txt", "r") as file:
    lines = file.readlines()

for line in sorted(lines):
    print("Hello,", line, end="")


# Opening a file called test.log, writing the string 'test succeeded' to it, and then closing it.
with open('test.log', mode='w', encoding='utf-8') as a_file:
    a_file.write('test succeeded')

# Opening a file called test.log, writing the string 'test succeeded' to it, and then closing it.
with open('test.log', mode='w', encoding='utf-8') as a_file:
    print(a_file.read())
