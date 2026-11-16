# Estimate Storage for One Photo Shoot

name = input("Enter photographer name: ")
shoot_type = input("Enter shoot type: ")
photos = int(input("Enter number of photos: "))
avg_size = float(input("Enter average image size (MB): "))
card_capacity = float(input("Enter memory card capacity (GB): "))
duration = int(input("Enter session duration (minutes): "))

# Calculate storage
total_mb = photos * avg_size
total_gb = total_mb / 1024

# Remaining memory card space
remaining = card_capacity - total_gb

# Convert minutes into hours and minutes
hours = duration // 60
minutes = duration % 60

# Create session code
session_code = name[:3].upper() + shoot_type[:3].upper()

# Display output
print("\n----- PHOTO SHOOT STORAGE REPORT -----")
print("Photographer Name:", name)
print("Shoot Type:", shoot_type)
print("Total Photos:", photos)
print("Total Storage (MB):", total_mb)
print("Total Storage (GB):", round(total_gb, 2))
print("Remaining Card Space (GB):", round(remaining, 2))
print("Duration:", hours, "Hours", minutes, "Minutes")
print("Session Code:", session_code)