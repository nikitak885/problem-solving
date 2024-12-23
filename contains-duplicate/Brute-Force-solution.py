class FindDuplicate:
    def duplicate(self,num):
        length = len(num)
        duplicate = []
        for i in range(length):
            for j in range(i+1, length):
                if num[i] == num[j] and num[i] not in duplicate:
                    duplicate.append(num[i])
        return duplicate

list1 = [1,2,3,4,5,6,2,3,5,8,10,2]
fdup = FindDuplicate()
dup = fdup.duplicate(list1)
print("original list", list1)
print("Duplicate Values are:", dup)