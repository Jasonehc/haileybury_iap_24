print("Let's play Hangman!")
word = "password"

seen = set()
alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:    
    guess = input("Guess a letter.")
    if guess not in seen:
        seen.add(guess)
        display_word = ""
        for char in word:
            if char in seen:
                display_word += char
            else:
                display_word += "*"
        print(display_word)

        if display_word == word:
            break
        
        remaining_letters = ""
        for remaining_letter in alphabet:
            if remaining_letter not in seen:
                remaining_letters += remaining_letter
        print("Remaning letters are", remaining_letters)

    else:
        print("You've already guessed this letter.")
        
print("Congratulations, you won! The word was", word)