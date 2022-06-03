from faker import Faker
from datetime import date

# Gera os arquivos fakes
fake = Faker()


def create_data(x):
    # dictionary
    fake_data = {}
    for i in range(0, x):
        fake_data[i] = {}
        fake_data[i]["name"] = fake.name()
        fake_data[i]["first_name"] = fake.first_name()
        fake_data[i]["last_name"] = fake.last_name()
        fake_data[i]["city"] = fake.city()
        fake_data[i]["type"] = fake.word()
        fake_data[i]["job"] = fake.job()
        fake_data[i]["ip"] = fake.ipv4()
        fake_data[i]["Host_name"] = fake.hostname()
        fake_data[i]["Domain_name"] = fake.domain_name()
        fake_data[i]["Domain_word"] = fake.domain_word()
        fake_data[i]["TLD"] = fake.tld()
        fake_data[i]["first_access"] = fake.past_date()
        fake_data[i]["last_access"] = date.today()

    return fake_data
