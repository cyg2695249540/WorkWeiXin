# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_demo.py
# @Author   : Pluto.
# @Time     : 2020/11/3 13:30
from time import sleep

import pytest
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
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("aaa")
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys(12345)
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_phone").send_keys(13711111111)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        assert "aaa" in namelist

    def test_delete_member(self):
        eles1 = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(1)")
        len1 = len(eles1)
        print(len1)
        if len1 > 1:
            eles1[0].click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_delete").click()
        self.driver.find_element(By.CSS_SELECTOR, "[d_ck='submit']").click()
        sleep(1)
        rtext = self.driver.find_element(By.CSS_SELECTOR, ".success").text
        assert rtext == "删除成功"
        sleep(1)
        eles2 = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(1)")
        len2 = len(eles2)
        print(len2)
        assert len1 - 1 == len2

    def test_addmember_fail(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("bbb")
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys(123456)
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_phone").send_keys(13711111112)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_cancel").click()
        self.driver.find_element(By.CSS_SELECTOR, "[node-type='cancel']").click()
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        assert "bbb" not in namelist

    @pytest.mark.flaky(reruns=1)
    def test_contact_addmember(self):
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        while True:
            self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            try:
                if self.driver.find_element(By.CSS_SELECTOR, ".js_btn_cancel") is not None:
                    break
            except:
                print("再次点击")
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("ccc")
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys(1234567)
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_phone").send_keys(13711111113)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")))
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        namelist = [name.text for name in eles]
        assert "ccc" in namelist

    def test_sss(self):
        eles=self.driver.find_elements(By.XPATH,"//*[@class='qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container']//a[@class='jstree-anchor']")
        eles[0].click()
    def test_111(self):
        self.driver.find_element(By.LINK_TEXT,"删除").click()