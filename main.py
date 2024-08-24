# Codes 0 to 127: Dynamic Instructions
# Codes 128 to 255: Instruction Modifiers
def mapcpage(nums): # We're using braille chars
    l = []
    for x in nums:
        if x == 32:
            l.append(0)
        else:
            l.append(x - 10240)
    return [x - 10240 for x in nums]

def run(code, inp):
    code = mapcpage([chr(x) for x in code])
    return 'not implemented'