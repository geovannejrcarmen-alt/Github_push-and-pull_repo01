from cultivator import Cultivator

# ---- SUBCLASS 2 ----
class AlchemistCultivator(Cultivator):
    def __init__(self, name):
        super().__init__(name)

    def use_technique(self):
        print(f"{self.name} hurls an explosive Golden Core Pill at the enemy!")
