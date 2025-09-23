def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    curr = 0
    for i in range(len(t)):
        pointer = i
        if (s[curr] == t[pointer]) and (curr == len(s) - 1):
            return True
        if s[curr] == t[pointer]:
            curr += 1
        print(curr, pointer)
    return False



if __name__ == "__main__":
    s = "agd"
    t = "ahbgdc"
    x = "axc"
    print(isSubsequence(s, t))
