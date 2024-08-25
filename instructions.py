# Modifier 128: Number and Maths functions
# Modifier 129: String functions
# Modifier 130: Array and Dictionary functions
# Modifier 131: Constants
# Modifier 132 - 254: TBD
# Modifier 255: Common Functions (Default Modifier)

def constant(c):
    def inner(stack):
        return stack.append(c)
    return inner

instructions = {131: {

}}

def instruction(dynins, insmod):
    def decor(func):
        try:
            ins[insmod]
        except KeyError:
            ins[insmod] = {}
        
        ins[insmod].update({dynins: func})

        def inner(*a, **k):
            return func(*a, **k)
        return inner
    return decor
