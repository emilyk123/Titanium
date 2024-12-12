# Titanium

![titanium](https://github.com/user-attachments/assets/1e8994d2-c293-493a-b758-25e2cc4715c3)

## About 
*  Titanium is a game made in Python using the pygame library, and it is inspired by the game Frogger.

## How to play 
- Clone the repo to your computer 
- Open the file in VSCode
- Then press the play button in the game.py file
- WASD or Arrow keys allow the player to move their character
- When the player touches the water tiles, they lose one's health. In total, they have three health points. The health bar is the the top right of the screen.
- When the player loses all of their health, they are shown the game over screen.
- The player can move on top of the moving platforms to progress through the level.
- When the player gets to the end of the level and moves on top of the brown tiles, they move to the next level.
- Pressing the ESC button lets the player pause the game

## Camera 
- As the player moves, the camera follows the player’s movements
- The camera has a x and y-axis, so when the player moves side-to-side or up-and-down the camera moves too. 
- Once the player reaches the top level, the camera and player reset to the bottom of the screen for the next level.

## Power-up
- The player intersects power-up on all sides and spawns randomly
- Power-up randomly spawns without touching the water tiles
- Invisible powerup makes the player invisible and gives them extra health 
- There is also a speed power-up that increases the speed of the player. 


# Resources

## Assets Used
    # Dirt and Grass Tilemaps
        # https://bagong-games.itch.io/topdown-tileset
    # Water Tilemap
        # https://beeler.itch.io/top-down-earth-tileset

## Used to help set up project, player, and tilemap
    # https://www.youtube.com/watch?v=2gABYM5M0ww&t=2642s&ab_channel=DaFluffyPotato
    # Window and Game
        # https://www.youtube.com/watch?v=2gABYM5M0ww&t=2642s&ab_channel=DaFluffyPotato
        # https://dafluffypotato.com/assets/pg_tutorial (01_window and 02_images_input_collisions)
    # Player
        # https://www.youtube.com/watch?v=2gABYM5M0ww&t=2642s&ab_channel=DaFluffyPotato
        # https://dafluffypotato.com/assets/pg_tutorial (03_player_tiles_physics)
    # Tilemap
        # https://www.youtube.com/watch?v=2gABYM5M0ww&t=2642s&ab_channel=DaFluffyPotato
        # https://dafluffypotato.com/assets/pg_tutorial (03_player_tiles_physics)

## Used to help add player input delay
    # How to create a timer: https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer
    # How to create custom events: https://stackoverflow.com/questions/24475718/pygame-custom-event
