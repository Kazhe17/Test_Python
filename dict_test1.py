# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Учтите, что бывают ситуации когда город с таким называнием
# бывает в разных странах (Брест есть в Беларуси и Франции).

dct_conty1 = dict.fromkeys(input('4 cities for country').split(), input('country'))
dct_conty2 = dict.fromkeys(input('3 cities for country').split(), input('country'))
list_ = list(dct_conty2.keys()) + list(dct_conty1.keys())
for i in list_:
    if i in dct_conty2:
        print(dct_conty2[i])
    elif i in dct_conty1:
        print(dct_conty1[i])
    else:
        print('not found')
