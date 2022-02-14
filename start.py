names = input('input names: ').split(", ")
title_names = []
not_title_names = []
for i in names:
    a = i.istitle()
    if a == True:
        title_names.append(i)
    else:
        not_title_names.append(i)
print(title_names)
print(not_title_names)
