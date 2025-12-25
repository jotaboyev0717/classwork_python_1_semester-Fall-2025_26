def parse_settings(config_lines):
    settings = {}
    for line in config_lines:
        try:
            
            word = line.split(":")
            if len(word) != 2:
                raise IndexError
            key = word[0]
            value = word[1]
            value = int(value)

            if value < 0 or value > 100:
                raise ValueError(f"Age {value} is invalid. Out of range.")
            settings[key] = value
        except IndexError:
            print(f"Format error in: {line}")

        except ValueError as e:
            print(f"Invalid value in: {line} ({e})")
    return settings

configs = [
    "volume:80",          # Valid
    "brightness:120",     # Invalid Range
    "difficulty:hard",    # Invalid Type
    "mute",               # Invalid Format (no colon)
    "contrast:50"         # Valid
]
settings = parse_settings(configs)
print(f"Loaded Settings: {settings}")