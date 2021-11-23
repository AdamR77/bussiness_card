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
    base_contact = BaseContact(name = fake.name(), address = fake.address(), 
    phone = fake.phone_number(), email = fake.email())       
    business_contact = BusinessContact(name = base_contact.name, address = fake.address(),
    email = fake.email(), job = fake.job(), company = fake.company(),phone = base_contact.phone,
     business_phone = fake.phone_number(), business_email = fake.email())  
    name = base_contact.name
    priv_phone = base_contact.phone
    biz_phone = business_contact.phone
    lenght = len(name)  
    return name, priv_phone, biz_phone, lenght


def create_card( _type, number):
    if _type == 'priv':
        for x in range(number):
            data = create_contact()
            name = data[0]
            priv_phone = data[1]
            biz_phone = data[2]
            lenght = data[3] 
            print(f'wybieram numer prywatny: {priv_phone} i kontaktuję się z {name}, LenghtName = {lenght}')

    if _type == 'biz':
        for x in range(number):
            data = create_contact()
            name = data[0]
            priv_phone = data[1]
            biz_phone = data[2]
            lenght = data[3]
            print(f'wybieram numer służbowy: {biz_phone} i kontaktuję się {name}, LeghtName = {lenght}')

while True:
    _type = input('Podaj typ kontaktów do wygenerowania prywatny/biznesowy [priv]/[biz]: ')
    if _type in ['priv', 'biz']:
        break

while True:
    try:
        number = int(input('Podaj ile mam stworzyć kontaktów z danymi? '))    
    except:
        print('ilość wizytówek musi liczbą całkowitą')
    else:
        break



create_card(_type, number)

#contacts = create_contacts(_type, number)
#print(contacts)






















 #   def __str__(self):
 #       name = fake.name()
 #       adres = fake.address()
 #       email = fake.email()
 #       return f'{self.name} {self.adres} {self.email}'
# example_person = Bussiness_card(name ='Jan Kowalski', adres = 'ul. Sezamkowa 10/36',
# company ='PKN Orlen S.A.', phone = '+48 502 228 366', email = 'jkowalski@onet.pl')




















