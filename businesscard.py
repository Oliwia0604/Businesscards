from faker import Faker


class Card:
    def __init__(self, first_name, last_name, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.email = email

    def contact(self):
        return f"Kontaktuje się z {self.first_name} {self.last_name} - {self.position} email: {self.email}"

    @property
    def name_length(self):
        return len(f"{self.first_name} {self.last_name}")


if __name__ == "__main__":
    faker = Faker("pl_PL")

    for _ in range(10):
        card = Card(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            position=faker.job(),
            email=faker.email()
        )
        print(card.contact())
        print(card.name_length)


#from faker import Faker


#class BaseContact:
 #   def __init__(self, first_name, last_name, phone_number, email):
  #      self.first_name = first_name
   #     self.last_name = last_name
    #    self.phone_number = phone_number
     #   self.email = email
      #  print(BaseContact)
    


#class Businesscontact:
 #   def __init__(self, position, company, phone_number2):
  #      self.position = position
   #     self.company = company
    #    self.phone_number2 = phone_number2
    #print(Businesscontact)

    #def contact(self):
     #   return f"Kontaktuje się z {self.first_name} {self.last_name} - {self.position} email: {self.email}"

    #@property
    #def name_length(self):
     #   return len(f"{self.first_name} {self.last_name}")

#if __name__ == "__main__":
#if __name__ == "__main__":
 #   faker = Faker("pl_PL")

  #  for _ in range(10):
   #     BaseContact = BaseContact (
    #        first_name=faker.first_name(),
     #       last_name=faker.last_name(),
      #      phone_number=faker.phone_number(),
       #     email=faker.email()
        #)
        #print(BaseContact)
        #print(Businesscontact)
        #print(BaseContact.name_length)






#from faker import Faker
#fake = Faker()


#class Contact:
 #   def __init__(self, name, address, email):
  #      self.name = name
   #     self.address = address
    #    self.email = email
    #def __str__(self):pyth
     #   return '{} {} {}'.format(self.name, self.address, self.email)

#all_contacts=[]
#for person in range(5):
 #   person= Contact(name=fake.name(), address=fake.address(), email=fake.email())
  #  all_contacts.append(person)

#print(all_contacts)