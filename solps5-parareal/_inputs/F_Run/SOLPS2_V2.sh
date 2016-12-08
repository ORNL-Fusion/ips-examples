#! /bin/tcsh -f
##$ -cwd
##$ -N Task_share 
##$ -m e
##$ -l h_rt=4:30:00
##$ -pe impi_hydra 1
##$ -S /bin/tcsh


#module swap pgi intel
#setenv PATH ${PATH}:/pfs/scratch/dsam/SOLPS/RUNS/my_solps_ORNL
#setenv PATH ${PATH}:/afs/ipp-garching.mpg.de/@sys/bin

#set SIMPATH=$1

echo "$SIMPATH"
#echo $1
#echo $SIMPATH

set SIM_DIR=$PWD
if (-e SOLPSTOP) then
  pushd `cat SOLPSTOP`
else
  pushd `echo $PWD | sed 's:/src/.*::'`
endif

pushd $SOLPS5_SOURCE_DIR
source setup.csh
popd

#sbr
#cd $SIMPATH
cd $SIM_DIR
echo "In dir:" $PWD

cp ../$INPUT_file1 b2fstati
cp ../$INPUT_file2 b2.sputter_save.parameters_unused
cp ../$INPUT_wall b2.wall_save.parameters_unused
#cp b2fstate b2fstati
echo "cp ../"$INPUT_file1 "b2fstati"
echo "b2fstati is updated"
b2run b2mn < input.dat >! run_scr.log
#./conv_2d u_OP.txt u_OP1.txt conv.txt 39601 1.5E-6

echo "Done running solps. Now copy files"
#cp b2fstate ../b2fstate$SIMPATH
mv b2fstate ../$OUTPUT_file1
mv b2.sputter_save.parameters_unused ../$OUTPUT_file2
mv b2.wall_save.parameters_unused ../$OUTPUT_wall
mv b2time.nc ../b2time_fine.$SIMPATH.nc
rm b2fstati
cd ..

