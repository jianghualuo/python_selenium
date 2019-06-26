from calculator import Count


# 定义测试类
class TestCount:

    def test_add(self):
        try:
            j = Count(2, 3)
            add = j.add()
            assert(add == 5), '结果错误'
        except AssertionError as msg:
            print(msg)
        else:
            print("test pass")

# 执行测试类的测试方法
mytest = TestCount()
mytest.test_add()

# 为了让单元测试代码更容易维护和编写，最好的方式是遵循一定的规范来编写测试用例。
