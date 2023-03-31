import json

input_data = {
    111111:('Alina',27),
    222222:('Dima',26),
    333333:('Ira',46),
    444444:('Kira',53),
    555555:('Anton',15),
    666666:('Oleg',33)
}

with open ('input_data.json', 'w') as file:
    json.dump(input_data, file)