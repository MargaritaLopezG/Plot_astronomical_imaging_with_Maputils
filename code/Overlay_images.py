https://www.astro.rug.nl/software/kapteyn/maputilstutorial.html

Example: mu_overlayscuba.py - Overlay image with different world coordinate system


from kapteyn import maputils
from matplotlib import pyplot as plt
from matplotlib import cm

file1="/home/hector/Documents/Doctorado/pruebas_python/pruebas_APLpy/fits/A87_gS_2.fits"
file2="/home/hector/Documents/Doctorado/pruebas_python/pruebas_APLpy/fits/A87_mom0_gS_2.fits"
Basefits = maputils.FITSimage(file1)
Secondfits = maputils.FITSimage(file2)
Reprojfits = Secondfits.reproject_to(Basefits)

fig = plt.figure()
frame = fig.add_subplot(1,1,1)

baseim = Basefits.Annotatedimage(frame)
baseim.Image()
baseim.set_histogrameq()
baseim.Graticule()

overlayim = Basefits.Annotatedimage(frame, boxdat=Reprojfits.boxdat)
levels = list(range(20,200,20))
overlayim.Contours(levels=levels, colors='w')

fig.colorbar(cm.ScalarMappable(norm=None, cmap='jet'))
baseim.plot()
overlayim.plot()
baseim.interact_toolbarinfo()
baseim.interact_imagecolors()

plt.show()

#guardar como Figure_A87_matplotlib.png
