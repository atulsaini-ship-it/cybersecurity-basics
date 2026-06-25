import string
import secrets

def check_password_strength(password):
    """Evaluates password strength based on standard security metrics."""
    score = 0
    feedback = []

    
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("• Should be at least 12 characters long.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("• Missing an uppercase letter (A-Z).")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("• Missing a lowercase letter (a-z).")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("• Missing a number (0-9).")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("• Missing a special character (e.g., !, @, #, $).")

    
    if score <= 2:
        rating = " WEAK"
    elif score <= 4:
        rating = " MEDIUM"
    else:
        rating = " STRONG"

    return rating, feedback

def generate_strong_password(length=16):
    """Generates a cryptographically secure random password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    print("---  PassFort: Password Strength Tool ---")
    user_pass = input("Enter a password to test: ").strip()
    
    rating, feedback = check_password_strength(user_pass)
    print(f"\nPassword Rating: {rating}")
    
    if feedback:
        print("Suggestions to improve:")
        for line in feedback:
            print(line)
            
    if rating != " STRONG":
        choice = input("\nWould you like to generate a strong password instead? (y/n): ").lower()
        if choice == 'y':
            new_pass = generate_strong_password()
            print(f"\n[+] Your secure password: {new_pass}")
            print("[*] Keep it safe!")

if __name__ == "__main__":
    main()
