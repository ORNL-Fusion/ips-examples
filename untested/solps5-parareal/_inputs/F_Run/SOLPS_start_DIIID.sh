#! /bin/tcsh -f
##$ -cwd
##$ -N Task_share 
##$ -m e
##$ -l h_rt=0:30:00
##$ -pe impi_hydra 1
##$ -S /bin/tcsh

#module swap pgi intel
#SIMPATH is self.suffix in python file
#INPUT_file is last b2fstate
#OUTPUT_file is b2fstate from current path
setenv SIMPATH $1
setenv INPUT_file1 $2
setenv OUTPUT_file1 $3
setenv INPUT_file2 $4
setenv OUTPUT_file2 $5
setenv INPUT_wall $6
setenv OUTPUT_wall $7

setenv FILE 0

#set SIMPATH=$1

echo "$SIMPATH"

mkdir $SIMPATH
cp SOLPS2_V2.sh $SIMPATH/.
cd $SIMPATH

if !(-e ../baserun) echo "create baserun"
if !(-e ../baserun) setenv FILE 1
if !(-e ../baserun) mkdir -p ../baserun
#mkdir -p creates dir only if it doesn not exist.
#mkdir -p ../baserun
echo $IPS_SOLPS_PARAREAL_SUBMITDIR
if ($FILE == 1) cp -r  $IPS_SOLPS_PARAREAL_SUBMITDIR/_inputs/F_Run/baserun/* ../baserun/ 
if ($FILE == 1) touch ../baserun/b2ag.dat
sleep 1
if ($FILE == 1) touch ../baserun/b2ag.prt
sleep 1
if ($FILE == 1) touch ../baserun/b2fgmtry
sleep 1
if ($FILE == 1) touch ../baserun/fort.30
sleep 1
if ($FILE == 1) touch ../baserun/fort.31
sleep 1
if ($FILE == 1) touch ../baserun/b2ah.dat
sleep 1
if ($FILE == 1) touch ../baserun/b2ah.prt
sleep 1
if ($FILE == 1) touch ../baserun/b2fpardf
sleep 1
if ($FILE == 1) touch ../baserun/b2ar.dat
sleep 1
if ($FILE == 1) touch ../baserun/b2ar.prt
sleep 1
if ($FILE == 1) touch ../baserun/b2frates
if ($FILE == 1) touch ../baserun/fort.44
sleep 1
if ($FILE == 1) touch ../baserun/b2ai.dat
sleep 1
if ($FILE == 1) touch ../baserun/b2ai.prt
sleep 1
if ($FILE == 1) touch ../baserun/b2fstati
sleep 1

setenv FILE 0

cp -rp $IPS_SOLPS_PARAREAL_SUBMITDIR/_inputs/F_Run/Frun_files_DIIID/* .
#rm *log ds* *prt* b2a*dat f* g* s* b2*.nc *.eps
rm  g*


./SOLPS2_V2.sh


