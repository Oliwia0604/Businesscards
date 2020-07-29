from faker import Faker

class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonie do {self.first_name} {self.last_name}")


    @property
    def label_length(self):
        return f"{self._class_._name_}"


class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name,phone, email, position, company, company_number):
        super()._init_(first_name=first_name,
                       last_name=last_name,
                       phone=phone,
                       email=email)
        self.position = position
        self.company = company
        self.company_number = company_number

    def contact(self):
        print(f"Wybieram numer {self.company_number} i dzwonie do {self.first_name} {self.last_name}")

def create_contacts(card, quantity):
    faker = Faker("pl_PL")

    item = None

    for _ in range(quantity):
        if card is BusinessContact:
            item = card(first_name=faker.first_name(),
                        last_name=faker.last_name(),
                        phone=faker.phone_number(),
                        email=faker.email(),
                        company_phone=faker.company_phone())

        elif card is BaseContact:
            item = card(first_name=faker.first_name(),
                        last_name=faker.last_name(),
                        phone=faker.phone_number(),
                        email=faker.email())

        item.contact()
        print(item.label_lenght, item._str_())


if name =="_main_":
    create_contacts(BusinessContact, 10)
    create_contacts(BaseContact, 10)
    
    




