from functools import wraps

def validate(fn):
    '''
    fn - outer function for validation
    parametr_diap from 0 to 256 (incl.)
    if params are in parametr_diap - creating pixel, else: return error message
    '''
    @wraps(fn)
    def wrapper(*args):
        for i in args:
            if int(i) >= 0 and int(i) <= 256:
                continue
            else:
                return "Function call is not valid!"
        return fn(*args)
    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"