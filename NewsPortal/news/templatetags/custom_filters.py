from django import template

register = template.Library()

stop_word = [
    'Voldemort',
    'found'
]


@register.filter(name='censor')
def censor(value):
    for s_w in stop_word:
        if isinstance(value, str):
            value = value.replace(s_w[1:], "*" * 5)
        else:
            raise ValueError(f'Ошибка! Тип {type(value)} не подходит!')
    return value
