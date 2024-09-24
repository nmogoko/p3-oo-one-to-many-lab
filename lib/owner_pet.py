class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type.lower() not in self.PET_TYPES:
            raise Exception(
                f"Invalid pet type '{pet_type}'. Valid types are: {', '.join(self.PET_TYPES)}.")

        # Validate name type
        if not isinstance(name, str):
            raise Exception("Pet name must be a string.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string.")

        self.name = name
        self.owned_pets = []  # List to store pets owned by this owner
        self.name = name
        self.owned_pets = []  # List to store pets owned by this owner

    def pets(self):
        # Return a list of pets owned by this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Check if the pet is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("The provided pet is not of type Pet.")

        # Add the owner to the pet
        pet.owner = self
        # Also add the pet to the owner's list of owned pets
        self.owned_pets.append(pet)

  
    def get_sorted_pets(self):
        # Return a sorted list of pets by their names
        return sorted(self.owned_pets, key=lambda pet: pet.name)
