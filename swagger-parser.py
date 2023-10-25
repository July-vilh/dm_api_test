import yaml

def load_swagger_spec(swagger_file):
    with open(swagger_file, 'r') as file:
        swagger_spec = yaml.safe_load(file)
    return swagger_spec

if __name__ == '__main__':
    swagger_file = 'USERS.yaml'  # Укажите путь к вашему файлу спецификации Swagger
    swagger_spec = load_swagger_spec(swagger_file)

print(swagger_spec)