def codedict():
    a = []
    b = [*range(256)]
    d = {}
    for x in range(32, 127):
        a.append(x)
    for x in range(161, 173):
        a.append(x)
    for x in range(174, 323):
        a.append(x)
    for x in b:
        d.update({a[x]: x})
    return d