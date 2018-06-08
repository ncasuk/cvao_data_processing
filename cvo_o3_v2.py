# args exected
#1. full path to file to be converted
#2. output diretory 
#3. path to meta file

import sys
#import os
import numpy as np
from collections import namedtuple
from cvo_o3_parser_v1 import cvo_o3_get_file_v1, cvo_o3_parse_data_v1
from cvo_o3_NC_v2 import cvo_o3_get_meta_v1, NC_cvo_o3_v1

data = namedtuple("data", "DT DoY ET O3 flag")
#path to file in
fin = str(sys.argv[1])
#path to file out
dout = str(sys.argv[2])
#"/AMF_Netcdf/"
#path to file metadata
fn_meta = str(sys.argv[3])

#get the data
data.DT, data.DoY, data.ET, data.O3, data.flag = cvo_o3_get_file_v1(fin, np)

#parse data - make sure just one month of data
data.DT, data.DoY, data.ET, data.O3, data.flag = cvo_o3_parse_data_v1(data)

#save nc file
meta = cvo_o3_get_meta_v1(fn_meta)
NC_cvo_o3_v1(meta, dout, data, np)

