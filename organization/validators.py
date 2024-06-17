from rest_framework.exceptions import ValidationError
# from .models import IdCards  

# def validate_card_id(value):
#     if not (value[0:2].isalpha() and value[3:8].isdigit()):
#         raise ValidationError(
#             "ID karta haqiqiyga o'xshamayabdi!"
#         )
#     if IdCards.objects.filter(card_id=value).exists():
#         raise ValidationError(
#             "Bu ID raqam mavjud!"
#         )
