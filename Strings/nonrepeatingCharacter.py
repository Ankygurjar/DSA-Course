








def nonrepeatingCharacter(self,s):
        #code here
        count = Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return ch
        
        return -1

















