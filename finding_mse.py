
# coding: utf-8

# In[3]:

import pandas as pd
import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Input an msID and the mseIDs with timepoints will output")
parser.add_argument("-m","--ms",
                    dest="ms",
                    type=str,
                    default=[],
                    metavar="ms####",
                    action="append",
                    help="import one or more msIDs using the format msIDs")
args = parser.parse_args()

if args.ms == []:
    raise parser.error("No msIDs inputted")
else:
    subjects = args.ms

info = pd.DataFrame.from_csv("/data/henry1/keshavan/lesion_seg/administrative.csv")

for num in range(len(subjects)):
    ind_data = info[info['msid'] == subjects[num]]
    trunc_data = ind_data[['msid','mse','timepoint']]
    data = trunc_data.values
    print "Here is the data for", subjects[num]
    for count in range(len(data)):
        print "timepoint:", data[count][2], "mseID:", data[count][1]
    print


# In[ ]:



