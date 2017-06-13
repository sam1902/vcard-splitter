#!/usr/bin/python

# 
# vCard splitter
# 
# Created by Samuel Prevost on 13/06/2017.
# Copyright © 2017 Samuel Prevost. All rights reserved.
# 

import sys

def helpMessage():
    print("This script split a vCard (.vcf) file containing multiple contacts into multiple vCard, one for each contact.")
    print("Syntax:")
    print("\tvcard-split.py /path/to/inputFile.vcf /path/to/out/ [prefix-for-new-files]")

def isValidVCard(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            if ("BEGIN:VCARD" in line):
                return True

    return False

# sys.argv[0] is the file itself
if len(sys.argv) < 3:
    helpMessage()
    exit()

input_file = sys.argv[1]
if not isValidVCard(input_file):
    print("The given file wasn't a valid vCard file !")
    helpMessage()
    exit()

output_dir = sys.argv[2]
# E.g. output_dir = "/Users/sam1902/Downloads/CHUMontpellierVCF/out/"
if output_dir[-1:] != '/':
    output_dir = output_dir + "/"

# E.g. output_seed = 'contacts-part-'
if len(sys.argv) >= 4:
    output_seed = sys.argv[3]
else:
    output_seed = ""

with open(input_file, 'r') as f:
    i = 0
    individualContact = []
    for line in f:
        if ("BEGIN:VCARD" in line):
            if i > 0:
                with open(output_dir + output_seed + str(i) + '.vcf','w') as oFile:
                    oFile.write(line)
                    for line in individualContact:
                        oFile.write(line) 
                del individualContact[:]
            i += 1
        else:
            individualContact.append(line)

    with open(output_dir + output_seed + str(i) + '.vcf','w') as oFile:
        oFile.write("BEGIN:VCARD\n")
        for line in individualContact:
            oFile.write(line) 

print("Done !")