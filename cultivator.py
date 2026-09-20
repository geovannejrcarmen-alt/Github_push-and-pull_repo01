# ---- SUPERCLASS (parent) ----
class Cultivator:
    def __init__(self, name):
        self.name = name
        self.realm = "Qi Condensation"
        self.spiritual_power = 10

    # Shared by every cultivator, regardless of path
    def cultivate(self):
        self.spiritual_power += 10
        print(f"{self.name} meditates and absorbs qi. Spiritual power: {self.spiritual_power}")

    def breakthrough(self):
        if self.spiritual_power >= 50:
            self.realm = "Foundation Establishment"
            print(f"{self.name} breaks through to {self.realm}!")
        else:
            print(f"{self.name} isn't ready to break through yet.")

    # Default technique - subclasses override this with their own style
    def use_technique(self):
        print(f"{self.name} punches forward with raw qi.")