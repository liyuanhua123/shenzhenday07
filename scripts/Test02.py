import os
import sys

import allure

import allure
import pytest


class Test02:

    @allure.step("01yi")
    @allure.severity("critical")
    def test001(self):
      print("我是被执行")

    allure.attach("02bu","")
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test002(self):
        print("我被更新")
        print("123444")
