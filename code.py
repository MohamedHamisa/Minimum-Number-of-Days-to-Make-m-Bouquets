class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int):
        if len(bloomDay) < m*k: return -1 # edge case 
        
        def fn(d):
            """Return True if it is possible to make m bouquets on given day."""
            mm, kk = m, k
            for x in bloomDay: 
                kk = kk-1 if x <= d else k
                if not kk: mm, kk = mm-1, k
                if not mm: return True
            return False 
        
        # "first true" binary search
        lo, hi = 0, max(bloomDay)
        while lo < hi:
            mid = lo + hi >> 1
            if fn(mid): hi = mid
            else: lo = mid + 1
        return lo  
