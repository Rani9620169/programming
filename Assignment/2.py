# Milestone 2: Multiple Photography Sessions

shoot_types = {
    "Portrait": "PRT",
    "Event": "EVT",
    "Landscape": "LND",
    "Product": "PRD",
    "Sports": "SPT"
}

sessions = []

while True:

    shoot = input("\nEnter shoot type (or DONE): ").title()

    if shoot == "Done":
        break

    if shoot not in shoot_types:
        print("Invalid shoot type! Try again.")
        continue

    try:
        photos = int(input("Enter number of photos: "))
        avg_size = float(input("Enter average image size (MB): "))

        if photos <= 0 or avg_size <= 0:
            print("Photos and image size must be positive!")
            continue

    except ValueError:
        print("Invalid input! Enter numeric values.")
        continue

    storage = (photos * avg_size) / 1024

    if storage < 4:
        category = "Light"
    elif storage <= 8:
        category = "Moderate"
    else:
        category = "Heavy"

    sessions.append({
        "shoot": shoot,
        "photos": photos,
        "storage": storage,
        "category": category
    })

# Weekly Summary

print("\n----- WEEKLY SHOOT SUMMARY -----")

total_photos = 0
total_storage = 0
unique_types = set()

for s in sessions:
    total_photos += s["photos"]
    total_storage += s["storage"]
    unique_types.add(s["shoot"])

print("Total Sessions:", len(sessions))
print("Total Photos:", total_photos)
print("Total Storage:", round(total_storage, 2), "GB")
print("Unique Shoot Types:", unique_types)

print("\nSessions Sorted by Storage:")

sorted_sessions = sorted(
    sessions,
    key=lambda x: x["storage"],
    reverse=True
)

for s in sorted_sessions:
    print(
        s["shoot"],
        "-", s["photos"], "photos -",
        round(s["storage"], 2), "GB -",
        s["category"]
    )