#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   loader.py
@Time    :   2024/06/23 04:43:52
@Author  :   MuliMuri 
@Version :   1.0
@Desc    :   To load all the plugin from the ".plugins" folder
'''

import importlib
import inspect

from .plugins.plugin_base import PluginBase

class PluginLoader:
    def __init__(self) -> None:
        pass

    def load_plugin(self, module_name: str):
        pass

    def unload_plugin(self):
        pass

