﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Robert Frost")

image path_choice = "autumn_park_autumn_stroll_park_leaves_listopad_yellow_leaves_golden_autumn-1217917.jpeg"
image second_road_pic = "autumn_leaves_tree_autumn_leaf_yellow_leaves_nature_golden_autumn_listopad-679772.jpeg"
image first_road_pic = "path_in_the_park_fallen_leaves_park_autumn_autumn_park_romantic_stromovka_czech_budejovice-1380032.jpeg"

# The game starts here.

label start:

    scene path_choice
    
    play music "Lee_Rosevere_-_04_-_Keeping_Old_Letters.mp3" loop

    "Two roads diverged in a yellow wood"
    
    "And sorry I could not travel both\n
    And be one traveler, long I stood\n"
    
    "And looked down one as far as I could\n
    To where it bent in the undergrowth"
    
    r "Should I take the first road? Or the second?"
    
    menu:
            "The first road":
                jump first_road

            "The second road":
                jump second_road
    
    label second_road:
        scene second_road_pic
    
        "Oh, I kept the first for another day!"
        
        "Yet knowing how way leads on to way,\n
        I doubted if I should ever come back.\n"
        
        jump ending_regrets
    
    label first_road:
        scene first_road_pic
    
        "Then took the other, as just as fair,\n
        And having perhaps the better claim,\n
        Because it was grassy and wanted wear\n"

        "Though as for that the passing there\n
        Had worn them really about the same\n"

        "And both that morning equally lay\n
        In leaves no step had trodden black.\n"
        
        jump ending_regrets
        
    label ending_regrets:

        " I shall be telling this with a sigh\n
        Somewhere ages and ages hence:\n
        Two roads diverged in a wood, and I—\n"

        "I took the one less traveled by,\n
        And that has made all the difference.\n"
        
    stop music

    # Thus ends this brief game.

    return
