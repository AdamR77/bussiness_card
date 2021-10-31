from faker import Faker
fake = Faker()

name = fake.name()
address= fake.address()
phone = fake.phone_number()
company = fake.company()
position = fake.job()
email = fake.email()

class BussinessCard:
    def __init__ (self, name, address, phone, company, job, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.company = company
        self.job = job
        self.email = email
    def __str__ (self):
        return f'{self.name} {self.address}  {self.company} {self.phone} {self.job}  {self.email}'

for x in range(6):
    name = fake.name()
    address = fake.address()
    company = fake.company()
    phone = fake.phone_number()
    job = fake.job()
    email = fake.email()
    person = BussinessCard(name, address, phone, company, job, email)
    print(person)


def __str__ (self):
    return f' kontaktuję się z {name} {company} {job} {email}'
contact = BussinessCard(name = name, address=address, phone = phone, email = email, company = company, job = job)

print(contact)
print(BussinessCard)












 #   def __str__(self):
 #       name = fake.name()
 #       adres = fake.address()
 #       email = fake.email()
 #       return f'{self.name} {self.adres} {self.email}'
# example_person = Bussiness_card(name ='Jan Kowalski', adres = 'ul. Sezamkowa 10/36',
# company ='PKN Orlen S.A.', phone = '+48 502 228 366', email = 'jkowalski@onet.pl')




















