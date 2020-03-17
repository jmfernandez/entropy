#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''
Calculate Shannon Entropy (min bits per byte-character)
of the middle 1MB section of a file, so there is an upper limit in
time processing
original source: https://www.kennethghartman.com/calculate-file-entropy/
'''

from __future__ import division

__version__ = '0.2'
__description__ = 'Calculate Shannon Entropy for middle 1MB section of given file'

import os
import sys
import math

BLOCKSIZE=1024*1024

def main():
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            middle_entropy(filename,BLOCKSIZE)
    else:
        print("Usage: {} <filename>+".format(sys.argv[0]), file=sys.stderr)

def middle_entropy(filename,blocksize):
    print('Opening file {}...'.format(filename))
    
    # First, file size
    fileSize = os.stat(filename).st_size
    
    counts = dict.fromkeys(range(256),0)
    readSize = 0
    with open(filename, 'rb') as f:
        # Second, locate seek position
        if fileSize > blocksize:
            f.seek((fileSize - blocksize) // 2)
        
        byteArr = f.read(blocksize)
        readSize = len(byteArr)
        if readSize > 0:
            for byte in byteArr:
                counts[byte] += 1
    
    print()
    print('File size in bytes: {:,d}'.format(fileSize))
    # calculate the frequency of each byte value in the file
    print('Calculating Shannon entropy of middle {} bytes file. Please wait...'.format(readSize))
    freqList = []
    for b in range(256):
        ctr = counts[b]
        freqList.append(float(ctr) / readSize)
    # Shannon entropy
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    ent = -ent
    print('Shannon entropy for {}: {}'.format(filename,ent))
    print()


if __name__== "__main__":
    main()
