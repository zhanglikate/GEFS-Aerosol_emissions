#!/bin/bash



f=${PWD}/../fengsha/bsmfv3
directory=`pwd`

for i in 01 02 03 04 05 06 07 08 09 10 11 12; do
    for t in tile1 tile2 tile3 tile4 tile5 tile6; do
	pushd ${directory}/${i}/${t}
	ln -sf ${f}/${i}/${t}/rdrag.dat .
	ln -sf ${f}/${i}/${t}/clay.dat .
	ln -sf ${f}/${i}/${t}/sand.dat .
	ln -sf ${f}/${i}/${t}/ssm.dat .
	ln -sf ${f}/${i}/${t}/uthr.dat .
	popd
    done
done
