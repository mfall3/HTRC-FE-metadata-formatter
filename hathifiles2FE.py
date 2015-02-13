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
    print('missing name of hathifile -- Usage: python3 ' + sys.argv[0] + ' hathifile [outDirectory] [startLine] [endLine]')
    sys.exit(1)

# set defaults values for optional arguments
outDir = os.getcwd()
startLine = 0

def file_line_count(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
        return i+1

endLine = file_line_count(hathifile)

# use the provided output directory, or default to current directory
if len(sys.argv) > 2:
    outDir = sys.argv[2]

def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# use provided start line, if valid
if len(sys.argv) > 3 and is_int(sys.argv[3]) and int(sys.argv[3]) < endLine:
    startLine = int(sys.argv[3])

# use provided end line, if valid
if len(sys.argv) > 4 and is_int(sys.argv[4]) and int(sys.argv[4]) < endLine and int(sys.argv[4]) >= startLine :
    endLine = int(sys.argv[4])

ts = time.time();
batchtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d'+'T'+'%H:%M')

linenum = 1

# log progress
with open(outDir + os.sep + "hathifiles2FE_log_" + batchtime + ".txt", 'w+') as log:


    print("startLine: " + str(startLine))
    print("endLine: " + str(endLine))
    log.write("startLine: " + str(startLine)  + "\n")
    log.write("endLine: " + str(endLine)  + "\n")

    # read in one line at a time, write out one file at a time, logging progress
    with open(hathifile) as f:

        for line in f:

            if linenum >= startLine:

                print ("reading line number " + str(linenum) + " ...")
                log.write("reading line number " + str(linenum) + "\n")
                row = (line.split('\t'))
                institutionId = (row[0].split('.'))[0]
                cleanVolumeId = row[0].replace(':', "+")
                cleanVolumeId = cleanVolumeId.replace('/', "=")
                if not os.path.exists(outDir + os.sep  + institutionId):
                    os.makedirs(outDir + os.sep + institutionId)
                outfileName = outDir + os.sep + institutionId + os.sep + cleanVolumeId + '.json'

                with open(outfileName, 'w') as outfile:
                    print("writing " + outfileName + " ..." )
                    log.write("writing " + outfileName + "\n")
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

            linenum+=1
            if linenum > endLine:
                f.close()
                log.close()
                print("done")
                exit()

        f.close()
    log.close()

print("done")