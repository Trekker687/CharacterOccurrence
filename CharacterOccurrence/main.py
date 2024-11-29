string = input("Enter a word")
char = input("Enter a character from the word")

i = 0
count = 0

while i < (len(string)):
    if string[i] == char:
        count = count + 1
    i = i + 1

print("The total number of times", char, "has occurred in the word", string, ":",count)  
