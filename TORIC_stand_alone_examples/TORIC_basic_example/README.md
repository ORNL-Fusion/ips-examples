# Brief description
TORIC_basic_example runs TORIC using a set of input files located in *_inputs/toric_input*
directory.  The component python wrapper is a stripped down version called TORIC_basic_component.py
which simply stages the input files to the toric work directory, launches the TORIC code,
and stages the output files to the simulation_results directory.  It does not couple to the
Plasma State system or process the input or output files. The required input files are: 
equidt.data equigs.data and torica.inp.


The example is taken from an ITER simulation done several years ago by Francesca Poli in 
conjunction with TSC.  The case is the same as that provided in *TORIC_ITER_TSC_example*.
However that example uses the full rf_toric_abr_mcmd.py wrapper component, which does 
make use of the Plasma State system.  The much simpler python wrapper TORIC_basic_component.py 
used here could be useful as is when the user has the toric input files in hand and makes 
direct use of the output files.
