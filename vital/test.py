def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

A = str(input('Input the string:\n'))
print(any_lowercase5(A))