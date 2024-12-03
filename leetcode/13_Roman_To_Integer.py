def romanToInt(s):
    """
    :type s: str
    :rtype: int
    s = "MCMXCIV"
    dict 
    1000 900 1900 90 1990 4 1994
    """
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for i, char in enumerate(s):
        if i == len(s) - 1 or roman[char] >= roman[s[i + 1]]:
            total += roman[char]
        else:
            total -= roman[char]
    return total
    #time O(n) space O(1)
