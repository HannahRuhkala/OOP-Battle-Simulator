from goblin import Goblin


ARENA_NAME = "The Colusseum of Chaos"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Cornilius")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("Will he play the game of death to live or die to give another life.")


if __name__ == "__main__":
    main()
