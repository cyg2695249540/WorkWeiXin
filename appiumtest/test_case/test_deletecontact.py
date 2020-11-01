# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_deletecontact.py
# @Author   : Pluto.
# @Time     : 2020/11/1 14:33
from appiumtest.page.app import App


class TestDeletecontact:
    def setup(self):
        self.app = App()
        self.main = App().start().goto_main_page()

    def teardown(self):
        self.app.stop()

    def test_deletement(self):
        self.main.goto_contact().goto_secrch_page().searchcontact(
        ).go_to_personal_information_setup_page().go_to_edit_member_page().delete_member()
