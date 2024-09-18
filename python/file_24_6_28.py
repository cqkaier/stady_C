#输入十个数，用起泡法将10个数从小到大排序
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
# nums = [1, 90, 3, 4, 50, 6, 7, 8, 9, 10]
nums = []
for i in range(10):
    nums.append(int(input("请输入第%d个数：" % (i+1))))

print(bubble_sort(nums))