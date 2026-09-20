from cultivator import Cultivator

class SwordCultivator(Cultivator):
    def __init__(self, name):
        super().__init__(name)

    def use_technique(self):
        print(f"{self.name} unleashes the Nine Heavens Sword Intent!")