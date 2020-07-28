from faker import Faker

class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        return f"Wybieram numer {self.phone_number} i dzwonie do {self.first_name} {self.last_name}"

class Businesscontact:
    def __init__(self, position, company, phone_number2):
        self.position = position
        self.company = company
        self.phone_number2 = phone_number2

    def contact(self):
        return f"Wybieram numer {self.phone_number2} i dzwonie do {self.first_name} {self.last_name}"


if __name__ == "__main__":
    faker = Faker("pl_PL")

def create_contacts(self, BaseContact, Businesscontact):
    for _ in range(7):
        create_contacts=create_contacts(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            position=faker.position(),
            company=company.faker()
            email=faker.email(),
        )
create_contacts()

    print(BaseContact)
    or
    print(Businesscontact)
    pass
    print(create_contacts.name_length)





