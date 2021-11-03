from faker import Faker
fake = Faker()


class BaseContact:
    def __init__ (self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        
class BusinessContact(BaseContact):
    def __init__(self, job, company, business_phone, business_email, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.job = job
        self.company = company
        self.business_phone = business_phone
        self.business_email = business_email 
       
def create_contact():
    base_contact = BaseContact(name = fake.name(), address = fake.address(), phone = fake.phone_number(), email = fake.email())
    business_contact = BusinessContact(name = base_contact.name, phone = base_contact.phone, email = base_contact.email, job = fake.job(),
    company = fake.company(), business_phone = fake.phone_number(), address = base_contact.address, business_email = fake.email())    
    print(f'wybieram numer prywatny: {base_contact.phone} i kontaktuję się z {base_contact.name} ')
    print(f'wybieram numer służbowy: {business_contact.business_phone} i kontaktuję się {business_contact.name} ')
    print('długość pola: imię + nazwisko', len(base_contact.name))
create_contact()




















 #   def __str__(self):
 #       name = fake.name()
 #       adres = fake.address()
 #       email = fake.email()
 #       return f'{self.name} {self.adres} {self.email}'
# example_person = Bussiness_card(name ='Jan Kowalski', adres = 'ul. Sezamkowa 10/36',
# company ='PKN Orlen S.A.', phone = '+48 502 228 366', email = 'jkowalski@onet.pl')




















