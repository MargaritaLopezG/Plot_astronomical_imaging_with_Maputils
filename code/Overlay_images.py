## Code created by Martha Margarita López Gutiérrez ##

#Example: mu_overlayscuba.py - Overlay image with different world coordinate system

from kapteyn import maputils
from matplotlib import pyplot as plt
from matplotlib import cm


Basefits = maputils.FITSimage(Files/A87_gS_2.fits)
Secondfits = maputils.FITSimage(Files/A87_mom0_gS_2.fits)
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
# Save the plot
#plt.savefig('Files/output/Figure_A87_matplotlib.png')
