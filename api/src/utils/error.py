class MissingArgumentError(Exception):
    def __init__(self, var_name, *args, **kwargs):
        self.var_name = var_name
        super().__init__(*args, **kwargs)
    def solve(self):
        return {"MissingArgumentError":f"Argument '{self.var_name}' is mandatory"}


def errorHandling(fn):
    def wrapper(*args,**kwargs):
        try:
            return fn(*args,**kwargs)
        except MissingArgumentError as e:
            return e.solve()
        except:
            return {
                "Error":"Something went Wrong"
            }
    wrapper.__name__= fn.__name__
    return wrapper