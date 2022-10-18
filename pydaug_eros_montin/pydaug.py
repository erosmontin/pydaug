import ctypes
import os
from pynico_eros_montin import pynico as pn



def dAugIt(im,r,j,imo=None,ro=None,tmp=None):
    basepath = os.path.dirname(os.path.abspath(__file__))
    handle = ctypes.CDLL(os.path.join(basepath,"bld/libdaug.so"))
    handle.main.argtypes =[ctypes.c_int,ctypes.POINTER(ctypes.c_char_p)]
        
    if not imo:
        imo=pn.createRandomTemporaryPathableFromFileName('a.nii.gz',tmp).getPosition()
    if not ro:
        ro =pn.createRandomTemporaryPathableFromFileName('a.nii.gz',tmp).getPosition()
    args=(ctypes.c_char_p*6)(b'dAug',im.encode(),r.encode(),imo.encode(),ro.encode(),j.encode())
    handle.main(len(args),args) 
    return  imo, ro


