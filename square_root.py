class SquareRoot:
    def __init__(self, n):
        self.n = n

    def nearest_square(self):
        if self.n==0 | self.n==1:
            return self.n
        start = 1
        end =  self.n
        ans = 0
        while start <= end:
            mid = (end + start) // 2
            if mid*mid == self.n: 
                return mid 
            if mid*mid < self.n:
                start = mid+1
                
            else:
                end = mid-1
                ans = mid
        return ans
