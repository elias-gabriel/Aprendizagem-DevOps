import csv
import json
from faker import Faker

fake = Faker(locale='pt_BR')

# Open the CSV file in append mode
with open('fake_data.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # Only write the header row if the file is empty
    if f.tell() == 0:
        writer.writerow(['nome', 'endereço', 'email', 'telefone', 'cpf', 'cnpj', 'cep', 'cidade', 'estado', 'pais', 'data', 'hora'])

    # Open the JSON file in append mode
    with open('fake_data.json', 'a', encoding='utf-8') as j:
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

            # Write each row to the CSV file
            writer.writerow([nome, endereço, email, telefone, cpf, cnpj, cep, cidade, estado, pais, data, hora])

            # Write each set of data to the JSON file
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
            }, j, ensure_ascii=False, indent=4)

            # Add a newline character after each set of data
            j.write('\n')
