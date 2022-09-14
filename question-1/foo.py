def foo(L):
    onlyNumbers = filter(lambda item: isinstance(item, int), L)
    onlyPositive = filter(lambda number: number >= 1, list(onlyNumbers))
    onlyPositive = list(onlyPositive)
    p = range(1,len(onlyPositive) + 1)
    leftOver = set(p)-set(onlyPositive)
    if len(leftOver) == 0:
        return len(onlyPositive) + 1
    else:
        return min(set(p)-set(onlyPositive))

"""
if __name__== "__main__" :
    l = [1,2,3,4,5,8, "hello", -1]
    print(foo(l))
"""