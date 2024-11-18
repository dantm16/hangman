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
    set_word = choose_word_easy()
    current_guesses = []
    print("Welcome to hangman! Please choose a difficulty:")
    print("Easy | Medium | Hard")
    print()





play_game()