import random

easy_words = ["apple", "orange", "grape", "dance", "table", "chair", "cloud", 
    "mount", "sword", "liver", "beach", "floor", "jumpy", "lucky", 
    "melon", "flame", "water", "salt", "plaza", "breeze", 
    "radio", "sword", "candy", "grape", "sprint", "storm", "cream", 
    "north", "south"]

medium_words = ["notebook", "journey", "guitar", "bicycle", "shadow", "overcome", 
    "battery", "mystery", "holiday", "stranger", "lighthouse", "paradise", 
    "sunshine", "formula", "brilliant", "mountain", "friendship", "detective", 
    "wizardry", "eclipse", "journeys", "companion", "together", 
    "reliable", "mountain", "adventure", "stadium", "vacation"]

hard_words = ["perspective", "equilibrium", "revolution", "algorithm", "phenomenal", 
    "successful", "unfortunate", "wonderfully", "combination", "masterpiece", 
    "celebration", "corruption", "coincidence", "explanation", "substantial", 
    "development", "counterfeit", "contribution", "counterclockwise", "international", 
    "disastrously", "incredible", "inspirational", "unbelievable", "procrastinate", 
    "implementation", "unpredictable", "exaggeration", "rejuvenation", "relationship"]

def set_word(dif):
    if dif == "easy":
        return random.choice(easy_words)
    elif dif == "medium":
        return random.choice(medium_words)
    else:
        return random.choice(hard_words)


def display_progress(word, guesses):
    word_so_far = ""
    for char in word:
        if char in guesses:
            word_so_far += char
        else:
            word_so_far += "_"        
    return word_so_far

def get_user_guess():
    user_guess = input("Please enter a letter:").lower()
    while len(user_guess) != 1:
        print("Invalid length, please enter only a single letter.")
        user_guess = input("Please enter a letter:").lower()
    return user_guess  

def play_game():

    print("Welcome to Hangman! Please choose a difficulty:")
    print("Easy | Medium | Hard")

    difficulty = (input("Difficulty:")).lower()
    valid_difficultys = ["easy", "medium", "hard"]
    while difficulty not in valid_difficultys:
        print("Invalid input. Please choose from easy, medium, or hard")
        difficulty = (input("Difficulty:")).lower()
    print(f"You have chosen {difficulty}!")
    word = set_word(difficulty)
    current_guesses = 0
    guess_list = []
    
    print(display_progress(word, guess_list))
    
    while "_" in display_progress(word, guess_list):
        guess_list.append(get_user_guess())
        print(display_progress(word, guess_list))
        current_guesses += 1
    
    print(f"Congratulations! You won in {current_guesses} guesses!")
    
    

    #this line is just to test push/pulling from alternate workstations
    


play_game()