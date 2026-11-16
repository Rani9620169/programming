# Milestone 3: OOP using Classes and Objects

class MemoryCard:

    def __init__(self, card_id, capacity_gb):
        self.card_id = card_id
        self.capacity_gb = capacity_gb
        self.used_gb = 0

    def available_space(self):
        return self.capacity_gb - self.used_gb

    def can_store(self, required_gb):
        return required_gb <= self.available_space()

    def store(self, required_gb):
        if self.can_store(required_gb):
            self.used_gb += required_gb
            return True
        return False


class PhotoSession:

    def __init__(self, session_id, photographer_name,
                 shoot_type, photo_count, avg_size_mb,
                 card):

        self.session_id = session_id
        self.photographer_name = photographer_name
        self.shoot_type = shoot_type
        self.photo_count = photo_count
        self.avg_size_mb = avg_size_mb
        self.card = card

    def storage_required(self):
        return (self.photo_count * self.avg_size_mb) / 1024

    def fits_on_assigned_card(self):
        return self.card.can_store(self.storage_required())

    def session_summary(self):

        return (
            "\nSession ID: " + str(self.session_id) +
            "\nPhotographer: " + self.photographer_name +
            "\nShoot Type: " + self.shoot_type +
            "\nPhotos: " + str(self.photo_count) +
            "\nStorage: " + str(round(self.storage_required(), 2)) +
            " GB" +
            "\nMemory Card: " + self.card.card_id +
            "\nFits on Card: " + str(self.fits_on_assigned_card())
        )

    def __str__(self):
        return self.session_summary()


# Create MemoryCard objects

card1 = MemoryCard("CARD-1", 16)
card2 = MemoryCard("CARD-2", 32)


# Create PhotoSession objects

session1 = PhotoSession(
    1, "Aditi", "Portrait", 320, 18.5, card1
)

session2 = PhotoSession(
    2, "Rani", "Event", 100, 20, card2
)


# Store photos on memory cards

card1.store(session1.storage_required())
card2.store(session2.storage_required())


# Display session details

print("----- PHOTOGRAPHY SESSION DETAILS -----")

print(session1)
print("\nAvailable Card Space:", round(card1.available_space(), 2), "GB")

print("\n--------------------------------")

print(session2)
print("\nAvailable Card Space:", round(card2.available_space(), 2), "GB")