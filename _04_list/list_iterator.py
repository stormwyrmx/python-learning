nums=[1,2,3,4,5,6,7,8,9,10]
nums_even=[]

for num in nums:
    if num%2==0:
        nums_even.append(num)
print(f"通过for循环，从列表{nums}中取出偶数,组成新列表{nums_even}")

i=0
nums_even=nums_even[:0]
while i<len(nums):
    if nums[i]%2==0:
        nums_even.append(nums[i])
    i+=1
print(f"通过while循环，从列表{nums}中取出偶数,组成新列表{nums_even}")