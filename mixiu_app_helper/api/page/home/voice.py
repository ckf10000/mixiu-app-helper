# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  mixiu-app-helper
# FileName:     voice.py
# Description:  TODO
# Author:       zhouhanlin
# CreateDate:   2024/08/16
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from poco.proxy import UIObjectProxy
from airtest_helper.platform import ANDROID_PLATFORM
from airtest_helper.libs.extend import get_poco_factory
from mixiu_app_helper.api.page.home.room import UiRoomApi


class UiVideoRoomApi(UiRoomApi):

    def get_randomly_idle_seat(self, loop: int = 20, peroid: float = 0.5, **kwargs) -> UIObjectProxy:
        d_type = ""
        name = ""
        if self.platform == ANDROID_PLATFORM:
            d_type = "android.widget.ImageView"
            name = "com.mixiu.com:id/addImg"
        options = dict(d_type=d_type, name=name)
        return get_poco_factory(poco=self.poco, options=options, loop=loop, peroid=peroid, **kwargs)

    def touch_randomly_idle_seat(self, loop: int = 20, peroid: float = 0.5, **kwargs) -> bool:
        idle_seat_poco = self.get_randomly_idle_seat(loop=loop, peroid=peroid, **kwargs)
        if idle_seat_poco:
            idle_seat_poco.click()
            return True
        return False

    def get_three_point_enter(self, loop: int = 20, peroid: float = 0.5, **kwargs) -> UIObjectProxy:
        d_type = ""
        name = ""
        if self.platform == ANDROID_PLATFORM:
            d_type = "android.widget.ImageView"
            name = "com.mixiu.com:id/live_leave_img"
        options = dict(d_type=d_type, name=name)
        return get_poco_factory(poco=self.poco, options=options, loop=loop, peroid=peroid, **kwargs)

    def touch_three_point_enter(self, loop: int = 20, peroid: float = 0.5, **kwargs) -> bool:
        three_point_enter_poco = self.get_three_point_enter(loop=loop, peroid=peroid, **kwargs)
        if three_point_enter_poco:
            three_point_enter_poco.click()
            return True
        return False

    def get_leave_video_room(self, loop: int = 20, peroid: float = 0.5, **kwargs) -> UIObjectProxy:
        d_type = name = ""
        if self.platform == ANDROID_PLATFORM:
            d_type = name = "android.widget.TextView"
        options = dict(d_type=d_type, name=name, text="退出房间")
        return get_poco_factory(poco=self.poco, options=options, loop=loop, peroid=peroid, **kwargs)

    def touch_leave_video_room(self, loop: int = 20, peroid: float = 0.5, **kwargs) -> bool:
        leave_video_room_poco = self.get_leave_video_room(loop=loop, peroid=peroid, **kwargs)
        if leave_video_room_poco:
            leave_video_room_poco.click()
            return True
        return False
