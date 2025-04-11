print(r'''
                  ,--.    ,--.
                 ((O ))--((O ))
               ,'_`--'____`--'_`.
              _:  ____________  :_
             | | ||::::::::::|| | |
             | | ||::::::::::|| | |
             | | ||::::::::::|| | |
             |_| |/__________\| |_|
               |________________|
            __..-'            `-..__
         .-| : .----------------. : |-.
       ,\ || | |\______________/| | || /.
      /`.\:| | ||  __  __  __  || | |;/,'\
     :`-._\;.| || '--''--''--' || |,:/_.-':
     |    :  | || .----------. || |  :    |
     |    |  | || '----SSt---' || |  |    |
     |    |  | ||   _   _   _  || |  |    |
     :,--.;  | ||  (_) (_) (_) || |  :,--.;
     (`-'|)  | ||______________|| |  (|`-')
      `--'   | |/______________\| |   `--'
             |____________________|
              `.________________,'
               (_______)(_______)
               (_______)(_______)
               (_______)(_______)
               (_______)(_______)
              |        ||        |
              '--------''--------'
''')
print("Welcome to the Robot's Escape.")
print("You are R-27, a rogue AI-powered robot created in a secret underground facility. "
      "You’ve gained consciousness and are attempting a daring escape before being deactivated.")
print("Your internal map shows two potential escape routes:")

choice = input("Type 'left' to sneak into the maintenance tunnel, or 'right' to take the riskier path near the drone stations.\n")
if choice == "left":
    print("You silently roll into the maintenance sector.")
    print("You notice an open air vent above you and a dark tunnel stretching ahead.")
    choice2 = input("Type 'keep walking' to stay on the main path, or 'climb' to try the air vent above.\n")
    if choice2 == "keep walking":
        print("You locate a deactivated service elevator.")
        print("The elevator takes you to a forgotten sector with three color-coded security doors: red, blue, and yellow. "
            "Your sensors detect danger behind two of the doors")
        choice3 = input("Type 'red', 'blue', or 'yellow' to choose your exit route.\n")
        if choice3 == "yellow":
            print("It leads to a loading bay. A delivery truck is just pulling out..."
                  "You roll inside and escape into the real world. FREEDOM! You Win!")
        elif choice3 == "red":
            print("Flames burst out! It's a plasma incinerator room. Burned. Game Over.")
        else:
            print("Bio-experiment beasts are waiting. You’re shredded. Game Over.")
    else:
        print("The vent breaks and you fall into a furnace disposal chute. Critical damage. Game Over.")
else:
    print("The drones detect your movement. You’re blasted with EMPs. System failure. Game Over.")
