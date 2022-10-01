from faker import Faker
import json
import csv

fake = Faker(locale = 'pt_BR')

for i in range(10):
    nome = (fake.name())
    endereço = (fake.address())
    email = (fake.email())
    telefone = (fake.phone_number())
    cpf = (fake.cpf())
    cnpj = (fake.cnpj())
    cep = (fake.postcode())
    cidade = (fake.city())
    estado = (fake.state())
    pais = (fake.country())
    data = (fake.date())
    hora = (fake.time())
    with open('fake_data.json', 'a', encoding='utf-8') as f:
        json.dump({
            'nome': nome,
            'endereço': endereço,
            'email': email,
            'telefone': telefone,
            'cpf': cpf,
            'cnpj': cnpj,
            'cep': cep,
            'cidade': cidade,
            'estado': estado,
            'pais': pais,
            'data': data,
            'hora': hora,
        }, f, ensure_ascii=False, indent=4)

    # Saving in csv file
    with open('fake_data.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['nome', 'endereço', 'email', 'telefone', 'cpf', 'cnpj', 'cep', 'cidade', 'estado', 'pais', 'data', 'hora'])
        writer.writerow([nome, endereço, email, telefone, cpf, cnpj, cep, cidade, estado, pais, data, hora])
