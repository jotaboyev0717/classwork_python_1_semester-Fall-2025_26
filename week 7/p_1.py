def find_flights_from_city(flight_data,origin,min_passengers):
    result = []
    for flight in flight_data:
        flight_number, origin_city, destination_city, passenger_count=flight
        if origin_city == origin and passenger_count >= min_passengers:
            result.append(flight_number)
    return result

flights = [
    ('AA101', 'New York', 'Los Angeles', 250),
    ('UA202', 'Chicago', 'New York', 180),
    ('DL303', 'New York', 'Miami', 160),
    ('AA404', 'Dallas', 'Los Angeles', 220),
    ('UA505', 'New York', 'Chicago', 175),
    ('DL606', 'Miami', 'New York', 150)
]

print(find_flights_from_city(flights, 'New York', 200))
# ['AA101']

print(find_flights_from_city(flights, 'New York', 150))
# ['AA101', 'DL303', 'UA505']

print(find_flights_from_city(flights, 'Chicago', 200))
# []