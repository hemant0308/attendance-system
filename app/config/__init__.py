import json

from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, Authenticated, Everyone, ALL_PERMISSIONS, DENY_ALL,Deny
from marshmallow import class_registry,Schema

from app.models.meta import Base
from app.utils import to_camel_case,to_snake_case,change_dict_keys
from app import constants
from app.constants import Permissions

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

def is_admin(request):
    roles = request.jwt_claims.get('roles',[])
    return True if constants.Roles.Admin in roles else False

def get_school_id(request):
    return request.jwt_claims.get('school_id', None)

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

class RootFactory:
    __acl__ = [
        (Allow, Everyone, Permissions.every_one),
        (Allow, Authenticated, Permissions.authenticated_only),
        (Allow, constants.Roles.Admin, ALL_PERMISSIONS),
        DENY_ALL
    ]
    def __init__(self,request):
        pass

def get_principals(userid, request):
    return [role for role in request.jwt_claims.get('roles',[])]

def includeme(config):
    config.add_view_deriver(custom_deriver)
    config.add_request_method(validated,'validated',reify=True)
    config.add_request_method(is_admin, 'is_admin', reify=True)
    config.add_request_method(is_admin, 'school_id', reify=True)
    config.add_renderer(None, CustomRenderer)
    config.set_jwt_authentication_policy(callback=get_principals)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_root_factory(RootFactory)