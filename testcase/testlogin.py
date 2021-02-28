
class Testlogincase:

    def setuo(self):
        print("前置条件")

    def teardown(self):
        print("后置条件")

    def test_01(self):
        assert 1+1==2

    def test_02(self):
        assert 1+1==3
