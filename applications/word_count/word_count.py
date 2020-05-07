ignore = ('":;,.-+=/\|[]{}()*^&')
def word_count(s):
    word_counts = {}

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



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))