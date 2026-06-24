password = input("Enter a password to test: ")

print("\n--- Running Security Check ---")

if password == "123456" or password == "password" or password == "qwerty":
    print(" CRITICAL: This password is too common! Easily hacked.")

else:
    score = 0
    
    if len(password) >= 8:
        score = score + 1
    else:
        print(" Warning: Password should be at least 8 characters long.")
        
    if any(char.isdigit() for char in password):
        score = score + 1
    else:
        print(" Warning: Add at least one number (0-9).")
        
    if any(char.isupper() for char in password):
        score = score + 1
    else:
        print(" Warning: Add at least one capital letter (A-Z).")

    print(f"\nFinal Score: {score}/3")
    
    if score == 3:
        print(" STRONG: Good complexity!")
    elif score == 2:
        print(" MEDIUM: Acceptable, but follow the warnings above.")
    else:
        print(" WEAK: Very easy to guess or brute-force.")
