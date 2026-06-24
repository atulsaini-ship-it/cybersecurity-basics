# --- Simple Password Checker ---

# 1. Get the password from the user
password = input("Enter a password to test: ")

print("\n--- Running Security Check ---")

# 2. Check for common/weak passwords (Dictionary Attack Check)
if password == "123456" or password == "password" or password == "qwerty":
    print("❌ CRITICAL: This password is too common! Easily hacked.")

# 3. Check length and complexity using simple IF statements
else:
    score = 0
    
    # Check length
    if len(password) >= 8:
        score = score + 1
    else:
        print("⚠️ Warning: Password should be at least 8 characters long.")
        
    # Check if it contains a number
    if any(char.isdigit() for char in password):
        score = score + 1
    else:
        print("⚠️ Warning: Add at least one number (0-9).")
        
    # Check if it has an uppercase letter
    if any(char.isupper() for char in password):
        score = score + 1
    else:
        print("⚠️ Warning: Add at least one capital letter (A-Z).")

    # 4. Give final result based on points scored
    print(f"\nFinal Score: {score}/3")
    
    if score == 3:
        print("🟢 STRONG: Good complexity!")
    elif score == 2:
        print("🟡 MEDIUM: Acceptable, but follow the warnings above.")
    else:
        print("🔴 WEAK: Very easy to guess or brute-force.")
