import random

def draw_hangman(attempts):
    stages = [
        '''
        +---+
        |   |
            |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
        '''
    ]
    return stages[attempts]

words_list = ["bad", "ugly", "good"]
computer_choice = random.choice(words_list)
display_word = ['-'] * len(computer_choice)

print(draw_hangman(0))

lives = 6
guessed_letters = set()
hangman_stage = 0

while '-' in display_word and lives > 0:
    print('Current word: ' + ''.join(display_word))
    entry = input('Please enter a letter: ').lower()

    if len(entry) != 1 or not entry.isalpha():
        print("❗ Please enter a single alphabetical letter.\n")
        continue

    if entry in guessed_letters:
        print(f'\nYou already guessed the letter "{entry}". Lives left: {lives}\n')
        continue

    guessed_letters.add(entry)

    if entry in computer_choice:
        for i, letter in enumerate(computer_choice):
            if letter == entry:
                display_word[i] = entry
        print("Good guess!\n")
    else:
        lives -= 1
        hangman_stage += 1
        print(f"Wrong guess! You lost a life. Lives remaining: {lives} " + '♥️' * lives + "\n")
        print(draw_hangman(hangman_stage))

if '-' not in display_word:
    print(f"🎉 Congratulations! You guessed the word: {computer_choice}")
else:
    print("😞 You lose!")
    print(f"The word was: {computer_choice}")
    print(draw_hangman(6))
