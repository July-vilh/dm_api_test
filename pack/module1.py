name = 'Artur'

def create_message(name):
    message = f'fuck you, {name}!'
    return message


def printing_message(name):
    message=create_message(name)
    print(message)

if __name__ == '__main__':

    match name:
        case 'Ivan':
            printing_message(name)
        case 'Artur':
            printing_message(name)
        case 'Nikita':
            printing_message(name)
        case _:
            print('Fuck u')
