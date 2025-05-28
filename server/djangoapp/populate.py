from .models import CarMake, CarModel

def initiate():
    # Delete existing data to avoid duplicates if you run this multiple times.
    # This will delete all your CarMake and CarModel data each time it is run.
    CarModel.objects.all().delete()
    CarMake.objects.all().delete()

    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology", "car_id": 101},
        {"name":"Mercedes", "description":"Luxury and performance. German technology", "car_id": 102},
        {"name":"Audi", "description":"Progress through technology. German engineering", "car_id": 103},
        {"name":"Kia", "description":"Movement that inspires. Korean technology", "car_id": 104},
        {"name":"Toyota", "description":"Leading the way. Japanese technology", "car_id": 105},
        {"name":"Ford", "description":"Built Ford Tough. American innovation", "car_id": 106},
        {"name":"BMW", "description":"The Ultimate Driving Machine. German precision", "car_id": 107},
        {"name":"Tesla", "description":"Accelerating the world's transition to sustainable energy. American electric vehicles", "car_id": 108},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(name=data['name'], 
                                   description=data['description'], 
                                   car_id=data['car_id'])
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        # NISSAN (car_make_instances[0])
        {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 12345},
        {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 12345},
        {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 12345},
        {"name":"Titan", "type":"TRUCK", "year": 2024, "car_make":car_make_instances[0], "dealer_id": 12346},
        {"name":"Altima", "type":"Sedan", "year": 2024, "car_make":car_make_instances[0], "dealer_id": 12347},
        {"name":"GT-R", "type":"SPORTS CAR", "year": 2025, "car_make":car_make_instances[0], "dealer_id": 12348},

        # Mercedes (car_make_instances[1])
        {"name":"GLC", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 23456},
        {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 23456},
        {"name":"C-Class", "type":"Sedan", "year": 2024, "car_make":car_make_instances[1], "dealer_id": 23456},
        {"name":"E-Class Estate", "type":"WAGON", "year": 2024, "car_make":car_make_instances[1], "dealer_id": 23457},
        {"name":"AMG GT", "type":"SPORTS CAR", "year": 2025, "car_make":car_make_instances[1], "dealer_id": 23458},
        {"name":"EQE", "type":"ELECTRIC", "year": 2025, "car_make":car_make_instances[1], "dealer_id": 23459},

        # Audi (car_make_instances[2])
        {"name":"Q5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 34567},
        {"name":"A4", "type":"Sedan", "year": 2024, "car_make":car_make_instances[2], "dealer_id": 34567},
        {"name":"A5 Coupe", "type":"COUPE", "year": 2024, "car_make":car_make_instances[2], "dealer_id": 34568},
        {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 34568},
        {"name":"RS 6 Avant", "type":"WAGON", "year": 2025, "car_make":car_make_instances[2], "dealer_id": 34569},
        {"name":"e-tron GT", "type":"ELECTRIC", "year": 2025, "car_make":car_make_instances[2], "dealer_id": 34570},

        # Kia (car_make_instances[3])
        {"name":"Telluride", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 45678},
        {"name":"K5", "type":"Sedan", "year": 2024, "car_make":car_make_instances[3], "dealer_id": 45678},
        {"name":"Soul", "type":"HATCHBACK", "year": 2024, "car_make":car_make_instances[3], "dealer_id": 45679},
        {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 45680},
        {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 45680},
        {"name":"Carnival", "type":"MINIVAN", "year": 2025, "car_make":car_make_instances[3], "dealer_id": 45680},
        {"name":"EV6", "type":"ELECTRIC", "year": 2025, "car_make":car_make_instances[3], "dealer_id": 45681},

        # Toyota (car_make_instances[4])
        {"name":"RAV4", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 56789},
        {"name":"Corolla", "type":"Sedan", "year": 2024, "car_make":car_make_instances[4], "dealer_id": 56789},
        {"name":"Prius", "type":"HYBRID", "year": 2024, "car_make":car_make_instances[4], "dealer_id": 56790},
        {"name":"Tacoma", "type":"TRUCK", "year": 2025, "car_make":car_make_instances[4], "dealer_id": 56791},
        {"name":"Supra", "type":"SPORTS CAR", "year": 2025, "car_make":car_make_instances[4], "dealer_id": 56792},
        {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 56792},
        {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 56790},

        # Ford (car_make_instances[5])
        {"name":"F-150", "type":"TRUCK", "year": 2024, "car_make":car_make_instances[5], "dealer_id": 67890},
        {"name":"Explorer", "type":"SUV", "year": 2024, "car_make":car_make_instances[5], "dealer_id": 67890},
        {"name":"Mustang", "type":"SPORTS CAR", "year": 2025, "car_make":car_make_instances[5], "dealer_id": 67891},
        {"name":"Bronco", "type":"SUV", "year": 2025, "car_make":car_make_instances[5], "dealer_id": 67892},
        {"name":"Maverick", "type":"TRUCK", "year": 2026, "car_make":car_make_instances[5], "dealer_id": 67893},

        # BMW (car_make_instances[6])
        {"name":"X3", "type":"SUV", "year": 2024, "car_make":car_make_instances[6], "dealer_id": 78901},
        {"name":"3 Series", "type":"Sedan", "year": 2024, "car_make":car_make_instances[6], "dealer_id": 78901},
        {"name":"4 Series Coupe", "type":"COUPE", "year": 2025, "car_make":car_make_instances[6], "dealer_id": 78902},
        {"name":"iX", "type":"ELECTRIC", "year": 2025, "car_make":car_make_instances[6], "dealer_id": 78903},
        {"name":"Z4 Roadster", "type":"CONVERTIBLE", "year": 2026, "car_make":car_make_instances[6], "dealer_id": 78904},

        # Tesla (car_make_instances[7])
        {"name":"Model 3", "type":"ELECTRIC", "year": 2023, "car_make":car_make_instances[7], "dealer_id": 89012},
        {"name":"Model Y", "type":"ELECTRIC", "year": 2024, "car_make":car_make_instances[7], "dealer_id": 89012},
        {"name":"Cybertruck", "type":"TRUCK", "year": 2025, "car_make":car_make_instances[7], "dealer_id": 89013},
        {"name":"Model S", "type":"ELECTRIC", "year": 2025, "car_make":car_make_instances[7], "dealer_id": 89014},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            dealer_id=data['dealer_id']
        )
