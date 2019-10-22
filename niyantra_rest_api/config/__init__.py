from marshmallow import class_registry,Schema
import json
from niyantra_rest_api.models.meta import Base
from niyantra_rest_api.utils import to_camel_case,to_snake_case,change_dict_keys

def custom_deriver(view,info):
    schema = info.options.get('schema')
    response_schema = info.options.get('response_schema')
    def custom_view(context, request):
        request.set_property(lambda r:schema, "schema",reify=True)
        request.set_property(lambda r:response_schema,"response_schema",reify=True)
        return view(context,request)
    return custom_view

custom_deriver.options = ('schema','response_schema')

def validated(request):
    schema = request.schema
    if schema is not None:
        json_body = request.json_body
        if isinstance(schema,(str,type)):
            if isinstance(schema, str):
                schema = class_registry.get_class(schema)
            change_dict_keys(json_body, to_snake_case)
        return schema().load(json_body)

class CustomRenderer(object):
    def __init__(self, info):
        pass

    def __call__(self,value,system):
        request = system['request']
        request.response.content_type = 'application/json'
        response_schema = request.response_schema

        many = False
        instance = value
        if(isinstance(value, list)):
            many = True
            if len(value) > 0:
                instance = value[0]
            else:
                instance = None

        if response_schema is not None and isinstance(instance, (Schema, Base)):
            if isinstance(response_schema,str):
                response_schema = class_registry.get_class(request.response_schema)
            res = response_schema().dump(value, many=many)
            change_dict_keys(res,to_camel_case)
            return json.dumps(res)
        else:
            return json.dumps(value)

def includeme(config):
    config.add_view_deriver(custom_deriver)
    config.add_request_method(validated,'validated',reify=True)
    config.add_renderer(None, CustomRenderer)