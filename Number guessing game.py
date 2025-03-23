Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... def number_guessing_game():
...     """Simple number guessing game."""
...     print("Welcome to the Number Guessing Game!")
...     number_to_guess = random.randint(1, 100)
...     attempts = 0
...     
...     while True:
...         try:
...             user_guess = int(input("Guess a number between 1 and 100: "))
...             attempts += 1
...             
...             if user_guess < 1 or user_guess > 100:
...                 print("Please guess a number within the range.")
...                 continue
...             
...             if user_guess < number_to_guess:
...                 print("Too low! Try again.")
...             elif user_guess > number_to_guess:
...                 print("Too high! Try again.")
...             else:
...                 print(f"Congratulations! You guessed the number in {attempts} attempts.")
...                 break
...         except ValueError:
...             print("Invalid input! Please enter a number.")
... 
... # Run the game
... if __name__ == "__main__":
