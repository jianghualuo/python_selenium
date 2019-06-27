import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("直接跳过测试")

    @unittest.skipIf(3 > 2, "当条件为真时跳过测试")
    def test_skip_if(self):
        print("当条件为真时跳过测试")

    @unittest.skipUnless(3 > 2, "当条件为真时执行测试")
    def test_skip_unless(self):
        print("当条件为真时执行测试")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()

