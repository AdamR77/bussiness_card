from faker import Faker
fake = Faker()

name = fake.name()
address= fake.address()
company = fake.company()
phone = fake.phone_number()
email = fake.email()

class BussinessCard:
    def __init__ (self, name, address, phone, company, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.company = company
        self.email = email
    def __str__ (self):
        return f'{self.name} {self.address}  {self.company} {self.phone}  {self.email}'

for x in range(6):
    name = fake.name()
    address = fake.address()
    company = fake.company()
    phone = fake.phone_number()
    email = fake.email()
    person = BussinessCard(name, address, phone, company, email)
    print(person)







 #   def __str__(self):
 #       name = fake.name()
 #       adres = fake.address()
 #       email = fake.email()
 #       return f'{self.name} {self.adres} {self.email}'
# example_person = Bussiness_card(name ='Jan Kowalski', adres = 'ul. Sezamkowa 10/36',
# company ='PKN Orlen S.A.', phone = '+48 502 228 366', email = 'jkowalski@onet.pl')




















