from django.template.defaulttags import register



@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# def get_value(dictionary, key,key2='testresult'):
#     for id,val in dictionary.items():
#         if id == key:
#             return val.get(key2)
#         else:
#             return 0