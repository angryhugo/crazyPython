def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    """Here's the comments"""
    if type(arg)== int or type(arg) == float:
        print abs(arg)
        return abs(arg)
    else:
        print "%s is not a number" % arg


biggest_number(1, 2, 3, -56)
smallest_number(1, 2, 3, -56)
distance_from_zero(-56)
distance_from_zero("hugo")