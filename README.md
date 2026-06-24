
password = input("Enter your password to check strength: ")
score = 0


if len(password) >= 8:
    score = score + 1
else:
    print("Warning: Password should be at least 8 characters long.")


if any(char.isdigit() for char in password):
    score = score + 1
else:
    print("Warning: Add at least one number (0-9).")


if any(char.isupper() for char in password):
    score = score + 1
else:
    print("Warning: Add at least one capital letter (A-Z).")


print(f"\nFinal Score: {score}/3")

if score == 3:
    print("STRONG: Good complexity!")
elif score == 2:
    print("MEDIUM: Acceptable, but follow the warnings above.")
else:
    print("WEAK: Very easy to guess or brute-force.")
    
