def gen():
    yield 1
    yield 2
for i in gen(): print(i)