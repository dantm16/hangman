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

def choose_word_easy():
    return random.choice(easy_words)

def choose_word_medium():
    return random.choice(medium_words)

def choose_word_hard():
    return random.choice(hard_words)

def display_progress():
    pass

def play_game():

    current_guesses = []

    print("Welcome to hangman! Please choose a difficulty:")
    print("Easy | Medium | Hard")

    difficulty = (input("Difficulty:")).lower()
    valid_difficultys = ["easy", "medium", "hard"]
    while difficulty not in valid_difficultys:
        print("Invalid input. Please choose from easy, medium, or hard")
        difficulty = (input("Difficulty:")).lower()
    print(f"You have chosen {difficulty}!")

    set_word = 0
    if difficulty == "easy":
        set_word = choose_word_easy()
    elif difficulty == "medium":
        set_word = choose_word_medium()
    else:
        set_word = choose_word_hard()

    print(set_word)

    

    





play_game()