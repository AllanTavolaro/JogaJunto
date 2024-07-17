from faker import Faker

faker = Faker('pt_BR')

persona = {

    "nome": faker.name(),
    "cidade": faker.address(),
    "Idade" : faker.random_int(18, 100),

}

print(persona)