class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <=1:
            return nums
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        left_sorted = self.sortArray(left_half)
        right_sorted = self.sortArray(right_half)

        sorted_array = self.merge(left_sorted, right_sorted)
        return sorted_array
    
    def merge(self, l_array, r_array):
        left_index , right_index = 0, 0
        sort_arr = []
        while ((left_index < len(l_array)) and (right_index < len(r_array))):
            if l_array[left_index] < r_array[right_index]:
                sort_arr.append(l_array[left_index])
                left_index +=1
            else:
                sort_arr.append(r_array[right_index])
                right_index +=1

        sort_arr.extend(l_array[left_index:])
        sort_arr.extend(r_array[right_index:])

        return sort_arr
            

        
        