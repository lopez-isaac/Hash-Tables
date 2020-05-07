def no_dups(s):
    # Implement me.
    word_counts = {}
    words = str.split(s)

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    key = list(word_counts.keys())
    ans = " ".join(str(x) for x in key)
    return ans




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))