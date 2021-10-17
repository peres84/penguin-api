from bson import json_util 

def serialize(fn):
    def wrapper(*args,**kwargs):
        res =  fn(*args,**kwargs)
        return json_util.dumps(res)
    wrapper.__name__= fn.__name__
    return wrapper