import re
from rest_framework import serializers


def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise serializers.ValidationError("Invalid email format.")
    return value


def validate_phone_number(value):
    phone_regex = r'^\+?1?\d{9,15}$'  # O'zingizning telefon raqami regex formatingizni kiritishingiz mumkin
    if not re.match(phone_regex, value):
        raise serializers.ValidationError("Invalid phone number format.")
    return value
