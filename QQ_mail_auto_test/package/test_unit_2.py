from calculator import Count
import unittest


class TestAdd(unittest.TestCase):
    """测试加"""

    def setUp(self):
        print("test start")

    def test_add(self):
        """加法1"""
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        """加法2"""
        j = Count(34, 25)
        self.assertEqual(j.add(), 59)

    def tearDown(self):
        print("test end")


class TestSub(unittest.TestCase):
    """测试加"""

    def setUp(self):
        print("test start")

    def test_sub(self):
        """减法1"""
        j = Count(4, 3)
        self.assertEqual(j.sub(), 1)

    def test_sub2(self):
        """减法2"""
        j = Count(34, 25)
        self.assertEqual(j.sub(), 9)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    # suite = unittest.TestSuite
    # suite.addTest(TestAdd("test_add"))
    # suite.addTest(TestAdd("test_add2"))
    # suite.addTest(TestSub("test_sub"))
    # suite.addTest(TestSub("test_sub2"))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()

