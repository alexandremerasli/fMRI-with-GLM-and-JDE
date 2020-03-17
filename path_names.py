import nibabel as nib
import os

def create_directory(path):
    """Create a new directory if it does not exist.
    
    Parameters
    ----------
    path : str
        Path of the new directory.

    Examples
    --------
    >>> create_directory('/home/jariasal/scipy_notebook/data')
        
    """
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

subject = 'S01'

# Directory where input files are
INPUT_FOLDER=os.path.abspath(os.path.join(os.getcwd(),'./input'))
create_directory(INPUT_FOLDER)

# Directory where output files will be
OUTPUT_FOLDER=os.path.abspath(os.path.join(os.getcwd(),'./output'))
create_directory(OUTPUT_FOLDER)

# Directory where the output of PyHRF will be saved
PYHRF_OUTPUT = os.path.abspath(os.path.join(OUTPUT_FOLDER, subject, 'pyhrf_output'))
create_directory(PYHRF_OUTPUT)

# Directory where figures will be saved
FIGURES_OUTPUT = os.path.abspath(os.path.join(OUTPUT_FOLDER, subject, 'figures'))
create_directory(FIGURES_OUTPUT)