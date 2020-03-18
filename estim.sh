#!/bin/bash


## Variables

TR=2.76

# Estimate the HRF
ESTIMATE_HRF=True

# Zero constraint 
ZERO_CONSTRAINT=True

# Time length of the HRF (in seconds, default: 25.0)
#HRF_DURATION=27.6
HRF_DURATION=25

# Time resolution of the HRF
#DT=$((TR/2.0))
#DT=1.38
DT=0.69

HRF_HYPERPRIOR=1000 #100000

BETA=1.0

SIGMA_H=0.1

# Drifts type ('poly', 'cos')
DRIFT_TYPE='cos'  # poly

SUBJECT='S01'
# Files
INPUT_FOLDER='input'
PARCELLATION_MASK="${INPUT_FOLDER}/mask_parcel.nii"
PARADIGM_FILE="${INPUT_FOLDER}/signal_stim.csv"
BOLD_FILE="${INPUT_FOLDER}/bold.nii"
OUTPUT_FOLDER='output'

## Run jde estimation
pyhrf_jde_vem_analysis $TR $PARCELLATION_MASK $PARADIGM_FILE $BOLD_FILE -o "${OUTPUT_FOLDER}/${SUBJECT}/pyhrf_output" -d $DT -l $HRF_DURATION 
#--beta $BETA --hrf-hyperprior $HRF_HYPERPRIOR --sigma-h $SIGMA_H --drifts-type $DRIFT_TYPE --estimate-hrf --zero-constraint