import re

def assess_password_strength(password):

    length_criteria = len(password) >= 8
    
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[\W_]', password)) -
    
    feedback = []
    
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    
    if not has_upper:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if not has_lower:
        feedback.append("Password should contain at least one lowercase letter.")
    
    if not has_digit:
        feedback.append("Password should contain at least one number.")
    
    if not has_special:
        feedback.append("Password should contain at least one special character (e.g., !, @, #).")
    
  
    if length_criteria and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif len(password) >= 6 and (has_upper or has_lower) and (has_digit or has_special):
        strength = "Medium"
    else:
        strength = "Weak"
    
    # Return the strength and feedback
    return {
        'strength': strength,
        'feedback': feedback
    }

password = input("Enter a password: ")
result = assess_password_strength(password)

print(f"Password Strength: {result['strength']}")
if result['feedback']:
    print("Suggestions:")
    for suggestion in result['feedback']:
        print(f"- {suggestion}")
