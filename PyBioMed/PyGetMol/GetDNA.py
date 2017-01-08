# -*- coding: utf-8 -*-
"""

This module is used for downloading the DNA sequence from ncbi web. You can only 

need input a DNA ID.


Authors: Zhijiang Yao and Dongsheng Cao.

Date: 2016.11.04

Email: gadsby@163.com

"""


import urllib
import sys

ALPHABET = 'ACGT'

class Seq:
    def __init__(self, name, seq, no):
        self.name = name
        self.seq = seq.upper()
        self.no = no
        self.length = len(seq)

    def __str__(self):
        """Output seq when 'print' method is called."""
        return "%s\tNo:%s\tlength:%s\n%s" % (self.name, str(self.no), str(self.length), self.seq)

def GetDNAFromUniGene(SeqID = ''):
    
    '''
    This module is used for downloading the DNA sequence from ncbi web. You can only 

    need input a DNA ID.
    
    '''
    url = 'http://www.ebi.ac.uk/ena/data/view/{0}&display=fasta'.format(SeqID)
    temp = urllib.urlopen(url).read()    
    return temp

def IsUnderAlphabet(s, alphabet):
    """
    #################################################################
    Judge the string is within the scope of the alphabet or not.

    :param s: The string.
    :param alphabet: alphabet.

    Return True or the error character.
    #################################################################
    """
    for e in s:
        if e not in alphabet:
            return e

    return True	

def IsFasta(seq):
    """
    #################################################################
    Judge the Seq object is in FASTA format.
    Two situation:
    1. No seq name.
    2. Seq name is illegal.
    3. No sequence.

    :param seq: Seq object.
    #################################################################
    """
    if not seq.name:
        error_info = 'Error, sequence ' + str(seq.no) + ' has no sequence name.'
        print(seq)
        sys.stderr.write(error_info)
        return False
    if -1 != seq.name.find('>'):
        error_info = 'Error, sequence ' + str(seq.no) + ' name has > character.'
        sys.stderr.write(error_info)
        return False
    if 0 == seq.length:
        error_info = 'Error, sequence ' + str(seq.no) + ' is null.'
        sys.stderr.write(error_info)
        return False

    return True

def ReadFasta(f):
    """
    #################################################################
    Read a fasta file.

    :param f: HANDLE to input. e.g. sys.stdin, or open(<file>)

    Return Seq obj list.
    #################################################################
    """
    name, seq = '', ''
    count = 0
    seq_list = []
    lines = f.readlines()
    for line in lines:
        if not line:
            break

        if '>' == line[0]:
            if 0 != count or (0 == count and seq != ''):
                if IsFasta(Seq(name, seq, count)):
                    seq_list.append(seq)
                else:
                    sys.exit(0)

            seq = ''
            name = line[1:].strip()
            count += 1
        else:
            seq += line.strip()

    count += 1
    if IsFasta(Seq(name, seq, count)):
        seq_list.append(seq)
    else:
        sys.exit(0)

    return seq_list



if __name__ == '__main__':
    seqid = 'AA954964'
    seqid2 = 'CB216422'
    print GetDNAFromUniGene(seqid)
    dna = ReadFasta(open('D:/PyBioMed/PyBioMed/PyBioMed/test/test_data/example.fasta'))


