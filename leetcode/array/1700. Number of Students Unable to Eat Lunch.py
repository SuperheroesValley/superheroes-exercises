class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = students.count(1)
        zeros = len(students) - ones
        
        for s in sandwiches:
            if s == 1:
                ones -= 1
            else:
                zeros -= 1
            
            if ones < 0:
                return zeros
            if zeros < 0:
                return ones
        
        return 0
