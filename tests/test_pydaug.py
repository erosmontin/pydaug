
from pydaug_eros_montin import pydaug as daug

im='tests/data/a.nii.gz'
r='tests/data/b.nii.gz'
imo='tests/data/_a.nii.gz'
ro='tests/data/_b.nii.gz'
j='tests/data/c.txt'
print(daug.dAugIt(im,r,j))