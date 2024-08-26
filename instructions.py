# Modifier 128: Number and Maths functions
# Modifier 129: String functions
# Modifier 130: Array and Dictionary functions
# Modifier 131: Loop construct
# Modifier 132: Constants
# Modifier 133: Create string
# Modifier 134: Create base 128 number
# Modifier 135 - 254: TBD
# Modifier 255: Common Functions (Default Modifier)

import math

def constant(c):
    def inner(stack):
        return stack.append(c)
    return inner

instructions = {132: {
    1: constant("hello world")
    2: constant("Hello World")
    3: constant("Hello world")
    4: constant("HELLO WORLD")
    5: constant("Hello, World!")
    6: constant("HELLO WORLD!")
    7: constant("Hello, World")
    8: constant("Hello world!")
    9: constant("")
    10: constant(1)
    11: constant(2)
    12: constant(3)
    13: constant(4)
    14: constant(5)
    15: constant(6)
    16: constant(7)
    17: constant(8)
    18: constant(9)
    19: constant(0)
    20: constant(10)
    21: constant(26)
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

@instruction(1, 128)
def p10(stack):
    stack.append(10 ** stack.pop())

@instruction(2, 128)
def pe(stack):
    stack.append(math.e ** stack.pop())

@instruction(3, 128)
def a(stack):
    stack.append(stack.pop() + stack.pop())

@instruction(4, 128)
def s(stack):
    a, b = stack.pop(), stack.pop()
    stack.append(b - a)

@instruction(5, 128)
def m(stack):
    stack.append(stack.pop() * stack.pop())

@instructions(6, 128)
def d(stack):
    a, b = stack.pop(), stack.pop()
    stack.append(b / a)

@instructions(7, 128)
def p(stack):
    a, b = stack.pop(), stack.pop()
    stack.append(b ** a)

@instructions(8, 128)
def sn(stack):
    a, b = stack.pop(), stack.pop()
    stack.append(b * 10 ** a)