#!/usr/bin/env python3

import pydoop.hdfs as hdfs
import pandas as pd

out = hdfs.load('/output/part-00000', mode = 'rt')

