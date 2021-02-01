print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to the Treasure Island!\n\nYou\'re lost on this deserted island, but somehow feel that luck is on your side.\n')
choice = input('Are you ready to start the adventure of your life? y/n')
if choice.lower().startswith('n'):
    print('Very well, then. Sit on the shore and wait for someone to come and save you! It will no doubt happen shortly.')
    exit()
print('Excited to do the great deeds that are meant for you, you go exploring and find yourself at a crossroad.')
crossroad = input('Now, what is the right path to take? Choose wisely. right/left \n')
if crossroad.lower().startswith('r'):
    print('You decide to go right.\nYou see a village ahead and hurry towards it.\nYou notice a bunch of funny people cooking something in a huge cauldron in front of a hut.\nHungry as you are, you aproach them and ask for some food.\nOh! NO! It turns out they were thinking to cook you.')
    print('''
        (
               )  )
           ______(____
          (___________)
           /         \
          /           \
         |             |
     ____\             /____
    ()____'.__     __.'____()
    jgs  .'` .'```'. `-.
        ().'`       `'.()
        Means GAME OVER. On the bright side, you turned out to be quite tasty.
        ''')
    exit()
print('You go left and walk for a while.\nYou were starting to get tired when you see a lake ahead. \nThe water is dark and you wonder what kind of creatures are lurking in it.')
lake = input('What are you going to do? Swim to the other side or rest a little and wait for a boat to come? swim/wait\n')
if lake.lower().startswith('w'):
    print('You wait for so long that you forget what you were waiting for.\nWe reckon you\'d be still waiting if Charon\'s barge hadn\'t finally came to take you to the Underworld.')
    print('''
                    
                                                        _._
                                                    _/,__\,
                                                    __/ _/o'o
                                                /  '-.___'/  __
                                                /__   /\  )__/_))\
                    /_/,   __,____             // '-.____|--'  \\
                    e,e / //  /___/|           |/     \/\        \\
                    'o /))) : \___\|          /   ,    \/         \\
                    -'  \\__,_/|             \/ /      \          \\
                            \_\|              \/        \          \\
                            | ||              <    '_    \          \\
                            | ||             /    ,| /   /           \\
                            | ||             |   / |    /\            \\
                            | ||              \_/  |   | |             \\
                            | ||_______________,'  |__/  \              \\
                            \|/_______________\___/______\_             \\
                                \________________________     \__           \\        ___
                                \________________________    _\_____      \\ _____/
                                    \________________________               \\
                        ~~~~~~~~  b'ger /  ~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~ ~~~~\\~~~~
                            ~~~~~~~~~~~~~~    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    //
                 Means GAME OVER! Safe travels!
        ''')
    exit()
print('You bravely jump into the dark cold waters and start swimming.\nFrozen fingers try to pull you into the deepness, but you manage to escape and arrive safely on the other shore of the lake.\nRight in front of your eyes,, there are three little houses, inviting you to get inside and rest.\n')
color_choice = input('The funny thing is that each house has a different color: one is red, one is blue and one is yellow. Which one do you enter? red/blue/yellow\n')
if color_choice.lower().startswith('r'):
    print('Red definitely isn\'t your lucky color.\nToo bad you didn\'t remember to stop before being swallowed by flames.')
    print('''
                            (  .      )
                            )           (              )
                                    .  '   .   '  .  '  .
                            (    , )       (.   )  (   ',    )
                            .' ) ( . )    ,  ( ,     )   ( .
                        ). , ( .   (  ) ( , ')  .' (  ,    )
                        (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                    jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    Means GAME OVER. 
                            ''')
    exit()
elif color_choice.lower().startswith('b'):
    print('Blue definitely isn\'t your lucky color.\nYou step inside the house and hardly have time to see the beasts before they prey on you.')
    print('''
        /\_/\____,
                  ,___/\_/\ \  ~     /
                  \     ~  \ )   XXX
                    XXX     /    /\_/\___,
                       \o-o/-o-o/   ~    /
                        ) /     \    XXX
                       _|    / \ \_/
                    ,-/   _  \_/   \
                   / (   /____,__|  )
                  (  |_ (    )  \) _|
                 _/ _)   \   \__/   (_
         b'ger  (,-(,(,(,/      \,),),)
         Means GAME OVER. 
        ''')
    exit()
print('You enter the yellow house and find an amazing treasure.')
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
Congrats! You won the game!
''')