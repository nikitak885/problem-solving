class FindAnagram:
    def Anagram(self,first:str, second:str) ->bool:
        if len(first) != len(second):
            return False 
        return sorted(first) == sorted(second)
    
stringone = "madam"
stringtwo = "madam"
fana = FindAnagram()
val = fana.Anagram(stringone,stringtwo)
print("the given strings is anagram:", val)