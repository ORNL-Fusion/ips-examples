# Brief description
The TORIC_ITER_TSC_example uses the full `rf_toric_abr_mcmd.py` wrapper component, which
makes use of the Plasma State system.  That is it obtains plasma profile data from a plasma 
state file, updates, a template toric input file with current plasma data, runs toric 
with the updated input file, then processes the toric output file to update the plasma state 
file with the new rf data. This is the standard TORIC IPS component that has been used 
extensively in the past.  The input files are in the Cori AToM installation, i.e. 
`$ATOM/examples_input_data/TORIC_ITER_TSC_example`, where 
`$ATOM=/global/common/software/atom/cori`.  

