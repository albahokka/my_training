# Создаем три списка для дальнейшего их использования в виде значений
# в словаре
favorite_places_K = ['restorant', 'street', 'kaffe']
favorite_places_M = ['house', 'bus', 'store']
favorite_places_S = ['theatre', 'cinema', 'museum']

favorite_places = {'katya':favorite_places_K,
                   'Misha':favorite_places_M,
                   'Sasha':favorite_places_S,
                   }

# Производим проверку с условиями с дальнейшим выводом на экран
for name, favorite_place in favorite_places.items():
    if name == 'katya':
        print(f'\n{name.title()} tell me, that her love place its')
        for place in favorite_place:
            print(place.title())
    elif name == 'Misha':
        print(f'\n{name.title()} tell me, that his love place its')
        for place in favorite_place:
            print(place.title())
    else:
        print(f'\n{name.title()} tell me, that his love place its')
        for place in favorite_place:
            print(place.title())