#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# HTRC-FE-metadata-formatter
# ==========================
#
# Reads a hathifiles text file one line at a time and creates HTRC Feature Extraction metadata json files.
#
# hathifiles2FE.py

import sys
import json
import os
import time
import datetime
from collections import OrderedDict

# require the name of the hathifile to read
if len(sys.argv) > 1:
    hathifile = sys.argv[1]
else:
    print('missing name of hathifile -- Usage: python3 ' + sys.argv[0] + ' hathifile [outDirectory]')
    sys.exit(1)

# use the provided output directory, or default to current directory
if len(sys.argv) > 2:
    outDir = sys.argv[2]
else:
    outDir = os.getcwd()

ts = time.time();
batchtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d'+'T'+'%H:%M')

# read in one line at a time, write out one file at a time
with open(hathifile) as f:

    rows = (line.split('t') for line in f)

    for line in f:
        row = (line.split('\t'))
        institutionId = (row[0].split('.'))[0]
        cleanVolumeId = row[0].replace(':', "+")
        cleanVolumeId = cleanVolumeId.replace('/', "=")
        if not os.path.exists(outDir + os.sep  + institutionId):
            os.makedirs(outDir + os.sep + institutionId)
        outfileName = outDir + os.sep + institutionId + os.sep + cleanVolumeId + '.json'

        with open(outfileName, 'w') as outfile:
            print("writing " + outfileName + " ..." )
            meta = OrderedDict()
            meta["schemaVersion"] = "1.2"
            meta["dateCreated"] = batchtime
            meta["title"] = row[11]
            meta["pubDate"] = row[16]
            meta["language"] = row[18]
            meta["htBibUrl"]="http://catalog.hathitrust.org/api/volumes/full/htid/"+row[0]+ ".json"
            meta["handleUrl"] = "http://hdl.handle.net/2027/"+row[0]
            meta["oclc"] = row[7]
            meta["imprint"] = row[12]
            record = OrderedDict()
            record["metadata"] = meta
            json.dump(record, outfile)