print("Description: This program will find the biggest value from the string of numbers")

nums = input("Please input some numbers (comma separated): ")
nums = nums.split(",")
if len(nums) == 0:
    print("There's no input numbers")
    exit(0)
for i in range(len(nums)):
    nums[i] = float(nums[i])


max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num

print(f"Max value: {max_num}" )

