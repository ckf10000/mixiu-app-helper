# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  mixiu-app-helper
# FileName:     chat.py
# Description:  TODO
# Author:       zhouhanlin
# CreateDate:   2024/08/16
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from poco.proxy import UIObjectProxy
from airtest_helper.platform import ANDROID_PLATFORM
from airtest_helper.libs.extend import get_poco_factory
from mixiu_app_helper.api.page.portal import UiHomePortalApi, UiMessagePortalApi


class UiHallChatApi(UiHomePortalApi):

    def get_hall_chat_enter(self, loop: int = 20, peroid: float = 0.5, **kwargs) -> UIObjectProxy:
        d_type = ""
        name = ""
        if self.platform == ANDROID_PLATFORM:
            d_type = "android.widget.TextView"
            name = "com.mixiu.com:id/iv_anchor_im"
        options = dict(d_type=d_type, name=name, text="来聊聊天...")
        return get_poco_factory(poco=self.poco, options=options, loop=loop, peroid=peroid, **kwargs)

    def send_hall_chat_content(self, content: str, loop: int = 20, peroid: float = 0.5, **kwargs) -> bool:
        hall_chat_enter_poco = self.get_hall_chat_enter(loop=loop, peroid=peroid, **kwargs)
        if hall_chat_enter_poco:
            hall_chat_enter_poco.click()
            hall_chat_enter_poco.set_text(content)
            # 模拟键盘按下回车键（keyCode为66表示回车键）
            self.dev.keyevent(keyname="66")
            return True
        return False


class UiPrivateChatApi(UiMessagePortalApi):
    pass
