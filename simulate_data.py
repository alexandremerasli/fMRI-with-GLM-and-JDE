import numpy as np
from pyhrf.ndarray import xndarray
from pyhrf.tools import Pipeline
import os
import csv
from path_names import SIMULATED_INPUT_FOLDER

# Functions used to generate items in the Simulation Pipeline
def generate_rls(spatial_shape, mean_rls,var_rls):
	rls =np.random.randn(*spatial_shape) *	var_rls**.5 +mean_rls
	return xndarray(rls, ['axial','sagittal', 'coronal'])

def generate_noise(stim_induced_signal,noise_var):
	noise =np.random.randn(*stim_induced_signal.data.shape) * noise_var**.5
	return xndarray.xndarray_like(stim_induced_signal, data=noise)

def create_stim_induced_signal(rasteRed_paradigm, hrf,response_levels):
	signal =np.convolve(rasteRed_paradigm,hrf)[np.newaxis,:] * response_levels.data[:,:,:,np.newaxis]
	return xndarray(signal, response_levels.axes_names +['time'])

def create_bold(stim_induced_signal, noise):
	return stim_induced_signal + noise


amplitude = np.array([0,0,1,0,0,0,1,0,0,0,1]);

# Definition of the simulation pipeline
simulation_steps ={
'spatial_shape' : (10,11,12), 'mean_rls' :
3., 'var_rls' : 0.5,
'response_levels' : generate_rls,
'rasteRed_paradigm' : amplitude,
'hrf' : np.array([0,.5,1,0.5,0.,0]),
'noise_var' : 1.,
'noise' : generate_noise,
'stim_induced_signal' : create_stim_induced_signal,
'bold' : create_bold,
}

simulation =Pipeline(simulation_steps)

# Computation of all quantities in the pipeline and data saving
simulation.resolve()
simulation_items =simulation.get_values()
#simulation_items['response_levels'].save(os.path.join(SIMULATED_INPUT_FOLDER,'mask_parcel.nii'))
simulation_items['stim_induced_signal'].save(os.path.join(SIMULATED_INPUT_FOLDER,'mask_parcel.nii'))
simulation_items['bold'].save(os.path.join(SIMULATED_INPUT_FOLDER,'bold.nii'))
# Save a file contrib.nii to create the mask with seuillage_contrib.py
simulation_items['bold'].save(os.path.join(SIMULATED_INPUT_FOLDER,'contrib.nii'))

# Writing paradigm in csv file

row_csv = []
for i in range(len(amplitude)):
    row_csv.append([1, "exp", 1.38, 2.76, float(amplitude[i])]) # First column is session, second is type of experiment, third is time, 
                                                               # Fourth is each stimulus duration, fifth is amplitude of stimulus (0 or 1)


with open(os.path.join(SIMULATED_INPUT_FOLDER,'signal_stim.csv'), 'w') as File:
    writer = csv.writer(File)
    writer.writerows(row_csv)