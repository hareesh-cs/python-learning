import re


def match(text):

    pattern = "[A-Z].*[.]"

    if re.search(pattern, text):
        return 'Yes'
    else:
        return 'No'


text =input("Enter a string: ")
print(match(text))