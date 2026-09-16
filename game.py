from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Colusseum of Cantations"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero .is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")



def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Cornilius")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("Will he play the game of death to live or die to give another life.")

    secondGoblin = Goblin("Nikki")
    
    print(f"{secondGoblin.name} enters the arena with {secondGoblin.health} health.")
    print("Will he play the game of death to live or die to give another life.")

    jan = Hero("Jana", "Beat them Goblins!")
    print(f"{jan.name} enters the arena.")

    jan.battle_cry()
    battle(jan, goblin)

if __name__ == "__main__":
    main()
