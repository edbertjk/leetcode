def romanToInt(s):

    """
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    """
    res = 0

    dict = {}
    dict["I"] = 1
    dict["V"] = 5
    dict["X"] = 10
    dict["L"] = 50
    dict["C"] = 100
    dict["D"] = 500
    dict["M"] = 1000

    for i in range(len(s)):
        if i+1 < len(s) and dict[s[i]] < dict[s[i+1]]:
            res -= dict[s[i]]
        else:
            res += dict[s[i]]
    return res

print(romanToInt("IX"))
