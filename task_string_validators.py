# """
# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False. """


def any_alnum(s):
    for c in s:
        if c.isalnum():
            return True
    else:
        return False


def any_alpha(s):
    for c in s:
        if c.isalpha():
            return True
    else:
        return False


def any_digit(s):
    for c in s:
        if c.isdigit():
            return True
    else:
        return False


def any_lower(s):
    for c in s:
        if c.islower():
            return True
    else:
        return False


def any_upper(s):
    for c in s:
        if c.isupper():
            return True
    else:
        return False


s = input()
print(any_alnum(s))
print(any_alpha(s))
print(any_digit(s))
print(any_lower(s))
print(any_upper(s))
