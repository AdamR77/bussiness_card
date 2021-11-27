from faker import Faker
fake = Faker()


class BaseContact:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} {self.address} {self.phone} {self.email}'

    def contact(self):
        print(f'Wybieram numer prywatny {self.phone} i dzwonię do {self.name}')

    def len(self):
        return f'{len(self.name)}'

class BusinessContact(BaseContact):
    def __init__(self, company, job, business_phone, business_email ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.business_phone = business_phone
        self.business_email = business_email
    def __str__(self):
        return f'{self.name} {self.address}, {self.phone} {self.email} \ ' \
               f'{self.company} {self.job} {self.business_phone}'

    def contact(self):
        print(f'Wybieram numer służbowy {self.business_phone} i dzwonię do {self.name}')

    def lenght(self):
        return f'{len(self.name)} '

def create_contacts(_type, number):
    if _type == 'priv':
        for nr in range(number):
            prive = BaseContact(name = fake.name(), address =  fake.address(),
                    phone = fake.phone_number(), email = fake.email())
            prive.contact()

    elif _type == 'biz':
        for nr in range(number):
            biz = BusinessContact(company = fake.company(), job = fake.job(), business_phone = fake.phone_number(),
                  name = fake.name(), address = fake.address(), email = fake.email(), phone = fake.phone_number(),
                  business_email = fake.email())
            biz.contact()

#sprawdzenie
_type = 'biz'
number = 5
create_contacts(_type, number)























