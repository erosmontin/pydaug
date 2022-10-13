import ctypes
import os
from pynico_eros_montin import pynico as me



def dAugIt(im,r,j,imo=None,ro=None,tmp=None):
    handle = ctypes.CDLL("bld/libdaug.so")
    handle.main.argtypes =[ctypes.c_int,ctypes.POINTER(ctypes.c_char_p)]
    if not tmp:
        tmp=''
        P = me.PathableTemp
    else:
        P = me.Pathable
    
    if not imo:
        imo=P(os.path.join(tmp,'o.nii.gz')).changeBaseNameWithoutExtensionRandom().getPosition()
    if not ro:
        ro = P(os.path.join(tmp,'o.nii.gz')).changeBaseNameWithoutExtensionRandom().getPosition()

    args=(ctypes.c_char_p*6)(b'dAug',im.encode(),r.encode(),imo.encode(),ro.encode(),j.encode())
    handle.main(len(args),args) 
    return  imo, ro

if __name__=="__main__":
    im='/data/PROJECTS/HIPSEGENTATION/meshing/meshtoimage/a.nii.gz'
    r='/data/PROJECTS/HIPSEGENTATION/meshing/meshtoimage/b.nii.gz'
    imo='/data/PROJECTS/HIPSEGENTATION/meshing/meshtoimage/_a.nii.gz'
    ro='/data/PROJECTS/HIPSEGENTATION/meshing/meshtoimage/_b.nii.gz'
    j='/data/PROJECTS/HIPSEGENTATION/meshing/meshtoimage/c.txt'
    print(dAugIt(im,r,j))
