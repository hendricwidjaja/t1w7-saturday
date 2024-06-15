def count_words(text):
    words = text.split()
    return len(words)

def unique_words(text):
    words = text.lower().split()
    return set(words)


# print(count_words("Good Morning everyone, welcome to the session"))
# print(unique_words("Good Morning everyone, welcome to the session. This session is good"))