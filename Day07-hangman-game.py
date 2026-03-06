import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

Game_over = False
correct_letter=[]

while not Game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        Game_over = True
        print("You win")
