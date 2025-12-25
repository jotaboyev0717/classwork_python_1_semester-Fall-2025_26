def parse_settings(config_lines):
    settings = {}

    for line in config_lines:
        try:
            # Split and validate structure
            parts = line.split(":")
            if len(parts) != 2:
                raise IndexError

            key, value_str = parts[0].strip(), parts[1].strip()

            # Convert to int (may raise ValueError)
            value = int(value_str)

            # Range check
            if not (0 <= value <= 100):
                raise ValueError("Out of range")

            # Valid → save
            settings[key] = value

        except IndexError:
            print(f"Format error in: {line}")

        except ValueError as e:
            print(f"Invalid value in: {line} ({e})")

    return settings
