# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:05:01 2016

@author: Gadsby
"""

import os

from test_PyDNA import test_pydna

from test_PyInteration import test_pyinteration

from test_PyPretreat import test_pypretreat

from test_PyGetMol import test_pygetmol

from test_PyMolecule import test_pymolecule

from test_PyProtein import test_pyprotein

def test_pybiomed():
    
    test_pydna()
    
    test_pyinteration()
    
    test_pypretreat()
    
    test_pygetmol()
    
    test_pymolecule()
    
    test_pyprotein()
    

if __name__ == '__main__':
    test_pybiomed()





