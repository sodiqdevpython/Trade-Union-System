from django import template

register = template.Library()


@register.filter
def display_salary(val):
    val = str(val)[::-1]
    count = 0
    result = ''
    for i in val:
        if count % 3 == 0:
            result = result + f' {i}'
        else:
            result = result + i
        count += 1

    return result[::-1]