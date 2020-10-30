# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/10/29 16:50
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



class TestDemo:
    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_addmember(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "[id='username']").send_keys("aaa")
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_acctid']").send_keys(12345)
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_phone']").send_keys(13711111111)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        assert "aaa" in namelist

    def test_addmember_fail(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "[id='username']").send_keys("bbb")
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_acctid']").send_keys(123456)
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_phone']").send_keys(13711111112)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_cancel").click()
        self.driver.find_element(By.CSS_SELECTOR,"[node-type='cancel']").click()
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        assert "bbb" in namelist

    def test_contact_addmember(self):
        self.driver.find_element(By.CSS_SELECTOR,".frame_nav_item:nth-child(2)").click()
        # WebDriverWait(self.driver,10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,".ww_operationBar .js_add_member")))
        while True:
            self.driver.find_element(By.CSS_SELECTOR,".ww_operationBar .js_add_member").click()
            try:
                if self.driver.find_element(By.CSS_SELECTOR, ".js_btn_cancel") is not None:
                    break
            except:
                print("再次点击")
        self.driver.find_element(By.CSS_SELECTOR, "[id='username']").send_keys("ccc")
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_acctid']").send_keys(1234567)
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_phone']").send_keys(13711111113)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        WebDriverWait(self.driver,10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")))
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        assert "ccc" in namelist





