import phonenumbers
from phonenumbers import carrier, geocoder, timezone

Numero_celular = input('Digite o número de celular: ')
Numero_celular = phonenumbers.parse(Numero_celular)

print('DDDPaís:', timezone.time_zones_for_number(Numero_celular))
print('Cidade:', geocoder.description_for_number(Numero_celular, 'pt'))
print('Validação de Número:', phonenumbers.is_valid_number(Numero_celular))
print('Possibilidade de Número:', phonenumbers.is_possible_number(Numero_celular))