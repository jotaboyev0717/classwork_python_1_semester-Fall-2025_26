def summarize_sensor_data(readings):
    if readings == []:
        return []
    
    result = []
    for sensor, temp in (readings):
        found = False
        
        for i in range(len(result)):
            if result[i][0] == sensor:
                found = True
                if temp > result[i][1]:
                    result[i] = (sensor, temp)
                break
        if not found:
            result.append((sensor, temp))
    result.sort()
    return result

readings = [
    ('SensorB', 25.4),
    ('SensorA', 22.1),
    ('SensorB', 26.1),
    ('SensorC', 30.5),
    ('SensorA', 21.9),
    ('SensorB', 25.9)
]

print(summarize_sensor_data(readings))

readings_empty = []
print(summarize_sensor_data(readings_empty))
