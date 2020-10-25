# Brief description
A TORIC stand alone example that runs TORIC in the IPS using standard TORIC input files.
It does not require use of the plasma state.  The required input files are: equidt.data 
equigs.data and torica.inp, contained in the directory _input/toric_input/


The example is taken from an ITER simulation done several years ago by Francesca Poli in 
conjunction with TSC.  The case is the same as that provided in TORIC_ITER_TSC_example/.
However that example uses the full rf_toric_abr_mcmd.py wrapper component, which does 
make use of the Plasma State system.  This example uses a much simpler TORIC python wrapper
TORIC_basic_component.py.
