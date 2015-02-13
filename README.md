HTRC-FE-metadata-formatter
==========================

Reads a hathifiles text file one line at a time and creates HTRC Feature Extraction metadata json files for use in generating Feature Extraction files as described at https://sandbox.htrc.illinois.edu/HTRC-UI-Portal2/Features.

Usage: python3 hathifiles2FE.py hathifile outDirectory startLine endLine

A log file named hathifiles2FE_log_[timestamp].txt will be created in outDirectory.

Optional arguments are only optional if no other arguments are used after them.  For example, if startLine is provided, outDirectory must be provided.

## arguments:

+ *hathifile* is the filename of the tab-delimited text files containing metadata from HathiTrust
    - downloaded from http://www.hathitrust.org/hathifiles
    - described at http://www.hathitrust.org/hathifiles_description

+ *outDirectory* is the destination directory for the ouput metadata json files
    - optional
    - default is the current directory

+ *startLine* is the first line of the hathifile to be processed
    - optional
    - default is the first line of the hathifile

+ *endLine* is the last line of the hathifile to be processed
    - optional
    - default is the last line of the hathifile