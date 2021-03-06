"""
Magnetic data from Rio de Janeiro
=================================

We provide sample total-field magnetic anomaly data from an airborne survey of
Rio de Janeiro, Brazil, from the 1970s. The data are made available by the
Geological Survey of Brazil (CPRM) through their `GEOSGB portal
<http://geosgb.cprm.gov.br/>`__. See the documentation for
:func:`verde.datasets.fetch_rio_magnetic_anomaly` for more details.
"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import verde as vd

# The data are in a pandas.DataFrame
data = vd.datasets.fetch_rio_magnetic_anomaly()
print(data.head())

# Make a Mercator plot of the data using Cartopy
plt.figure(figsize=(7, 5))
ax = plt.axes(projection=ccrs.Mercator())
ax.set_title('Total-field Magnetic Anomaly of Rio de Janeiro', pad=25)
# Since the data is diverging (going from negative to positive)
# we need to center our colorbar on 0. To do this, we calculate
# the maximum absolute value of the data to set vmin and vmax.
maxabs = np.max(np.abs([data.total_field_anomaly_nt.min(),
                        data.total_field_anomaly_nt.max()]))
# Cartopy requires setting the projection of the original data through the
# transform argument. Use PlateCarree for geographic data.
plt.scatter(data.longitude, data.latitude, c=data.total_field_anomaly_nt,
            s=1, cmap='seismic', vmin=-maxabs, vmax=maxabs,
            transform=ccrs.PlateCarree())
cb = plt.colorbar(pad=0.1)
cb.set_label('nT')
ax.gridlines(draw_labels=True)
# Set the extent of the plot to the limits of the data
ax.set_extent(vd.get_region(data.longitude, data.latitude))
plt.tight_layout()
plt.show()
