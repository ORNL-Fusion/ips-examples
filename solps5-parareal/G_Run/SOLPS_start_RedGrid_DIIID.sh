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

cp SOLPS2_RedGrid_V2.sh $SIMPATH/.

cd $SIMPATH
if !(-e ../baserun) echo "Create baserun"
if !(-e ../baserun) setenv FILE 1
if !(-e ../baserun) mkdir -p ../baserun
if ($FILE == 1) cp -r  /pfs/work/dsam/SOLPS_bin_DIIID/G_Run/baserun_G48_36/* ../baserun/ 
setenv FILE 0
#mkdir -p creates dir only if it doesn not exist.
#mkdir -p ../baserun
#cp -r  /pfs/work/dsam/SOLPS_bin/G_Run/baserun/* ../baserun/ 
cp -r /pfs/work/dsam/SOLPS_bin_DIIID/G_Run/Grun_files_G48_36_DIIID/* .
#rm *log ds* *prt* b2a*dat f* g* s* b2*.nc *.eps
rm  g*


#Create reduced grid b2fstati by using b2yt - 1st: create dir. Then-setup files(in following script). Then run b2run b2yt
cp -r  /pfs/work/dsam/SOLPS_bin_DIIID/G_Run/base_from_96_36to48_36 .

pwd


##Now, go back to $SIMPATH dir
./SOLPS2_RedGrid_V2.sh


