name = 'Artur'

# if name == 'Ivan':
#     print('Hello')
# else:
#     if name == 'Artur':
#         print('Hello')
#     else:
#         if name == 'Nikita':
#             print('Hello')
#         else:
#             print('Fuck u')

# if name == 'Ivan':
#     print('Hello')
# elif name == 'Artur':
#     print('Hello')
# elif name == 'Nikita':
#     print('Hello')
# else:
#     print('Fuck u')

def create_message(name):
    message = f'Hello, {name}!'
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




