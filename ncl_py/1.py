import Ngl
#-- open workstation
wks_type = "png"
wks = Ngl.open_wks(wks_type,"plot_TRANS_maps_py")
#-- which projection do we want to plot
projections = ["CylindricalEquidistant","Mollweide",\
"Robinson","Orthographic"]
#-- resource settings
#mpres = Ngl.Resources() #-- resource object
mpres.vpWidthF = 0.8 #-- viewport width
mpres.vpHeightF = 0.8 #-- viewport height
mpres.mpFillOn = True
mpres.mpOceanFillColor = "Transparent"
mpres.mpLandFillColor = "Gray90"
mpres.mpInlandWaterFillColor = "Gray90"
for proj in projections:
mpres.mpProjection = proj
mpres.tiMainString = proj
map = Ngl.map(wks,mpres)
Ngl.end()