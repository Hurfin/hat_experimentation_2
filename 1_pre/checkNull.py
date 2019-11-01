# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
path2 = r"E:\FengXu\result\JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName.txt"

data = pd.read_csv(path2, sep='\t', header=None)
data = data.dropna()
data.to_csv(r"E:\FengXu\result\1_JieqingContain_paperID_authorID_affiliationID_paperYear_normalizedName_displayName.txt",
            sep='\t',
            header=None,
            index=False)
