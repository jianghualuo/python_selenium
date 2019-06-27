from calculator import Count
import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")


class TestAdd(MyTest):

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(34, 25)
        self.assertEqual(j.add(), 59)


class TestSub(MyTest):

    def test_sub(self):
        j = Count(4, 3)
        self.assertEqual(j.sub(), 1)

    def test_sub2(self):
        j = Count(34, 25)
        self.assertEqual(j.sub(), 9)

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(TestAdd("test_add"))
#     suite.addTest(TestAdd("test_add2"))
#     suite.addTest(TestSub("test_sub"))
#     suite.addTest(TestSub("test_sub2"))
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

if __name__ == '__main__':
    unittest.main()