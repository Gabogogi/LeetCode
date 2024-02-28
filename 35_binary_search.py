'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity
Input: nums = [1,3,5,6], target = 5 Output: 2 Input: nums = [1,3,5,6], target = 2
Output: 1 Input: nums = [1,3,5,6], target = 7 Output: 4
'''
def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1 # two pointers , one at start the other at end

    while l <= r:
        mid = (l + r) // 2

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l
