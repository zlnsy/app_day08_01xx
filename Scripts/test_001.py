import allure

class Test_001:
    @allure.step(title="第一个测试")
    def test_001_1(self):
        allure.attach("这是一个描述","我是描述的内容")
        assert 0
