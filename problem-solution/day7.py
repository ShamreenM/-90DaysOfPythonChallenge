#Find max, min, and average of numbers in a list

nums = [14,24,65,90.3]
maximum = nums[0]
minimum = nums[0]
total=0
for i in nums:
    if i>maximum:
        maximum=i
    elif i<minimum:
        minimum=i  
    total= total+i
average = total/len(nums)
print(maximum)
print(minimum)
print(average)