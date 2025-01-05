class TwoSum:
    def Twosum(self, num: list[int], target:int) -> list[int]:
        listnew = []
        for i in range(len(num)):
            for j in range(len(num)):
                if num[i] + num[j] == target:
                    listnew.append([i,j])
        return listnew
ts = TwoSum()
listone = [1,2,3,4,5,6,7,8,9,10]
tar = 7
val = ts.Twosum(listone,tar)
print("the sum of two list index are:",val)