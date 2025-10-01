def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) == 0:
            return True
        
    s_p = 0

    for letter in t:
        if letter == s[s_p]:
            s_p += 1
        if s_p == len(s):
            return True        

    
    return False



if __name__ == "__main__":
    s = "agd"
    t = "ahbgdc"
    x = "axc"
    print(isSubsequence(s, t))
