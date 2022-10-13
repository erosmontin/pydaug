
from pydaug_eros_montin import pydaug as daug

im='../data/a.nii.gz'
r='../data/b.nii.gz'
imo='../data/_a.nii.gz'
ro='../data/_b.nii.gz'
j='../data/c.txt'
print(daug.dAugIt(im,r,j))

