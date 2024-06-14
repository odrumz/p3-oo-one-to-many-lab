class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if owner is not None:
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self.pets_list.append(pet)
            pet.owner = self
        else:
            raise Exception("Invalid pet")

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)