#! /bin/tcsh -f
##$ -cwd
##$ -N Task_share 
##$ -m e
##$ -l h_rt=0:30:00
##$ -pe impi_hydra 1
##$ -S /bin/tcsh


#module swap pgi intel
setenv PATH ${PATH}:/pfs/scratch/dsam/SOLPS/RUNS/my_solps_ORNL
setenv PATH ${PATH}:/afs/ipp-garching.mpg.de/@sys/bin

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
setenv USE_EIRENE '-DUSE_EIRENE -DNEW_SIZE'
source /pfs/scratch/dsam/SOLPS/RUNS/my_solps_ORNL/setup.csh
#sbr
#cd $SIMPATH
cd $SIM_DIR
echo "In dir:" $PWD

cd base_from_96_36to48_36
set yt1 = 0
set b2ytval1 = 0
cp -r  /pfs/work/dsam/SOLPS_bin_DIIID/G_Run/base_from_96_36to48_36/* .
#Next 2 lines modified as ORNL version does not have b2.sputter_save.parameters &  b2.wall_save.parameters
cp ../../$INPUT_file2 ../b2.sputter_save.parameters_unused
cp ../../$INPUT_wall ../b2.wall_save.parameters_unused

touch b2ah.dat
touch b2ar.dat
touch b2ag.dat
touch b2fgmtry
touch b2fpardf
touch b2frates
touch b2mn.exe.dir
touch b2mn.prt
rm b2ai.prt b2ah.prt b2ar.prt

touch b2fstati
touch b2fstate
while($b2ytval1<1)
#	cp -r  /pfs/work/dsam/SOLPS_bin/G_Run/base_from_150_36/* .
	cp ../../$INPUT_file1 b2fstati
	cp ../../$INPUT_file1 b2fstate

	touch b2fstati
	touch b2fstate
	b2run  b2yt
        @ yt1 = $yt1 + 1
	if (-e b2fstatt) set b2ytval1 = 1
end
echo "big to small tried" $yt1 times



#if !(-e b2fstatt) echo "Re run b2yt"
#if !(-e b2fstatt) ../SOLPS_start_RedGrid.sh $SIMPATH $INPUT_file $OUTPUT_file



#Reduced size b2fstati for G run
cp b2fstatt ../b2fstati
##cp b2.sputter_save.parameters.2 ../b2.sputter_save.parameters
##cp b2.wall_save.parameters.2 ../b2.wall_save.parameters
#cp ../$INPUT_file b2fstati
cd ..
echo "b2fstati is updated"

rm *prt
b2run b2mn  < input.dat >! run_scr.log
#./conv_2d u_OP.txt u_OP1.txt conv.txt 39601 1.5E-6

echo "Done running solps. Now create bigger grid for fine run"
cp -r  /pfs/work/dsam/SOLPS_bin_DIIID/G_Run/base_from_48_36to96_36 .
cd base_from_48_36to96_36

set b2ytval2 = 0
set yt2 = 0
cp -r  /pfs/work/dsam/SOLPS_bin_DIIID/G_Run/base_from_48_36to96_36/* .
##cp ../b2.sputter_save.parameters .
##cp ../b2.wall_save.parameters .
touch b2ah.dat
touch b2ar.dat
touch b2ag.dat
touch b2fgmtry
touch b2fpardf
touch b2frates
touch b2mn.exe.dir
touch b2mn.prt
while($b2ytval2<1)
#	cp -r  /pfs/work/dsam/SOLPS_bin/G_Run/base_from_150_18/* .
	cp ../b2fstate b2fstati
	cp ../b2fstate b2fstate
	touch b2fstati
	touch b2fstate
	b2run  b2yt
	@ yt2 = $yt2 + 1
	if (-e b2fstatt) set b2ytval2 = 1
end
echo "small  to big tried" $yt2 times

cp b2fstatt ../../$OUTPUT_file1
#Following 2 lines modified as no b2.sputter_save.parameters & b2.wall_save.parameters for DIIID
cp ../b2.sputter_save.parameters_unused ../../$OUTPUT_file2
cp ../b2.wall_save.parameters_unused ../../$OUTPUT_wall
cd ..


##mv b2fstate ../b2fstate$SIMPATH
#mv b2fstate ../$OUTPUT_file
mv b2time.nc ../b2time_coarse.$SIMPATH.nc
#rm b2fstati
cd ..

