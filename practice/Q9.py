
string = str(input("Enter a string:\n"))
stringlist = []
for i in range(len(string)):
    stringlist.append(string[i])
counter = (len(string) - 1)
reverse = ""
while counter >= 0:
    letter = (stringlist[counter])
    reverse += letter
    counter -= 1
print(reverse)
reverse_skipped = ""
for i in range(0, (len(reverse)), 2):
    letter = reverse[i]
    reverse_skipped += letter
print(reverse_skipped)

