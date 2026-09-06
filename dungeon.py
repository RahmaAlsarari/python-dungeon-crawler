import random

class Player:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.hp = 100
        self.gold = 0

    def move(self, direction, grid_size):
        if direction == "w" and self.y > 0:
            self.y -= 1
        elif direction == "s" and self.y < grid_size - 1:
            self.y += 1
        elif direction == "a" and self.x > 0:
            self.x -= 1
        elif direction == "d" and self.x < grid_size - 1:
            self.x += 1
        else:
            print(">>> You hit a wall!")


class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack


def render_grid(player, exit_pos, grid_size):
    print("\n" + "=" * 25)
    print(f" Player: {player.name} | HP: {player.hp} | Gold: {player.gold}")
    print("=" * 25)
    for row in range(grid_size):
        line = ""
        for col in range(grid_size):
            if player.x == col and player.y == row:
                line += "[P] "
            elif exit_pos[0] == col and exit_pos[1] == row:
                line += "[E] "
            else:
                line += "[.] "
        print(line)


def trigger_encounter(player):
    monsters = [Monster("Goblin", 30, 10), Monster("Skeleton", 45, 15), Monster("Orc", 60, 20)]
    monster = random.choice(monsters)
    
    print(f"\n⚠️ ENCOUNTER! A wild {monster.name} appears! (HP: {monster.hp})")

    while monster.hp > 0 and player.hp > 0:
        action = input("(A)ttack or (R)un? ").lower()
        if action == "a":
            player_dmg = random.randint(15, 30)
            monster.hp -= player_dmg
            print(f"You struck the {monster.name} for {player_dmg} damage!")

            if monster.hp > 0:
                monster_dmg = random.randint(5, monster.attack)
                player.hp -= monster_dmg
                print(f"The {monster.name} hit you for {monster_dmg} damage!")
            else:
                earned_gold = random.randint(10, 30)
                player.gold += earned_gold
                print(f"🎉 You defeated the {monster.name}! Found {earned_gold} gold.")
        elif action == "r":
            print("You fled from combat!")
            break
        else:
            print("Invalid command!")


def main():
    grid_size = 5
    player = Player("Hero")
    exit_pos = (4, 4)

    print("Welcome to the Dungeon Crawler Engine!")
    print("Legend: [P] = Player, [E] = Exit, [.] = Empty Room\n")

    while player.hp > 0:
        render_grid(player, exit_pos, grid_size)

        if (player.x, player.y) == exit_pos:
            print("\n🏆 CONGRATULATIONS! You reached the exit and escaped the dungeon!")
            print(f"Final Gold: {player.gold}")
            break

        move_input = input("Move (W=Up, S=Down, A=Left, D=Right, Q=Quit): ").lower()

        if move_input == "q":
            print("Exiting dungeon. Goodbye!")
            break
        elif move_input in ["w", "a", "s", "d"]:
            player.move(move_input, grid_size)
            
            # 30% chance to trigger a monster fight upon moving (if not at start or exit)
            if (player.x, player.y) not in [(0, 0), exit_pos] and random.random() < 0.3:
                trigger_encounter(player)
        else:
            print("Invalid key! Use W, A, S, or D.")

    if player.hp <= 0:
        print("\n💀 GAME OVER! You perished in the dungeon.")


if __name__ == "__main__":
    main()