import numpy as np
import Ngl,Nio
#-- open file and read variables
f = Nio.open_file("/mnt/e/SYSU/data/NCEP/air.mon.mean.nc", "r")
var = f.variables["air"][0,0,:,:]
lat = f.variables["lat"][:]
lon = f.variables["lon"][:]
wks = Ngl.open_wks("png","/mnt/e/SYSU/p_py")
#-- resource settings
res = Ngl.Resources()
res.nglFrame = False
res.cnFillOn = True
res.cnFillPalette = "NCL_default"
res.cnLineLabelsOn = False
res.lbOrientation = "horizontal" #-- horizontal labelbar
res.sfXArray = lon
res.sfYArray = lat
#-- create the contour plot
plot = Ngl.contour_map(wks,var,res)
#-- write variable long_name and units to the plot
txres = Ngl.Resources()
txres.txFontHeightF = 0.012
Ngl.text_ndc(wks,f.variables["air"].attributes['long_name'],\
0.14,0.82,txres)
Ngl.text_ndc(wks,f.variables["air"].attributes['units'], \
0.95,0.82,txres)
#-- advance the frame
Ngl.frame(wks)
Ngl.end()