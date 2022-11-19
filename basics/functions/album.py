# Создаем функцию с телом для создания словаря с необходимыми парами
# Один элемент словаря является заданным по умолчанию None
def make_album(name_musician, name_album, number_of_tracks=""):
    album = {name_musician.title(): name_album.title(), }
# Здесь указываем, что если будем задавать третье значение, то оно будет
# выведено на экран, а в ином случае нет
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
# Далее сформированный словарь вернется в функцию
    return album

# Вызываем функцию, и задаем элементы для преобразования в ней
album1 = make_album('monetochka', 'decorative and applied art', 3)
# Выводим на экран результат
print(album1)

album2 = make_album('letov', 'all go about plan')
print(album2)

album3 = make_album('zemfira', 'daisies')
print(album3)
