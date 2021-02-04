import random

wordList = ['abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie']


def getWordFromPlayer():
    word = input('Please enter a word.\n').upper()
    print(chr(27) + "[2J")
    return word

def getWordFromComputer():
    word = random.choice(wordList).upper()
    return word

print('Welcome to a Hangman game!')

option = ''
while option not in ['1', '2']:
    option = input('Make your choice.\nDo you want to play:\n1.Against a friend\n2.Against the computer\n')

if option == '1':
    word = getWordFromPlayer()
    practicalWord = list(word)
    
else:
    word = getWordFromComputer()
    practicalWord = list(word)

hiddenWord = []
for character in word:
    hiddenWord.append('_')

#print(word)
#print(hiddenWord)

attempts = 0
maxAttempts = 4


playGame = input('Are you ready to play?\n')
if playGame.lower()[0] == 'y':
    gameOn = True
else:
    gameOn = False

while gameOn == True:
    print(f'You have {maxAttempts - attempts} attempts remaining.')

    wordToGuess = ' '.join(hiddenWord)
    
    print('Word to guess:\n')
    print(wordToGuess)


    print('     ---------')
    print('     |       |')
    print('     |       ' + ('O' if attempts > 0 else ''))
    print('     |       ' + ('/\\' if attempts > 1 else ''))
    print('     |       ' + ('|' if attempts > 2 else ''))
    print('     |       ' + ('/\\' if attempts > 3 else ''))
    print('_____|_______')
    
    guess = input('Please guess a letter\n')
    guess = guess.upper()

    if guess in practicalWord:
        for i in range(len(practicalWord)):
            letter = practicalWord[i]
            if letter == guess:
                hiddenWord[i] = practicalWord[i]
                practicalWord[i] = '_'

    else:
        attempts += 1

    if all('_' == letter for letter in practicalWord):
        print('Congrats! You won!')

        gameOn = False
    
    if attempts >= maxAttempts:
        print('You lost! Better luck next time!')
    
        gameOn = False