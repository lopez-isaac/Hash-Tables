f = open("robin.txt", "r")

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

    return word_counts