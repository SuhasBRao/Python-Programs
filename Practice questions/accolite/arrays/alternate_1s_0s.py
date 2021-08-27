import unittest
# testing using unittest module
class TestSolution(unittest.TestCase):
    message = 'Test case failed'
    def test1(self):
        self.assertEqual( alternate([1,1,0,0]), [1,0,1,0], 
                        self.message)
    def test2(self):
        
        self.assertEqual( alternate([1,1,1,1,1,0,0,0,0,0]), [1,0,1,0,1,0,1,0,1,0],
                        self.message)

def alternate(arr):
    for i in range(len(arr) - 1):
        cur = arr[i]
        next = 0 if cur else 1
        j = i+1
        while j<len(arr) - 1 and arr[j] != next:
            j += 1
        arr[j], arr[i+1] = arr[i+1], arr[j]
    return arr

if __name__=="__main__":
    #arr = list(map(int, input().split()))
    #print(alternate(arr))
    # testing using assert statement
    assert alternate([1,1,1,0,0,0]) == [1,0,1,0,1,0]
    # testing using unittest library
    
    unittest.main()