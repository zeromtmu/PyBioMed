# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:07:23 2016

@author: Gadsby
"""
import os

import string

from PyBioMed.PyGetMol.GetDNA import GetDNAFromUniGene

from PyBioMed.PyGetMol.GetProtein import GetSeqFromPDB
from PyBioMed.PyGetMol.GetProtein import GetPDB

from PyBioMed.PyGetMol.Getmol import ReadMolFromSDF
from PyBioMed.PyGetMol.Getmol import ReadMolFromMOL
from PyBioMed.PyGetMol.Getmol import ReadMolFromSmile
from PyBioMed.PyGetMol.Getmol import GetMolFromCAS
from PyBioMed.PyGetMol.Getmol import GetMolFromNCBI
from PyBioMed.PyGetMol.Getmol import GetMolFromDrugbank
from PyBioMed.PyGetMol.Getmol import GetMolFromKegg



def test_pygetmol():
    #==============================================================================
    # GetDNA
    #==============================================================================
    seqid = 'AA954964'
    seqid2 = 'CB216422'
    try:
        sequence1 = GetDNAFromUniGene(seqid)
        sequence2 = GetDNAFromUniGene(seqid2)
        
        print sequence1
        print sequence2
    except:
        print "Can't visit the internet"    
    #==============================================================================
    # Get protein
    #==============================================================================
    try:
        GetPDB(['1atp','1efz','1f88'])
        
        seq = GetSeqFromPDB('1atp.pdb')
        print seq
        
        seq2 = GetSeqFromPDB('1efz.pdb')
        print seq2
        
        seq3 = GetSeqFromPDB('1f88.pdb')
        print seq3
    except:
        print "Can't visit the internet"
    #==============================================================================
    # Get molecule
    #==============================================================================
    print "Downloading......"
    try:
        temp=GetMolFromCAS(casid="50-12-4")
        print temp
        temp=GetMolFromNCBI(cid="2244")
        print temp
        temp=GetMolFromDrugbank(dbid="DB00133")
        print temp
        temp=GetMolFromKegg(kid="D02176")
        print temp
    except:
        print "Can't visit the internet"
        
#    temp = ReadMolFromSDF("test_data/drug.sdf")
#    print temp
#    temp = ReadMolFromMOL("test_data/drug.mol")
#    print temp
#    temp = ReadMolFromSmile("test_data/drug.smi")
#    print temp
    


if __name__ == '__main__':
    test_pygetmol()









