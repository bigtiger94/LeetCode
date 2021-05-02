class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # calculate median value from given list
        def cal_median(numlist: List[int]) -> float:
            N = len(numlist)
            if N % 2 == 1:
                return(numlist[N//2])
            else:
                return((numlist[N//2]+numlist[N//2-1])/2)
        
        # exception
        if len(nums1) == 0 and len(nums2) == 0:
            return(None)
        elif len(nums1) == 0 and len(nums2) > 0 :
            return(cal_median(nums2))
        elif len(nums1) > 0 and len(nums2) == 0:
            return(cal_median(nums1))

        nums = []
        ii = 0
        jj = 0
        # merge sort O(m+n)
        while ii < len(nums1) and jj < len(nums2):
            if nums1[ii] <= nums2[jj]:
                nums.append(nums1[ii])
                ii += 1
            else:
                nums.append(nums2[jj])
                jj += 1
                
            if ii == len(nums1):
                nums += nums2[jj:]
            if jj == len(nums2):
                nums += nums1[ii:]

        return(cal_median(nums))