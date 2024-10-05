# anagram - Two strings are anagrams if they contain the same characters in the same frequency, but arranged differently. 
# For example, "listen" and "silent" are anagrams because they both contain the same characters (l, i, s, t, e, n).

def anagram(s1,s2):

    if sorted(s1) == sorted(s2):
        return "anagrams"
    return "not anagrams"

print(anagram("ghjk", 'kjhg'))