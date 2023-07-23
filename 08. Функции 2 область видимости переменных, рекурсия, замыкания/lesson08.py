
list_1 = [1, 2, 3, 5, 7, 6, 4, 8, 9, 10, 12, 11]


def bubble_sort(nums):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

bubble_sort(list_1)
print(list_1)