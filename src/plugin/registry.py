#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   registry.py
@Time    :   2024/06/23 18:38:55
@Author  :   MuliMuri 
@Version :   1.0
@Desc    :   Register and verify plugin dependencies
'''

class PluginRegistry:
    def __init__(self) -> None:
        self.plugins = {}

    def register_plugin(self, name: str, plugin_instance: object):
        pass

    def unregister_plugin(self, name: str):
        pass

    def get_plugin(self, name: str):
        pass

    def verify_dependencies(self, name: str):
        pass