from celery import shared_task
from .models import PasswordCheck
import re

@shared_task
def analyze_password_strength(password, user_id):
    # password strength analysis code
    # Calculate the strength score and save it to the database
    strength_score = 0
    if any(x.isupper() for x in password):
        strength_score += 1
    if any(x.islower() for x in password):
        strength_score += 1
    if any(x.isdigit() for x in password):
        strength_score += 1
    special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
    if any(x for x in password if re.match(special_characters, x)):
        strength_score += 1
    if len(password) > 8:
        strength_score += 1

    # Save the password check result to the database
    password_check = PasswordCheck(password=password, strength_score=strength_score, user_id=user_id)
    password_check.save()

    return strength_score
