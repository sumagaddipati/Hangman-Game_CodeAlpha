import random

# Dictionary of categories and words for the Hangman game
categories = {
    "Programming Languages": ["python", "javascript", "ruby", "java", "swift"],
    "Fruits": ["apple", "banana", "cherry", "date", "fig"],
    "Countries": ["canada", "brazil", "india", "germany", "france"]
}

# Function to select a random word from the chosen category
def choose_word_and_category():
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    return category, word

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Function to check if the word is completely guessed
def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def hangman():
    category, word = choose_word_and_category()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    print(f"Category: {category}")
    print("Guess the word, one letter at a time.")
    print(display_word(word, guessed_letters))
    
    while incorrect_guesses < max_incorrect_guesses and not is_word_guessed(word, guessed_letters):
        guess = input("Enter a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")
        
        print(display_word(word, guessed_letters))
    
    if is_word_guessed(word, guessed_letters):
        print("Congratulations! You've guessed the word.")
    else:
        print(f"Sorry, you've run out of guesses. The word was '{word}'.")

if _name_ == "_main_":
    hangman()