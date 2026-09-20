from cultivator import Cultivator
from subclass_1 import SwordCultivator

# ---- MAIN PROGRAM ----
def main():
    sect = [
        SwordCultivator("Lin Feng"),
    ]

    for c in sect:
        for _ in range(5):
            c.cultivate()
        c.breakthrough()
        c.use_technique()
        print()


if __name__ == "__main__":
    main()
