# Libraries
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
 
# Set the dimension of the figure
my_dpi=96
plt.figure(figsize=(2600/my_dpi, 1800/my_dpi), dpi=my_dpi)
 
# read the data (on the web)
data = pd.read_csv('http://python-graph-gallery.com/wp-content/uploads/TweetSurfData.csv', sep=";")
 
# Make the background map
m = Basemap(projection='cyl')
m.drawmapboundary(fill_color='#060f36', linewidth=0)
m.fillcontinents(color='#3a4954', alpha=0.3)
m.drawcoastlines(linewidth=0.1, color="white")
 
# # prepare a color for each point depending on the continent.
data['labels_enc'] = pd.factorize(data['homecontinent'])[0]
 
# # Add a point per position
m.scatter(data['homelon'], data['homelat'], s=data['n']/10, alpha=0.5, c=data['labels_enc'], cmap="Set1")
 
# # copyright and source data info
plt.text( -170, -58,'COVID-19 diffusion over time', ha='left', va='bottom', size=9, color='#555555' )
plt.tight_layout()

# # Save as png
# plt.savefig('#315_Tweet_Surf_Bubble_map1.png', bbox_inches='tight')

plt.show()