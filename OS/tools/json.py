import json

def json2dict(PATH):
    with open(PATH,'r') as f:
        DICT = json.load(f)
    return DICT
def dict2json(DICT,PATH):
    with open(PATH,'w') as f:
        f.write(json.dumps(DICT))