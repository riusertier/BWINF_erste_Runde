lst = ['u', 'ea', 'a', 'o', 'e']

index = 0
while True:
    try:  
        if len(lst[index]) >= 2:
            laenge = len(lst[index])
            for num in range(1, laenge):
                del lst[index + num]
        index += 1
    except IndexError:
        break

print(lst)
