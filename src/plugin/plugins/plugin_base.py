#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   plugin_base.py
@Time    :   2024/06/23 14:26:24
@Author  :   MuliMuri 
@Version :   1.0
@Desc    :   The base class for all the plugins
'''

from abc import ABC, abstractmethod

class PluginBase(ABC):
    @abstractmethod
    def run(self):
        pass
