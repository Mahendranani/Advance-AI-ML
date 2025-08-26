def dec(f):
    return lambda: f()
@dec
def hi(): print('hi')
hi()