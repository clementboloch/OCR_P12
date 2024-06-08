import factory
from CRM.models import Client, Contract, Event
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker()
User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.LazyAttribute(lambda _: fake.email()[:50])
    first_name = factory.Faker('first_name', locale='en_US')
    last_name = factory.Faker('last_name', locale='en_US')
    birthdate = factory.Faker('date_of_birth')

class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    name = factory.LazyAttribute(lambda _: fake.company()[:50])
    email = factory.LazyAttribute(lambda _: fake.email()[:50])
    phone = factory.LazyAttribute(lambda _: fake.phone_number()[:15])
    company = factory.LazyAttribute(lambda _: fake.company()[:50])
    commercial_contact = factory.SubFactory(UserFactory)

class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contract

    client = factory.SubFactory(ClientFactory)
    amount = factory.Faker('random_number')
    is_signed = factory.Faker('boolean')

class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    contract = factory.SubFactory(ContractFactory)
    start_date = factory.Faker('date')
    end_date = factory.Faker('date')
    location = factory.LazyAttribute(lambda _: fake.address()[:50])
    attendees = factory.Faker('random_int', min=1, max=500)
    support_contact = factory.SubFactory(UserFactory)
