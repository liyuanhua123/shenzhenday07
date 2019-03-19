import allure


class Test02:

    @allure.step("01yi")
    @allure.severity("critical")
    def test001(self):
      print("我是被执行")