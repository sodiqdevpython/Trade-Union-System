from rest_framework.exceptions import ValidationError
from .models import User  

def validate_card_id(value):
    if not (value[0:2].isalpha() and value[3:8].isdigit()):
        raise ValidationError(
            "ID karta haqiqiyga o'xshamayabdi!"
        )
    if User.objects.filter(id_card=value).exists():
        raise ValidationError(
            "Bu ID raqam mavjud!"
        )
