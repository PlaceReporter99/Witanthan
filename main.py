import instructions
# Codes 0 to 127: Dynamic Instructions
# Codes 128 to 255: Instruction Modifiers
def codedict():
    a = []
    b = [*range(256)]
    d = {}
    for x in range(32, 127):
        a.append(chr(x))
    for x in range(161, 173):
        a.append(chr(x))
    for x in range(174, 323):
        a.append(chr(x))
    for x in b:
        d.update({a[b]: b})
    return a

def mapcpage(nums):
    l = []
    d = codedict()
    for x in nums:
        try:
            l.append(d[x])
        except:
            pass
    return l

def run(flag, code, inp):
    code = mapcpage([ord(x) for x in code])
    stack = [inp]
    mod = 255
    for x in code:
        if x <= 127:
            instructions.instructions[mod][x](stack)
        else:
            mod = x 