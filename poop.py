#   Python Object-Oriented Programming

class client:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = name.lower() + '.' + surname.lower() + '@company.com'


client_1 = client('Martin', 'Klockner', 21)
client_2 = client('Name', 'Surname', 00)

print(client_1.name, client_1.surname)
print(client_1.email)
