f = open("robin.txt", "r")
data = f.read()

ignore = ('":;,.-+=/\|[]{}()*^&')

word_counts = {}
def word_count(s):
    for char in ignore:
        s = s.replace(char, "")
    s = s.lower()
    words = str.split(s)

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

word_count(data)

items = list(word_counts.items())
items.sort(key=lambda e: e[1], reverse=True)

for i in items:
    print(f'{i[0]}  {"".join(["#"] * i[1])}')


