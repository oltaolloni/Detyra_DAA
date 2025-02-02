def majorityElement(nums):
    freq = {}  # Fjalor për të ruajtur numrin e shfaqjeve

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        if freq[num] > len(nums) // 2:  # Nëse kalon n/2, kthejmë menjëherë
            return num

nums1 = [3, 2, 3]
print(majorityElement(nums1))  # ➝ 3

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums2))  # ➝ 2