from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value,arg):
    arg_list = [arg.strip() for arg in arg.split(',')]
    if len(arg_list) == 2:
        return value.as_widget(attrs={'class':arg_list[0],'placeholder':arg_list[1]})
    else:
        return value.as_widget(attrs={'class':arg_list[0]})