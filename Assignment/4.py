import math
import os

# Part 1: Calculate Storage
def calculate_storage(photos, avg_size):
    total_mb = photos * avg_size
    return total_mb / 1024


# Part 2: Calculate Memory Cards
def cards_required(storage, card_capacity=16):
    return math.ceil(storage / card_capacity)


# Part 3: Calculate Backup Storage
def backup_storage(storage, copies=2):
    return storage * copies


# Part 4: Calculate Total Storage
def total_storage(*sizes):
    return sum(sizes)


# Part 5: Save Session Data
def save_log(data):
    os.makedirs("photo_logs", exist_ok=True)

    with open("photo_logs/shoot_log.txt", "a") as file:
        file.write(data + "\n")


# Main Program
print("PHOTOGRAPHY STORAGE MANAGEMENT")

sessions = int(input("Enter number of sessions: "))

storage_list = []

for i in range(sessions):

    print("\nSession", i + 1)

    photos = int(input("Enter number of photos: "))
    avg_size = float(input("Enter average image size (MB): "))

    storage = calculate_storage(photos, avg_size)
    storage_list.append(storage)

    print("Session Storage:", round(storage, 2), "GB")

    save_log(
        f"Session {i+1}, Photos: {photos}, Storage: {storage:.2f} GB"
    )


# Calculate Final Results
grand_total = total_storage(*storage_list)

cards = cards_required(grand_total)

backup = backup_storage(grand_total)

print("\n----- FINAL STORAGE REPORT -----")

print("Total Sessions:", sessions)
print("Total Storage:", round(grand_total, 2), "GB")
print("16 GB Cards Required:", cards)
print("Backup Storage:", round(backup, 2), "GB")

print("\n----- LOG FILE INFORMATION -----")

with open("photo_logs/shoot_log.txt", "r") as file:
    records = file.readlines()

print("Stored Records:", len(records))
print("Log File Size:", os.path.getsize(
    "photo_logs/shoot_log.txt"
), "Bytes")

print("\nProgram Completed Successfully!")