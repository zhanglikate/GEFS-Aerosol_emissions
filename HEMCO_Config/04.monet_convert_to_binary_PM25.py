#!/usr/bin/env python
import monet
import xarray
from monetio import prepchem as pc

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201901010000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201901010000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201901010000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201901010000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201901010000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201901010000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201902010000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201902010000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201902010000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201902010000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201902010000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201902010000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/01/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201903040000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/02/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201903040000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/02/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201903040000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/02/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201903040000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/02/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201903040000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/02/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201903040000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/02/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201904040000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/03/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201904040000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/03/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201904040000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/03/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201904040000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/03/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201904040000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/03/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201904040000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/03/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201905050000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/04/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201905050000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/04/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201905050000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/04/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201905050000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/04/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201905050000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/04/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201905050000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/04/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201906050000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/05/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201906050000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/05/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201906050000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/05/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201906050000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/05/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201906050000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/05/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201906050000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/05/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201907060000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/06/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201907060000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/06/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201907060000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/06/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201907060000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/06/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201907060000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/06/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201907060000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/06/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201908060000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/07/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201908060000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/07/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201908060000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/07/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201908060000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/07/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201908060000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/07/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201908060000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/07/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201909060000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/08/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201909060000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/08/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201909060000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/08/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201909060000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/08/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201909060000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/08/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201909060000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/08/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201910070000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/09/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201910070000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/09/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201910070000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/09/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201910070000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/09/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201910070000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/09/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201910070000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/09/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201911070000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/10/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201911070000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/10/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201911070000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/10/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201911070000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/10/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201911070000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/10/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201911070000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/10/tile6/e_pm25.dat')

f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201912080000_tile1_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/11/tile1/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201912080000_tile2_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/11/tile2/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201912080000_tile3_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/11/tile3/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201912080000_tile4_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/11/tile4/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201912080000_tile5_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/11/tile5/e_pm25.dat')
f=xarray.open_dataset("output/regrid/HEMCO_sa.diagnostics.201912080000_tile6_convert.nc")
pc.to_prepchem_binary(f.PM25_FV3,'output/fv3_chem/11/tile6/e_pm25.dat')

