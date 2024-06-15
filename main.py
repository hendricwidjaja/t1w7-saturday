from text_processing import count_words, unique_words, count_characters, count_unique_characters, reverse_string

# Test String
test_string = "Hello world hello"

# Using word_count module
print("Word Count:", count_words(test_string))
print("Unique words:", unique_words(test_string))

# Using char-count module
print("Character Count:", count_characters(test_string))
print("Unique Character Count:", count_unique_characters(test_string))

# Using reverse module
print("Reversed string:", reverse_string(test_string))
