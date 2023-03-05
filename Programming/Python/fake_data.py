import csv
import json
from faker import Faker

fake = Faker(locale='pt_BR')

# Prompt the user for the number of records to generate
while True:
    try:
        num_records = int(input("How many records do you want to generate? "))
        if num_records <= 0:
            raise ValueError()
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Prompt the user to choose the output format
while True:
    choice = input("Do you want to save the data in CSV or JSON format? ").lower()
    if choice == "csv":
        # Generate the data
        data = []
        for i in range(num_records):
            nome = fake.name()
            endereço = fake.address()
            email = fake.email()
            telefone = fake.phone_number()
            cpf = fake.cpf()
            cnpj = fake.cnpj()
            cep = fake.postcode()
            cidade = fake.city()
            estado = fake.state()
            pais = fake.country()
            data.append({
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
                'data': fake.date(),
                'hora': fake.time(),
            })

        # Write the data to the CSV file using a context manager
        with open('fake_data.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            if f.tell() == 0:
                writer.writeheader()
            writer.writerows(data)
        break
    elif choice == "json":
        # Generate the data
        data = []
        for i in range(num_records):
            nome = fake.name()
            endereço = fake.address()
            email = fake.email()
            telefone = fake.phone_number()
            cpf = fake.cpf()
            cnpj = fake.cnpj()
            cep = fake.postcode()
            cidade = fake.city()
            estado = fake.state()
            pais = fake.country()
            data.append({
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
                'data': fake.date(),
                'hora': fake.time(),
            })

        # Write the data to the JSON file using a context manager
        with open('fake_data.json', 'a', encoding='utf-8') as f:
            for item in data:
                json.dump(item, f, ensure_ascii=False, indent=4)
                f.write('\n')
        break
    else:
        print("Invalid choice. Please enter 'csv' or 'json'.")

print("Data saved successfully!")
