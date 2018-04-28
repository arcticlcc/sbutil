#!/usr/bin/python
#
# Script to upload published product files to ScienceBase
#

#import psycopg2
# import yaml
import csv
import time
import sys
#import getpass
import pysb  # https://my.usgs.gov/bitbucket/projects/SBE/repos/pysb/browse

sb = pysb.SbSession()

sbuser = raw_input("Please enter your ScienceBase id: ")
#pswd = getpass.getpass('SB Password:')

sb.loginc(str(sbuser))
# Need to wait a bit after the login or errors can occur
time.sleep(5)

with open(sys.argv[1], 'rb') as csvfile:
    rows = csv.reader(csvfile, delimiter='|', quotechar='"')
    for row in rows:
        print row
        print "    ", "Uploading to {item} from {url}".format(
            item=row[0], url=row[1])

        item = sb.get_item(row[0])
        # s.upload_file_to_item(item, row[1])
print "\nDone!\n"
