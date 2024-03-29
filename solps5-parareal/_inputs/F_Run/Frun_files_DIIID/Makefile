# GNU Makefile for B2.5; part 2--execution.
# Please see the general comments in the companion Makefile, part 1,
# which controls compile and load.
#-----------------------------------------------------------------------
# Variables.

SHELL = /bin/sh
TIME = time
OBJDIR = ${SOLPSTOP}/src/Braams/b2/base/${OBJECTCODE}
nil =
ifeq (${OBJECTCODE},linux_nag_f95.debug)
DBX = totalview
INC = 
else
ifeq (${OBJECTCODE},linux.Fujitsu.debug)
DBX = totalview
INC =
else 
ifeq (${OBJECTCODE},linux_pgf90.debug)
DBX = totalview
INC = 
else
ifeq (${OBJECTCODE},linux.ifort64.debug)
DBX = totalview
INC = 
else
DBX = dbx
ifdef USE_EIRENE
INC = -I ${OBJDIR} -I ${SOLPSTOP}/src/Eirene/${OBJECTCODE}
else
INC = -I ${OBJDIR}
endif
endif
endif
endif
endif

prints = b2ag.prt b2ah.prt b2ai.prt b2ar.prt b2mn.prt \
 b2yg.prt b2yh.prt b2yi.prt b2ym.prt b2yn.prt b2yp.prt b2yq.prt \
 b2yr.prt b2yt.prt b2yi_gnuplot.prt

target_ag = b2ag.prt b2fgmtry fort.30
target_ah = b2ah.prt b2fpardf
target_ai = b2ai.prt b2fstati
target_ar = b2ar.prt b2frates
ifdef USE_EIRENE
target_mn = b2mn.prt b2fparam b2fstate b2fmovie b2ftrace b2ftrack b2fplasma b2time.nc fort.31 fort.44 b2tallies.nc b2movies.nc b2wall.nc
else
target_mn = b2mn.prt b2fparam b2fstate b2fmovie b2ftrace b2ftrack b2fplasma b2time.nc b2tallies.nc b2movies.nc b2wall.nc
endif
target_co = b2co.prt
target_uf = b2uf.prt
target_fu = b2fu.prt
target_pl = b2pl.prt b2plot.ps
target_ts = b2ts.prt
target_yg = b2yg.prt b2yg.plt
target_yh = b2yh.prt
target_yi = b2yi.prt b2yi.plt
target_yi_gnuplot = b2yi_gnuplot.prt
target_ym = b2ym.prt b2ym.plt
target_yn = b2yn.prt b2yn.plt
target_yp = b2yp.prt b2yp.plt b2specp
target_yq = b2yq.prt b2yq.plt
target_yr = b2yr.prt b2yr.plt
target_yt = b2yt.prt b2fstatt b2mn.dat.2 b2ah.dat.2 b2ai.dat.2
target_xd = B2SXDR
target_rd = b2rd.prt

scandir := $(shell cd .. ; pwd)
projdir := $(shell cd ../.. ; pwd)
baserundir := $(shell cd $(scandir)/baserun ; pwd)
savefiles := $(shell echo ${PLASMASTATE} | sed -e 's:plasmastate:b2.*_save.parameters:')

echo:
	@echo scandir=${scandir} projdir=${projdir} baserundir=${baserundir} savefiles=${savefiles}

#-----------------------------------------------------------------------
# Directives.

vpath %.dat .:$(baserundir)
vpath b2fgmtry .:$(baserundir)
vpath b2fpardf .:$(baserundir)
vpath b2fstati .:$(baserundir)
vpath b2frates .:$(baserundir)
vpath fort.30 .:$(baserundir)

#-----------------------------------------------------------------------
# Rules.

default : b2mn.prt
all : $(prints)
prt : $(prints)

.PHONY : default all prt clean realclean testvars
.PRECIOUS : $(prints)
.SUFFIXES : $(nil)

$(target_xd) : b2fgmtry b2fparam b2fstate b2fplasma
	rm -rf b2xd.exe.dir ; mkdir b2xd.exe.dir ; cp $^ b2xd.exe.dir
	rm -f $(target_xd)
	cd b2xd.exe.dir ; ${TIME} ${OBJDIR}/b2xd.exe ; mv $(target_xd) .. ; rm -f $(notdir $^)
	-rmdir b2xd.exe.dir

$(target_ag) : b2ag.dat
	rm -rf b2ag.exe.dir ; mkdir b2ag.exe.dir ; cp $^ b2ag.exe.dir
	rm -f $(target_ag)
	cd b2ag.exe.dir ; ${TIME} ${OBJDIR}/b2ag.exe ; mv $(target_ag) .. ; rm -f $(notdir $^)
	-rmdir b2ag.exe.dir

$(target_ah) : b2ah.dat b2fgmtry
	rm -rf b2ah.exe.dir ; mkdir b2ah.exe.dir ; cp $^ b2ah.exe.dir
	rm -f $(target_ah)
	cd b2ah.exe.dir ; ${TIME} ${OBJDIR}/b2ah.exe ; mv $(target_ah) .. ; rm -f $(notdir $^)
	-rmdir b2ah.exe.dir

$(target_ai) : b2ag.dat b2ai.dat b2fgmtry
	rm -rf b2ai.exe.dir ; mkdir b2ai.exe.dir ; cp $^ b2ai.exe.dir
	rm -f $(target_ai)
	cd b2ai.exe.dir ; ${TIME} ${OBJDIR}/b2ai.exe ; mv $(target_ai) .. ; rm -f $(notdir $^)
	-rmdir b2ai.exe.dir

$(target_ar) : b2ar.dat stra.dat weis.dat b2fpardf b2fgmtry
	rm -rf b2ar.exe.dir ; mkdir b2ar.exe.dir ; cp $^ b2ar.exe.dir
	rm -f $(target_ar)
	cd b2ar.exe.dir ; ${TIME} ${OBJDIR}/b2ar.exe ; mv $(target_ar) .. ; rm -f $(notdir $^)
	-rmdir b2ar.exe.dir

$(target_mn) : b2mn.dat b2fgmtry b2fpardf b2fstati b2frates fort.30
ifdef OMP_NUM_THREADS
	@echo OMP_NUM_THREADS=${OMP_NUM_THREADS}
endif
	rm -rf b2mn.exe.dir ; mkdir b2mn.exe.dir ; cp $^ b2mn.exe.dir
	rm -f $(target_mn)
ifdef USE_EIRENE
	-cd b2mn.exe.dir ; ln -s ../HYDHEL ../AMJUEL ../METHANE ../SPUTER ../H2VIBR ../fort.21 ../fort.22 ../input.dat . ; [ -e ../fort.15 ] && cp -p ../fort.15 .
endif
ifdef USE_IMPGYRO
	cd b2mn.exe.dir ; mkdir tracing ; \
	touch use_impgyro ; [ -e ../restart_ext ] && cp ../restart_ext . ; \
	mpiexec -f ${MACH_FILE} \
	-n ${NPE_B2} -wdir ${WD_B2}/b2mn.exe.dir ${OBJDIR}/b2mn.exe : \
	-n ${NPE_IG} -wdir ${WD_IG} ${EXE_IG} ; \
	mv $(target_mn) .. ; mv tracing/* ../tracing ; \
	rm -f $(notdir $^) .quit ; rm -f use_impgyro
else
	cd b2mn.exe.dir ; mkdir tracing ; ${TIME} ${OBJDIR}/b2mn.exe ; mv $(target_mn) .. ; mv tracing/* ../tracing ; rm -f $(notdir $^) .quit
endif
ifdef USE_EIRENE
	-mv b2mn.exe.dir/fort.15 b2mn.exe.dir/fort.31 b2mn.exe.dir/fort.44 .
endif
	[ -e b2mn.exe.dir/tran ] && mv b2mn.exe.dir/tran b2mn.exe.dir/tran?? .
	-rmdir b2mn.exe.dir

dbx.b2mn : b2mn.dat b2fgmtry b2fpardf b2fstati b2frates fort.30
	rm -rf b2mn.exe.dir ; mkdir b2mn.exe.dir ; cp $^ b2mn.exe.dir
ifdef USE_EIRENE
	-cd b2mn.exe.dir ; ln -s ../HYDHEL ../AMJUEL ../METHANE ../SPUTER ../H2VIBR ../fort.21 ../fort.22 ../input.dat . ; [ -e ../fort.15 ] && cp -p ../fort.15 .
	cd b2mn.exe.dir ; mkdir tracing ; ${DBX} ${INC} ${OBJDIR}/b2mn.exe ; mv tracing/* ../tracing ; rm -f $(notdir $^) .quit
	-mv b2mn.exe.dir/fort.15 b2mn.exe.dir/fort.31 b2mn.exe.dir/fort.44 .
else
	cd b2mn.exe.dir ; ${DBX} ${INC} ${OBJDIR}/b2mn.exe ; rm -f $(notdir $^) .quit
endif
	[ -e b2mn.exe.dir/tran ] && mv b2mn.exe.dir/tran b2mn.exe.dir/tran?? .
	-rmdir b2mn.exe.dir

$(target_co) : b2mn.dat b2fgmtry b2fpardf b2fstati ${PLASMASTATE} ${savefiles}
	-rm -rf b2co.exe.dir ; mkdir b2co.exe.dir ; cp $^ b2co.exe.dir
	rm -f $(target_co)
	cd b2co.exe.dir ; ${TIME} ${OBJDIR}/b2co.exe `basename ${PLASMASTATE}` ; mv $(target_co) b2fstate .. ; rm -f $(notdir $^) .quit
	-rmdir b2co.exe.dir

$(target_uf) : b2fgmtry b2fparam b2fstate b2fplasma
	rm -rf b2uf.exe.dir ; mkdir b2uf.exe.dir ; cp $^ b2uf.exe.dir
	rm -f $(target_uf)
	cd b2uf.exe.dir ; ${TIME} ${OBJDIR}/b2uf.exe ; mv $(target_uf) b2fplasmf .. ; rm -f $(notdir $^) .quit
	-rmdir b2uf.exe.dir

$(target_fu) : b2fgmtry b2fparam b2fstate b2fplasmf
	rm -rf b2fu.exe.dir ; mkdir b2fu.exe.dir ; cp $^ b2fu.exe.dir
	rm -f $(target_fu)
	cd b2fu.exe.dir ; ${TIME} ${OBJDIR}/b2fu.exe ; mv $(target_fu) b2fplasma .. ; rm -f $(notdir $^) .quit
	-rmdir b2fu.exe.dir

ifdef USE_EIRENE
$(target_pl) : b2mn.dat b2fgmtry b2fparam b2fstate b2fplasma b2frates fort.44
else
$(target_pl) : b2mn.dat b2fgmtry b2fparam b2fstate b2fplasma b2frates
endif
	rm -rf b2pl.exe.dir ; mkdir b2pl.exe.dir ; cp $^ b2pl.exe.dir
	rm -f $(target_pl)
	cd b2pl.exe.dir ; ${TIME} ${OBJDIR}/b2pl.exe ; mv $(target_pl) .. ; rm -f $(notdir $^) .quit
	-rmdir b2pl.exe.dir

$(target_rd) : shotnumber.history
	rm -rf b2rd.exe.dir ; mkdir b2rd.exe.dir ; cp $^ b2rd.exe.dir
	rm -f $(target_rd)
	cd b2rd.exe.dir ; ${TIME} ${OBJDIR}/b2rd.exe ; mv $(target_rd) b2fstate b2fgmtrt .. ; rm -f $(notdir $^)
	-rmdir b2rd.exe.dir

$(target_ts) : b2fparam b2fgmtry b2fpardf b2fstate b2fplasma
	rm -rf b2ts.exe.dir ; mkdir b2ts.exe.dir ; cp $^ b2ts.exe.dir
	rm -f $(target_ts)
	cd b2ts.exe.dir ; ${TIME} ${OBJDIR}/b2ts.exe ; mv $(target_ts) b2fstate .. ; rm -f $(notdir $^) .quit
	-rmdir b2ts.exe.dir

$(target_yg) : b2yg.dat b2fgmtry
	rm -rf b2yg.exe.dir ; mkdir b2yg.exe.dir ; cp $^ b2yg.exe.dir
	rm -f $(target_yg)
	NCARG_GKS_OUTPUT=b2yg.plt ; export NCARG_GKS_OUTPUT ;\
	cd b2yg.exe.dir ; ${TIME} ${OBJDIR}/b2yg.exe ; mv $(target_yg) .. ; rm -f $(notdir $^)
	-rmdir b2yg.exe.dir

$(target_yh) : b2yh.dat b2fparam b2fgmtry
	rm -rf b2yh.exe.dir ; mkdir b2yh.exe.dir ; cp $^ b2yh.exe.dir
	rm -f $(target_yh)
	NCARG_GKS_OUTPUT=b2yh.plt ; export NCARG_GKS_OUTPUT ;\
	cd b2yh.exe.dir ; ${TIME} time ${OBJDIR}/b2yh.exe ; mv $(target_yh) .. ; rm -f $(notdir $^)
	-rmdir b2yh.exe.dir

$(target_yi) : b2yi.dat b2mn.dat b2fstate b2frates b2fgmtry
	rm -rf b2yi.exe.dir ; mkdir b2yi.exe.dir ; cp $^ b2yi.exe.dir
	rm -f $(target_yi)
	NCARG_GKS_OUTPUT=b2yi.plt ; export NCARG_GKS_OUTPUT ;\
	cd b2yi.exe.dir ; ${TIME} ${OBJDIR}/b2yi.exe ; mv $(target_yi) .. ; rm -f $(notdir $^)
	-rmdir b2yi.exe.dir

$(target_yi_gnuplot) : b2mn.dat b2fstate b2frates b2fgmtry
	rm -rf b2yi_gnuplot.exe.dir ; mkdir b2yi_gnuplot.exe.dir ; cp $^ b2yi_gnuplot.exe.dir
	rm -f $(target_yi_gnuplot)
	cd b2yi_gnuplot.exe.dir ; ${TIME} ${OBJDIR}/b2yi_gnuplot.exe ; mv $(target_yi_gnuplot) .. ; rm -f $(notdir $^)
	-rmdir b2yi_gnuplot.exe.dir

$(target_ym) : b2ym.dat b2fmovie
	rm -rf b2ym.exe.dir ; mkdir b2ym.exe.dir ; cp $^ b2ym.exe.dir
	rm -f $(target_ym)
	NCARG_GKS_OUTPUT=b2ym.plt ; export NCARG_GKS_OUTPUT ;\
	cd b2ym.exe.dir ; ${TIME} ${OBJDIR}/b2ym.exe ; mv $(target_ym) .. ; rm -f $(notdir $^)
	-rmdir b2ym.exe.dir

$(target_yn) : b2yn.dat b2mn.dat b2ftrack b2frates b2fstate
	rm -rf b2yn.exe.dir ; mkdir b2yn.exe.dir ; cp $^ b2yn.exe.dir
	rm -f $(target_yn)
	NCARG_GKS_OUTPUT=b2yn.plt ; export NCARG_GKS_OUTPUT ;\
	cd b2yn.exe.dir ; ${TIME} ${OBJDIR}/b2yn.exe ; mv $(target_yn) .. ; rm -f $(notdir $^)
	-rmdir b2yn.exe.dir

$(target_yp) : b2yp.dat b2mn.dat b2fgmtry b2fparam b2fstate b2frates
	rm -rf b2yp.exe.dir ; mkdir b2yp.exe.dir ; cp $^ b2yp.exe.dir
	rm -f $(target_yp)
	NCARG_GKS_OUTPUT=b2yp.plt ; export NCARG_GKS_OUTPUT ;\
	cd b2yp.exe.dir ; ${TIME} ${OBJDIR}/b2yp.exe ; mv $(target_yp) .. ; rm -f $(notdir $^)
	-rmdir b2yp.exe.dir

$(target_yq) : b2yq.dat b2ftrace
	rm -rf b2yq.exe.dir ; mkdir b2yq.exe.dir ; cp $^ b2yq.exe.dir
	rm -f $(target_yq)
	NCARG_GKS_OUTPUT=b2yq.plt ; export NCARG_GKS_OUTPUT ;\
	cd b2yq.exe.dir ; ${TIME} ${OBJDIR}/b2yq.exe ; mv $(target_yq) .. ; rm -f $(notdir $^)
	-rmdir b2yq.exe.dir

$(target_yr) : b2yr.dat b2frates b2fpardf b2fgmtry
	rm -rf b2yr.exe.dir ; mkdir b2yr.exe.dir ; cp $^ b2yr.exe.dir
	rm -f $(target_yr)
	NCARG_GKS_OUTPUT=b2yr.plt ; export NCARG_GKS_OUTPUT ;\
	cd b2yr.exe.dir ; ${TIME} ${OBJDIR}/b2yr.exe ; mv $(target_yr) .. ; rm -f $(notdir $^)
	-rmdir b2yr.exe.dir

$(target_yt) : b2yt.dat b2fstate b2mn.dat b2ah.dat b2ai.dat b2ag.dat b2fgmtry b2frates b2fpardf
	rm -rf b2yt.exe.dir ; mkdir b2yt.exe.dir ; cp $^ b2yt.exe.dir
	rm -f $(target_yt)
ifdef USE_EIRENE
	-cd b2yt.exe.dir ; [ -e ../input.dat ] && ln -s ../input.dat .
	cd b2yt.exe.dir ; ${TIME} ${OBJDIR}/b2yt.exe ; mv $(target_yt) .. ; rm -f $(notdir $^) input.dat
	[ -e b2yt.exe.dir/input.dat.2 ] && mv b2yt.exe.dir/input.dat.2 .
else
	cd b2yt.exe.dir ; ${TIME} ${OBJDIR}/b2yt.exe ; mv $(target_yt) .. ; rm -f $(notdir $^)
endif
	-rmdir b2yt.exe.dir

dbx.b2yt : b2yt.dat b2fstate b2mn.dat b2ah.dat b2ai.dat b2ag.dat b2fgmtry b2frates b2fpardf
	rm -rf b2yt.exe.dir ; mkdir b2yt.exe.dir ; cp $^ b2yt.exe.dir
	rm -f $(target_yt)
ifdef USE_EIRENE
	-cd b2yt.exe.dir ; [ -e ../input.dat ] && ln -s ../input.dat .
	cd b2yt.exe.dir ; ${DBX} ${INC} ${OBJDIR}/b2yt.exe ; mv $(target_yt) .. ; rm -f $(notdir $^) input.dat
	[ -e b2yt.exe.dir/input.dat.2 ] && mv b2yt.exe.dir/input.dat.2 .
else
	cd b2yt.exe.dir ; ${DBX} ${INC} ${OBJDIR}/b2yt.exe ; mv $(target_yt) .. ; rm -f $(notdir $^)
endif
	-rmdir b2yt.exe.dir

stra.dat :
	ln -s ${SOLPSTOP}/data/stra.dat .

weis.dat :
	ln -s ${SOLPSTOP}/data/weis.dat .

$(savefiles):
	touch $(shell echo ${PLASMASTATE} | sed -e 's:plasmastate:b2.dummy_save.parameters:')
	$(eval savefiles := $(shell echo ${PLASMASTATE} | sed -e 's:plasmastate:b2.dummy_save.parameters:'))

clean :
	rm -f *.prt* *.plt* *~
	rm -rf *.exe.dir

realclean : clean
	rm -f b2fgmtry b2fpar* b2frates b2fstat* b2ftra* b2fmovie b2specp

# The target testvars is present only for testing purposes.
testvars :
	@echo SHELL : $(SHELL)
	@echo OBJECTCODE : $(OBJECTCODE)
	@echo PATH : $(PATH)
	@echo `which b2mn.exe`
	@echo scandir: $(scandir)
	@echo projdir: $(projdir)
	@echo baserundir: $(baserundir)
	@echo codedir: $(codedir)

help help.prt:
	@echo "Available targets are:"
	@echo "  ${target_ag} : "
	@echo "     produce the geometry information"
	@echo "  ${target_ah} : "
	@echo "     produce the default physics information"
	@echo "  ${target_ai} : "
	@echo "     produce the initial plasma state"
	@echo "  ${target_ar} : "
	@echo "     produce the atomic physics rate information"
	@echo "  ${target_mn} : "
	@echo "     run the main code"
	@echo "  ${target_co} : "
	@echo "     prepares a b2fstate file from a plasmastate file"
	@echo "  ${target_rd} : "
	@echo "     prepares a b2fstate file from a saved MDSPLUS archive"
	@echo "  ${target_uf} : "
	@echo "     converts an unformatted b2fplasma file to a formatted version"
	@echo "  ${target_fu} : "
	@echo "     converts a formatted b2fplasma file to an unformatted version"
	@echo "  ${target_pl} : "
	@echo "     runs b2plot"
	@echo "  ${target_ts} : "
	@echo "     runs a dummy example of a post-processor"
	@echo "  ${target_yg} : "
	@echo "     displays geometry and magnetic field"
	@echo "  ${target_yh} : "
	@echo "     displays the physics parameters"
	@echo "  ${target_yi} : "
	@echo "     displays the plasma state"
	@echo "  ${target_yi_gnuplot} : "
	@echo "     displays the plasma state vis gnuplot"
	@echo "  ${target_ym} : "
	@echo "     displays a movie [not tested]"
	@echo "  ${target_yn} : "
	@echo "     displays the progress of the inner b2 iterations"
	@echo "  ${target_yp} : "
	@echo "     displays the plasma state"
	@echo "  ${target_yq} : "
	@echo "     displays a quick display of the evolution data"
	@echo "  ${target_yr} : "
	@echo "     displays the atomic physics rates"
	@echo "  ${target_yt} : "
	@echo "     transfers the plasma state to a mesh of a different size"
	@echo "  ${target_xd} : "
	@echo "     converts the plasma state to a SOLPS4.0 B2SXDR file [no longer functional]"
