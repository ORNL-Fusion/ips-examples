set nolog x
set nolog y
set zero 1e-50
set time
set xlabel "time"
set ylabel ""
set title ".../b2/runs/DIII_Lmode/F_withb2fstatiD1_dt1E-6/b2mn.exe.dir"
plot \
"gnuplot.data" using 1:2 title "tesepm" with linespoints
pause 3600
