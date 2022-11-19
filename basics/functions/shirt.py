# Задаем для функции тело, и потом вызываем ее
def make_shirt(size = "L", text = "I love Python"):
    print(f"My shirt have size - {size}, and text - {text}.")

make_shirt()
make_shirt('M', 'milk')