def pol(text_1):
    if len(text_1) == 1:
        return True
    if text_1[0] != text_1[-1]:
        return False
    return pol(text_1[1:-1])


text_1 = input('input text...')
print(pol(text_1))
