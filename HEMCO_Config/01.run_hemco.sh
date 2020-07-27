#!/bin/csh -f

#source hemco_run_netcdf

setenv ncpu 1
limit stacksize unlimited
#pushd /data/aqf/barryb/hemco_standalone_full
#make clean_hemco
#make -j4 all EXTRA_FLAGS="-traceback -g"
#popd
rm *.log
mpirun -np ${ncpu} ./hemco_standalone -c HEMCO_Config.rc >& hemco.log
