def getfebrow(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    return getfebrow(num - 1) + getfebrow(num - 2)


num = int(input('input number = '))
print(getfebrow(num))
