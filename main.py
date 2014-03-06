import numpy as np
import matplotlib.pyplot as pl

  
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

volumes = np.arange(2,3.1,0.1)
temps = range(26)

v, t = np.meshgrid(volumes, temps)

pl.contourf(v,t,bar_from_temp_and_volumes(t,v),30)
foo = pl.colorbar()
foo.set_label("Bar")
pl.ylabel("Ambient Temperature")
pl.xlabel("Volumes of CO2")
pl.title("Keg carbonation")
pl.show()

#for t in temps:
#    print str(t)+"C",
#    for v in volumes:
#        print round(bar_from_temp_and_volumes(t,v),1),
#    print "\n"