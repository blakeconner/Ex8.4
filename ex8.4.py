words = list()

inp = input("Enter a file name:")
if imp == ("romeo.txt"):
    fhand = open("romeo.txt")
    for line in fhand:
        line = line.rstrip()
        for word in line.split(" "):
            if word not in words:
                words.append(word)

print(sorted(words))
