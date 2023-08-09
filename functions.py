def sayName(name):
    while True:
        if not name:
            print('Dejaste el nombre vacio')
            name = input('Introduce nuevamente tu nombre:')
            continue
        capitalized_name = name[0].upper() + name[1:].lower()
        return f'Hola {capitalized_name}'
        break

# add unit testing for the result