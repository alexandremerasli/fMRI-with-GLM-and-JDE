#import nipy
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from path_names import *
import os

# Loading file
print(INPUT_FOLDER)
contrib = nib.load(os.path.join(INPUT_FOLDER,'contrib.nii'))

data_contrib = contrib.get_fdata()
print('Shape before = ', data_contrib.shape)
data_contrib = data_contrib[:,:,:,0]
print('Shape after = ', data_contrib.shape)
data_contrib = np.where(data_contrib != 0, 1, 0)
mem = np.memmap(os.path.join(INPUT_FOLDER,"memmap_array"),dtype='float64', mode='w+', shape=data_contrib.shape)
mem[:] = data_contrib[:]
#print(mem[20,20:40,0])

'''
for i in range(6):
	plt.subplot(3,2,i)
	im = data_contrib[:, :, i]
	plt.imshow(im, cmap='gray', vmin = np.min(im), vmax = np.max(im))
	# print(im[20:40,20:40]) # Que des 0 et des 1 -> ok
plt.show()
# contrib = nib.Nifti1Image(data_contrib, affine = np.eye(4))
# contrib.fdata = data_contrib
m0 = nib.load('m0.nii')
m0.fdata = data_contrib
nib.save(m0, 'mask_parcel.nii')
'''

contrib3D = nib.Nifti1Image(mem,contrib.affine)
nib.save(contrib3D, os.path.join(INPUT_FOLDER,'mask_parcel.nii'))
#help(contrib4D.slicer)

'''
contrib4D = nib.load('contrib.nii')
contrib3D = contrib4D.slicer([:,:,:,0])
nib.save(contrib3D, 'mask_parcel.nii')


bold = nib.load('bold.nii')
data_bold = bold.get_fdata()
print(data_bold.shape)
'''