HTRC-FE-metadata-formatter
==========================

Reads a hathifiles text file one line at a time and creates HTRC Feature Extraction metadata json files.

Usage: python3 hathifiles2FE.py hathifile outDirectory

## arguments:

+ *hathifile* is the filename of the tab-delimited text files containing metadata from HathiTrust
    - downloaded from http://www.hathitrust.org/hathifiles
    - described at http://www.hathitrust.org/hathifiles_description

+ *outDirectory* is the destination directory for the ouput metadata json files
    - optional
    - default is the current directory