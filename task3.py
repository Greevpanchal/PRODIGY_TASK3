def check_password_strength(password):
  """
  Evaluates the strength of a password based on various criteria.

  Args:
      password: The password to assess.

  Returns:
      A tuple containing:
          - Strength score (integer)
          - Feedback message (string)
  """
  score = 0
  feedback = ""

  # Check password length
  if len(password) >= 12:
    score += 2
    feedback += "Length is good! "
  elif len(password) >= 8:
    score += 1
    feedback += "Consider making it longer for better security. "
  else:
    feedback += "Password is too short. Use at least 8 characters. "

  # Check for uppercase letters
  if any(char.isupper() for char in password):
    score += 1
    feedback += "Good! It contains uppercase letters. "
  else:
    feedback += "Include uppercase letters for increased strength. "

  # Check for lowercase letters
  if any(char.islower() for char in password):
    score += 1
    feedback += "Good! It contains lowercase letters. "
  else:
    feedback += "Include lowercase letters for increased strength. "

  # Check for digits
  if any(char.isdigit() for char in password):
    score += 1
    feedback += "Good! It contains digits. "
  else:
    feedback += "Include digits for increased strength. "

  # Check for special characters
  if any(char in "!@#$%^&*()" for char in password):
    score += 1
    feedback += "Excellent! It contains special characters. "
  else:
    feedback += "Include special characters for the strongest security. "

  # Determine overall strength based on score
  if score >= 5:
    feedback += "This is a strong password."
  elif score >= 3:
    feedback += "This is a moderately strong password."
  else:
    feedback += "This is a weak password. Consider making it more complex."

  return score, feedback

def main():
  """
  Prompts user for password and displays strength assessment.
  """
  password = input("Enter your password: ")
  score, feedback = check_password_strength(password)

  print(f"Your password scored {score} out of 5.")
  print(feedback)

if __name__ == "__main__":
  main()
