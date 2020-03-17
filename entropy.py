#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''
Calculate Shannon Entropy (min bits per byte-character)
original source: https://www.kennethghartman.com/calculate-file-entropy/
'''

__version__ = '0.2'
__description__ = 'Calculate Shannon Entropy for given file'

import sys
import math

BLOCKSIZE=1024*1024

def main():
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            entropy(filename,BLOCKSIZE)

def entropy(filename,blocksize):
    print('Opening file {}...'.format(filename))
    counts = dict.fromkeys(range(256),0)
    with open(filename, 'rb') as f:
        byteArr = f.read(blocksize)
        fileSize = 0
        while len(byteArr) > 0:
            fileSize += len(byteArr)
            for byte in byteArr:
                counts[byte] += 1
            
            byteArr = f.read(blocksize)
    
    print
    print('File size in bytes: {:,d}'.format(fileSize))
    # calculate the frequency of each byte value in the file
    print('Calculating Shannon entropy of file. Please wait...')
    freqList = []
    for b in range(256):
        ctr = counts[b]
        freqList.append(float(ctr) / fileSize)
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
