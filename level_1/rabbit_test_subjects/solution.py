def answer(y, x):
    # your code here
    y.sort()
    x.sort()
    profile=(x[0]-y[0])/x[0]
    result=int(100*(profile))
    return result
