import json

CLASS_STR = '''class {class_name}(object):
    """ {class_name} DTO object

    Attributes:
{attributes_docstrings}
    """

    def __init__(self, {params_list}):
{attributes_initializes}
'''

ATTR_DOCSTRING = '        {name} ({data_type}): {description}'
ATTRIBUTE_INIT_STR = '        self.{name} = {name}'

with open('dtos.json', 'r') as f:
    dict_dtos = json.load(f)


for dict_dto_key in dict_dtos:
    attr_docstrings = []
    attr_inits = []
    params_list = []

    for dict_attr_key in dict_dtos[dict_dto_key]:
        data_type = dict_dtos[dict_dto_key][dict_attr_key]['data_type']
        description = dict_dtos[dict_dto_key][dict_attr_key]['description']

        attr_docstrings.append(ATTR_DOCSTRING.format(name=dict_attr_key,
                                                     data_type=data_type.replace('Dto', ''),
                                                     description=description))
        attr_inits.append(ATTRIBUTE_INIT_STR.format(name=dict_attr_key))
        params_list.append(dict_attr_key)

    class_str = CLASS_STR.format(class_name=dict_dto_key,
                                 attributes_docstrings='\n'.join(attr_docstrings),
                                 params_list=', '.join(params_list),
                                 attributes_initializes='\n'.join(attr_inits))

    filename = '%s.py' % dict_dto_key
    with open('/'.join(['dtos', filename]), 'w') as f:
        f.write(class_str)
