import os
import bcrypt
from app import constants
from dotenv import load_dotenv


def hash_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    return pwhash.decode('utf8')

def check_password(pw, hashed_pw):
    expected_hash = hashed_pw.encode('utf8')
    return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
    
def to_camel_case(kebab_case):
    if kebab_case is not None:
        words = kebab_case.split("_")
        return words[0]+"".join([word.title() for word in words[1:]])
    return None

def to_snake_case(camel_case):
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_case)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def change_dict_keys(input_dict, method):
    if isinstance(input_dict, dict):
        keys = list(input_dict.keys())
        for key in keys:
            new_key = method(key)
            value = input_dict[key]
            change_dict_keys(value, method)
            del input_dict[key]
            input_dict[new_key] = value
    elif isinstance(input_dict,list):
        for el in input_dict:
            change_dict_keys(el, method)
    else:
        return
def set_empty_response(request):
    request.response.status_code = 204
    return constants.EMPTY_STRING

def get_user_id(request):
    return 1 #self.request.authenticated_userid

def expandvars_dict(settings):
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
    """Expands all environment variables in a settings dictionary."""
    return dict((key, os.path.expandvars(value)) for
                key, value in settings.items())