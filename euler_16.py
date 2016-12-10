
def split(num):
    return sum([ int(x) for x in str(num)])

base=2
exp=1000
print split(base**exp)
