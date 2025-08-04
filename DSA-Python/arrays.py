nums = [2,7,11,15]
target = 9

tempList = nums[1:]

for i in range(len(nums)):
    for j in range(i+1,(len(nums))):
        if nums[i] + nums[j] == target:
            print([i,j])


prices = [7,1,5,3,6,4]
#here a stock's price is shown on 6 diff days
"""loop through
find min: store it
find max: store it
return the diff
"""
max_profit = 0
for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        if prices[i] < prices[j]:
            profit = prices[j]-prices[i]
            if max_profit < profit:
                max_profit = profit

print(max_profit)               