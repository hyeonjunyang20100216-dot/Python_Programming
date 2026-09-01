i = 1
while i < 11:
    print(i)
    i += 1
    if i == 6 :
        break
else :
    print("End")

nums = [1,3,5,7,9]
target = 2
i = 0
while i < len(nums):
    if nums[i] == target:
        print("find")
        break
        i += 1
    else:
        print("not found")

