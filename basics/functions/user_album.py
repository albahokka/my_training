# Создаем функцию с ее телом для формирования словаря с возвращением
# переменной в функцию
def make_album(name_musician, name_album, number_of_tracks=""):
    album = {name_musician.title(): name_album.title(), }
    return album

# Создаем цикл while, в котором вызываем нашу функцию с выводом на экран инфы
# в цикле предусмотрен признак завершения символом q
while True:
    print("\nPlease tell me about music album and name musician:")
    print("(enter 'q' at any time to quit)")

    name_m = input('Name: ')
    if name_m == 'q':
        break

    name_a = input('Album: ')
    if name_a == 'q':
        break

    user_album = make_album(name_m, name_a)
    print(f"Your lovely music is {user_album}?")