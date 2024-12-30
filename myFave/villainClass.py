from characterClass import Character;

class Villain(Character):
    #Constructors
    def __init__(self, n, a, g, h, m, evilness, archenemy):
        super().__init__(n, a, g, h, m);  # Initialize inherited properties
        self.evilness = evilness;         # New property specific to Villain
        self.archenemy = archenemy;       # Another property specific to Villain

    def __str__(self):
        base_info = super().__str__();
        return (
            f"{base_info} They have an evilness level of {self.evilness}. "
            f"Their archenemy is {self.archenemy}."
        )
    
    #Setters
    def set_evilness(self, new_evilness):
        self.evilness = new_evilness;
    
    #Other Methods
    def increase_evilness(self, level):
        self.evilness += level;
        print(f"Evilness level increased to: {self.evilness}");