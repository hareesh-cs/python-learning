import string

alphabets = set(string.ascii_lowercase)


def contains_all_alphabets(input_string: str) -> bool:
    return set(input_string.lower()) >= alphabets


str1 = input("Enter a string: ")
print(contains_all_alphabets(str1))
