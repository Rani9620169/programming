import os

# Create log directory
os.makedirs("photo_logs", exist_ok=True)

log_file = "photo_logs/shoot_log.txt"


def save_record(name, shoot, photos, size, capacity, duration):
    with open(log_file, "a") as file:
        file.write(
            f"{name}|{shoot}|{photos}|{size}|{capacity}|{duration}\n"
        )


def display_records():
    print("\n--- SAVED SHOOT RECORDS ---")

    try:
        with open(log_file, "r") as file:
            count = 0

            for line in file:
                try:
                    data = line.strip().split("|")

                    if len(data) != 6:
                        print("Skipping malformed record")
                        continue

                    name, shoot, photos, size, capacity, duration = data

                    print("Name:", name)
                    print("Shoot:", shoot)
                    print("Photos:", photos)
                    print("Image Size:", size, "MB")
                    print("Card Capacity:", capacity, "GB")
                    print("Duration:", duration, "minutes")
                    print("----------------------")

                    count += 1

                except ValueError:
                    print("Skipping invalid record")

            print("Total Valid Records:", count)

        print("Log File Size:", os.path.getsize(log_file), "bytes")

    except FileNotFoundError:
        print("Log file not found. No records available.")


def main():
    print("DIGITAL PHOTO SHOOT MANAGER")

    while True:
        try:
            name = input("\nEnter photographer name: ")

            if name.upper() == "DONE":
                break

            shoot = input("Enter shoot type: ")
            photos = int(input("Enter number of photos: "))
            size = float(input("Enter average image size (MB): "))
            capacity = float(input("Enter card capacity (GB): "))
            duration = int(input("Enter duration (minutes): "))

            if photos <= 0 or size <= 0 or capacity <= 0 or duration <= 0:
                raise ValueError("All numeric values must be positive.")

            save_record(name, shoot, photos, size, capacity, duration)

            print("Record saved successfully!")

        except ValueError as e:
            print("Invalid input:", e)
            print("Please enter valid values.")

    display_records()


main()