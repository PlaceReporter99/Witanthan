import instructions
import codedict
# Codes 0 to 127: Dynamic Instructions
# Codes 128 to 255: Instruction Modifiers
class CodeError(Exception):
    pass

def mapcpage(nums):
    l = []
    d = codedict.codedict()
    for x in nums:
        try:
            l.append(d[x])
        except KeyError:
            pass
    return l

def run(flag, code, inp):
    code = mapcpage([ord(x) for x in code])
    stack = [inp]
    mod = 255
    for x in code:
        if x <= 127:
            try:
                instructions.instructions[mod][x](stack)
            except KeyError:
                pass
            except Exception as e:
                raise CodeError(str(e))
        else:
            mod = x 