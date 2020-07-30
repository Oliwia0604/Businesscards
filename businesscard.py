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
        return len(self.first_name) + len(self.last_name)
    
    def __str__(self):
        return f"{self.__class__.__name__}"


class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone_number, email=None, position=None, company_name=None, company_number=None):
        super().__init__(first_name=first_name,
                        last_name=last_name,
                        phone_number=phone_number)
                        
        self.position = position
        self.company_name = company_name
        self.company_number = company_number

    def contact(self):
        print(f"Wybieram numer {self.company_number} i dzwonie do {self.first_name} {self.last_name}")

def create_contacts(card, quantity):
    faker = Faker("pl_PL")

    item = None

    for _ in range(quantity):
        if card is BusinessContact:
            item = BusinessContact(first_name=faker.first_name(),
                        last_name=faker.last_name(),
                        phone_number=faker.phone_number(),
                        email=faker.email(),
                        company_number=faker.phone_number())
            

        elif card is BaseContact:
            item = BaseContact(first_name=faker.first_name(),
                        last_name=faker.last_name(),
                        phone_number=faker.phone_number(),
                        email=faker.email())

        item.contact()
        print(item.label_length, item.__str__())


if __name__=="__main__":
    create_contacts(BusinessContact, 10)
    create_contacts(BaseContact, 10)
    
    




