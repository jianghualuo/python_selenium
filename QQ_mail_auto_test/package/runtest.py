import unittest
import test_unit
import test_unit_3

suite = unittest.TestSuite()

suite.addTest(test_unit.TestCount("test_add"))

suite.addTest(test_unit_3.TestSub("test_sub"))
suite.addTest(test_unit_3.TestSub("test_sub2"))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
