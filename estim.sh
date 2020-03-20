#!/bin/bash


## Variables

TR=2.76

# Estimate the HRF
ESTIMATE_HRF=True

# Zero constraint (enforce first and last point of the HRF to zero)
ZERO_CONSTRAINT=True

# Time length of the HRF (in seconds, default: 25.0)
#HRF_DURATION=27.6
HRF_DURATION=25.0

# Time resolution of the HRF
#DT=$((TR/2.0))
#DT=1.38
DT=0.69

# To enforce smoothness for the temporal response
HRF_HYPERPRIOR=1000 #100000

# Spatial correlation parameter
BETA=1.0

# HRF prior variance init
SIGMA_H=0.1

# Drifts type ('poly', 'cos')
DRIFT_TYPE='cos'  # poly

SUBJECT='notebook'
#SUBJECT='simu'
#SUBJECT='S01'

# Files
INPUT_FOLDER='notebook_data'
#INPUT_FOLDER='simulated_data'
#INPUT_FOLDER='real_data'

PARCELLATION_MASK="${INPUT_FOLDER}/mask_parcel.nii"
PARADIGM_FILE="${INPUT_FOLDER}/signal_stim.csv"
BOLD_FILE="${INPUT_FOLDER}/bold.nii"
OUTPUT_FOLDER='output'

## Run jde estimation
if $ESTIMATE_HRF
then
	if $ZERO_CONSTRAINT
	then
		pyhrf_jde_vem_analysis $TR $PARCELLATION_MASK $PARADIGM_FILE $BOLD_FILE -o "${OUTPUT_FOLDER}/${SUBJECT}/pyhrf_output" -d $DT -l $HRF_DURATION --beta $BETA --hrf-hyperprior $HRF_HYPERPRIOR --sigma-h $SIGMA_H --drifts-type $DRIFT_TYPE --estimate-hrf --zero-constraint
	else
		pyhrf_jde_vem_analysis $TR $PARCELLATION_MASK $PARADIGM_FILE $BOLD_FILE -o "${OUTPUT_FOLDER}/${SUBJECT}/pyhrf_output" -d $DT -l $HRF_DURATION --beta $BETA --hrf-hyperprior $HRF_HYPERPRIOR --sigma-h $SIGMA_H --drifts-type $DRIFT_TYPE --estimate-hrf --no-zero-constraint
	fi
else
	pyhrf_jde_vem_analysis $TR $PARCELLATION_MASK $PARADIGM_FILE $BOLD_FILE -o "${OUTPUT_FOLDER}/${SUBJECT}/pyhrf_output" -d $DT -l $HRF_DURATION --beta $BETA --hrf-hyperprior $HRF_HYPERPRIOR --sigma-h $SIGMA_H --drifts-type $DRIFT_TYPE --no-estimate-hrf
fi
