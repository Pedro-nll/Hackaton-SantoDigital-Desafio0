# O(n)
def stringsDeAsteriscos(n: int):
    res = []
    s = ""
    for i in range(n):
        s += "*"
        res.append(s)
    return res


print(stringsDeAsteriscos(5))