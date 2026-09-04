import unittest
from toolboxx import keys,apply
class Tests(unittest.TestCase):
 def test_helpers(self): self.assertEqual(keys({"b":1,"a":2}),["a","b"]);self.assertEqual(apply({"a":1},{"b":2}),{"a":1,"b":2})
if __name__=="__main__":unittest.main()
