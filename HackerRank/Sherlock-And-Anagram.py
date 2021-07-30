def sherlockAndAnagrams(s):
    n_ana = 0
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            for n_word in range(1, min(len(s)-i, len(s)-j)+1):
                if sorted(s[i:i+n_word]) == sorted(s[j:j+n_word]): n_ana += 1
    return n_ana
