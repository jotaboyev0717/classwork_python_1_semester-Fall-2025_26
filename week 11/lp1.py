# def clean_sensor_data(raw_readings):
#     a = []
#     for reading in raw_readings:
#         try:
#             value = float(reading)
#             if type(reading) != int:
#                 raise ValueError
#                 print("Invalid value")
                
#         except ValueError:
#             -50.0 < reading < 60 
#             if -50.0 > reading or reading > 60:
#                 raise ValueError
#                 print("Out of range")
#         a.append(reading)
#     return a
# data = ["22.5", "error", "105.0", "-10.0","N/A", "40.5"]
# print(clean_sensor_data(data))

def clean_sensor_data(raw_readings):
    cleaned = []

    for reading in raw_readings:
        try:
            value = float(reading)

            if not (-50.0 <= value <= 60.0):
                continue

            cleaned.append(value)

        except ValueError:
            continue

    return cleaned


data = ["22.5", "error", "105.0", "-10.0", "N/A", "40.5"]
print(clean_sensor_data(data))
