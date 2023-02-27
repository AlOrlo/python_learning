
def decorator_apply(n):   #factory accepts a function (lambda) as an input
    def decorator(func):
        def wrapper(*args, **kwargs):
            return n(func(*args, **kwargs))
        return wrapper
    return decorator



@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num
