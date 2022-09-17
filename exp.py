#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) 2014-2021 Megvii Inc. All rights reserved.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super().__init__()
        
        # basically, we just setup the minimum information here needed to properly use a model for inference:
        # number of classes, depth/width which is dependent on size of the YoloX model (here for yolox-l)
        self.num_classes = 1
        self.depth = 1.0
        self.width = 1.0
        
        