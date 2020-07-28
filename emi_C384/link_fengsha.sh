#!/bin/bash



f=../../../fengsha/bsmfv3
res='C384'
directory=`pwd`

for i in 01 02 03 04 05 06 07 08 09 10 11 12; do
    for t in tile1 tile2 tile3 tile4 tile5 tile6; do
	pushd ${directory}/${i}/${t}
	ln -sf ${f}/${res}/${i}/${t}/rdrag.dat .
	ln -sf ${f}/${res}/${i}/${t}/clay.dat .
	ln -sf ${f}/${res}/${i}/${t}/sand.dat .
	ln -sf ${f}/${res}/${i}/${t}/ssm.dat .
	ln -sf ${f}/${res}/${i}/${t}/uthr.dat .
	popd
    done
done

