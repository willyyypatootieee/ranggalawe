# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ranggalawe = Character("Ranggalawe", color="#c8ffc8")
define kerajaan = Character("NAsir", color="#c8ffc8")
# define e = Character("Fikri", color="#c8ffc8")
# define j = Character("NAsir", color="#c8ffc8")
# define e = Character("Fikri", color="#c8ffc8")
# define j = Character("NAsir", color="#c8ffc8")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room at Transform(zoom=5.0) with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nasir_angry at Transform(xalign=0.5, yalign=1.0, zoom=0.4) with dissolve

    # These display lines of dialogue.

    ranggalawe "Hello! you just made a visual novel! Isn't that great?"

    ranggalawe "Once you add a story, pictures, and music, you can release it to the world!"

    scene bg room at Transform(zoom=5.0) with fade

    show nasir_idle at Transform(zoom=0.4) with dissolve

    ranggalawe "Scene 2!"


    # This ends the game.

    

    return

    
