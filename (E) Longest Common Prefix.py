def longestCommonPrefix(strs):
    wrapper = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i < len(s) and strs[0][i] == s[i]:
                print(s[:i])
    return wrapper


print(longestCommonPrefix(["flower","flow","flight"]))