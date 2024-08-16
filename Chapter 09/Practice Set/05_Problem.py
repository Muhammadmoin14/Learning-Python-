# Repeat program 4 for a list of such words to be censored

list = ["donkey","bad"]
with open("05_file.txt") as f:
    content = f.read()

for word in list:
    content = content.lower()
    content = content.replace(word, "#####")

with open("05_file.txt","w") as f:

    f.write(content)
