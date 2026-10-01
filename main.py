import sys

# Fix Windows terminal encoding
sys.stdout.reconfigure(encoding="utf-8")

from game import play_game


print("=" * 50)
print("             KAUN BANEGA LAKHPATI")
print("=" * 50)

print("Answer 10 questions and win ₹1,00,000!")
print("Question 5 is your safety checkpoint.")
print("You can exit after every correct answer.")

print("=" * 50)

input("\nPress Enter to start the game...")

play_game()
