"""
#Problem1
nums= [1,3,2,4,5,3]
#return the index of first number that is greater than both neighbours

def findGreat(i):
    if i > 0 and i <= len(nums)-1:
        if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
         return True
    else:
        return False

for x in range(len(nums)):
    if findGreat(x):
     output = x
     break

print(output)
"""
"""
#Problem 2
nums = [10, 20, 4, 45, 99]
#return second largest number in list

largest_num = max(nums)
filtered_nums = []
for i in range(len(nums)):
    if nums[i] != largest_num:
        filtered_nums.append(nums[i])
if(filtered_nums):
    sec_largest_num = max(filtered_nums)
    print(sec_largest_num)
else:
    print("All numbers are same")"""

"""
#Problem 3
#reverse the integer

x = 123
temp = 0
minus = False
if x < 0:
    minus = True
    x = abs(x)
while x != 0:
    mod = x%10
    temp = temp*10 + mod
    x = x//10
if minus:
    print(-temp)
else:
    print(temp)"""

"""
#Problem 4 
# check for duplicates

nums = [1,2,3,4,2]
duplicate = False
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            duplicate = True
            break

print(duplicate)

#runs in O(n^2), adding set can make it run in o(n)
"""
"""
#Problem 5
# move zeroes to end

nums = [0,1,0,3,12]
print(nums)
for i in nums:
    if i == 0:
        nums.remove(i)
        nums.append(i)

print(nums)"""

#Problem 6
nums = [3,0,1]
# nums list has nums rnging 0 to n with 1 missing number
#so, essentially length of nums is the n

n = len(nums)
# while n!=0:
#     if n in nums:
#         n = n-1
#         break
# print(n)
for i in range(n+1):
    if i not in nums:
        print(i)
        break
