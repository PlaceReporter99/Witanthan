# Modifier 128: Number and Maths functions
# Modifier 129: String functions
# Modifier 130: Array and Dictionary functions
# Modifier 131: Loop construct
# Modifier 132: Constants
# Modifier 133: Create string
# Modifier 134: Create base 128 number
# Modifier 135 - 254: TBD
# Modifier 255: Common Functions (Default Modifier)

def constant(c):
    def inner(stack):
        return stack.append(c)
    return inner

instructions = {132: {
    0: constant("")
    1: constant("hello world")
    2: constant("Hello World")
    3: constant("Hello world")
    4: constant("HELLO WORLD")
    5: constant("Hello, World!")
    6: constant("HELLO WORLD!")
    7: constant("Hello, World")
    8: constant("Hello world!")
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
