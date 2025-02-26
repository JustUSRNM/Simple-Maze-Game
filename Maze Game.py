import random

#dictionary of the maze parts
hallways= {
    "left_forward": """\
         /|     /       \\      
        / |    /         \\ 
       /  |   /           \\ 
      /   |  /             \\ 
      |   | /               \\ 
      |___|/                 \\
      |                       \\
      |                        \\
      |                         \\
      |                          \\
      /                           \\
     /                             \\
    /                               \\
   /                                 \\
  /                                   \\
 /                                     \\""",
    "three_way": """\
         /|     /       \\     |\\   
        / |    /         \\    | \\
       /  |   /           \\   |  \\
      /   |  /             \\  |   \\
      |   | /               \\ |   |
      |___|/                 \\|___|
      |                           |
      |                           |
      |                           |
      |                           |
      /                           \\
     /                             \\
    /                               \\
   /                                 \\
  /                                   \\
 /                                     \\""",
    "right_forward": """\
                /       \\     |\\   
               /         \\    | \\
              /           \\   |  \\
             /             \\  |   \\
            /               \\ |   |
           /                 \\|___|
          /                       |
         /                        |
        /                         |
       /                          |
      /                           \\
     /                             \\
    /                               \\
   /                                 \\
  /                                   \\
 /                                     \\""",
    "left_right": """\
         /|                   |\\   
        / |                   | \\
       /  |                   |  \\
      /   |                   |   \\
      |   |                   |   |
      |___|___________________|___|
      |                           |
      |                           |
      |                           |
      |                           |
      /                           \\
     /                             \\
    /                               \\
   /                                 \\
  /                                   \\
 /                                     \\""",
 "exit": """\
          /                   \\
         /                     \\
        /                       \\
       /                         \\
      /                           \\
     /     "YOU FOUND THE EXIT"    \\
    /                               \\
   /                                 \\
  /                                   \\
 /                                     \\""",
}

# these are the valid moves for each of the maze parts
valid_moves = {
    "left_right": {"l", "r"},
    "left_forward": {"l", "f"},
    "right_forward": {"r", "f"},
    "three_way": {"l", "f", "r"},
    "exit": {}  # No valid moves, this is where you win
}

# Mapping of the short input to the full word
move_names = {"l": "left", "f": "forward", "r": "right"}

#variables of the game
depth = 0  # Tracks how deep the user is in the maze, the deeper you are the higher the chance of finding the exit


def get_random_hallway(depth):
    """Randomly selects a hallway type, increasing the exit chance as depth increases."""
    hallways_list = ["left_right", "left_forward", "right_forward", "three_way"]
    # Exit probability starts low and increases with depth
    exit_chance = min(0.02 + (depth * 0.02), 0.5)  # Max of 50% chance at deep levels
    # Generate probabilities dynamically
    hallway_chances = [0.25, 0.25, 0.25, 0.25 - exit_chance]  # Reduce total hallway chance for exit
    hallway_chances.append(exit_chance)  # increase exit chance
    # Select hallway based on probabilities
    return random.choices(hallways_list + ["exit"], weights=hallway_chances, k=1)[0]


# Gameplay Loop    
while True:
    depth = 0  # Reset depth on restart
    current_hallway = get_random_hallway(depth)  # Start with a random hallway
    
    while True:
        print(hallways[current_hallway])  # Show the current hallway

        if current_hallway == "exit":
            print("Congratulations! You found the exit!")
            break  # End maze loop

        move = input("Choose a direction (L/F/R): ").strip().lower()

        if move in valid_moves[current_hallway]:
            print(f"You move {move_names[move]}...\n")  # Shows full direction name
            depth += 1  # Increase depth when moving deeper into the maze
            current_hallway = get_random_hallway(depth)  # Generate new hallway
        else:
            print("Invalid direction! Try again.\n")
            # No change in hallway, it remains the same

    # Prompt player to restart
    restart = input('Type "restart" to return to the maze or anything else to quit: ').strip().lower()
    if restart != "restart":
        print("Thanks for playing!")
        break  # End the entire game loop