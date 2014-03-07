import numpy as np
import matplotlib.pyplot as pl
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

  
def bar_from_temp_and_volumes(temp,volumes):
    """returns pressure in Bar needed to carbonate a keg at 'volumes' of CO2 and 'temp' temperature
    British style beers = 2.0 - 2.4  (I think that 1.0 is more like it)
    Most other beers = 2.4 - 2.85
    High-carbonation beers = 2.85 - 2.95"""
    # TODO: native calculation in degrees C
    t = (temp * 9/5) + 32  # temp in F
    p = -16.6999 - (0.0101059*t) + (0.00116512*t*t) + (0.173354*t*v) + (4.24267*v)-(0.0684226*v*v)
    bar = p/14.5037738
    return bar

volumes = np.arange(0.5,5.5,0.1)
temps = range(26)
cnums = 1 * len(volumes)
v, t = np.meshgrid(volumes, temps)
pl.contour(bar_from_temp_and_volumes(t,v),t,v,22, colors='black', linewidth=.5, alpha=0.35)
pl.contourf(bar_from_temp_and_volumes(t,v),t,v,22, cmap="gist_ncar", linewidth=.5)

xmajorlocator = MultipleLocator(0.25)
xminorlocator = MultipleLocator(0.1)
pl.gca().xaxis.set_major_locator(xmajorlocator)
pl.gca().xaxis.set_minor_locator(xminorlocator)

ymajorlocator = MultipleLocator(2)
yminorlocator = MultipleLocator(1)
pl.gca().yaxis.set_major_locator(ymajorlocator)
pl.gca().yaxis.set_minor_locator(yminorlocator)


foo = pl.colorbar()
foo.set_label("Volumes of CO2")
pl.ylabel("Ambient Temperature [C]")
pl.xlabel("Bar")
pl.xlim(0,2.5)
pl.title("Keg carbonation")
#pl.grid()
pl.show()

#for t in temps:
#    print str(t)+"C",
#    for v in volumes:
#        print round(bar_from_temp_and_volumes(t,v),1),
#    print "\n"