
def canConstruct( ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    ransom_hash = {}
    magazine_hash = {}

    for i in range(len(ransomNote)):
        if ransomNote[i] not in ransom_hash:
            ransom_hash[ransomNote[i]] = 1
        else:
            ransom_hash[ransomNote[i]] += 1

    for i in range(len(magazine)):
        if magazine[i] not in magazine_hash:
            magazine_hash[magazine[i]] = 1
        else:
            magazine_hash[magazine[i]] += 1
    
    
    for letter in ransomNote:
        if ransom_hash.get(letter, -1) != -1 and magazine_hash.get(letter, -1) == -1:
            return False 
        elif magazine_hash[letter] < ransom_hash[letter]:
            return False

    return True
rn = "abb"
mag = "aabb"
print(canConstruct(rn, mag))