from datetime import datetime

name = input("What is your name? ")
greeting = "Good morning" if 4 <= hour < 12 else "Good afternoon" if 12 <= hour < 16 else "Good night"
print(f"{greeting}, {name}!")