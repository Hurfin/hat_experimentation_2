# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
path = r"E:\pythonCode\RJ_experimentation_1\Data_1\field_jq"
fields_ = os.listdir(path)
print(fields_[0].rstrip('.txt').split('_'))

