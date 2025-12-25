log_data = """[INFO] System started successfully
[WARNING] Memory usage high
[ERROR] Database connection failed
[INFO] User logged in
[ERROR] Payment gateway timeout
[INFO] Scheduled backup complete
[ERROR] Disk space critical"""

with open("server_log.txt", "w") as f:
    f.write(log_data)

with open("server_log.txt", "r") as f:
    lines = f.readlines()

count = 0
with open("urgent_alerts.txt", "w") as f:
    for line in lines:
        if "ERROR" in line:
            f.write(line)
            count += 1

print(f"Scan complete. Found {count} errors.")
print("Please check urgent_alerts.txt.")
