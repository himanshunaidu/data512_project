import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx
import folium.folium
 
from matplotlib.colors import rgb2hex
from matplotlib.patches import Patch
from geopandas.explore import _categorical_legend
from folium.plugins import Geocoder
#########
#
#    FUNCTIONS
#
def plot_gdf(gdf: gpd.GeoDataFrame, column: str, cmap: str = 'viridis', title: str = 'Map', 
    figsize: tuple = (10, 10), **kwargs):
    """
    Plot a GeoDataFrame with a specified column and colormap

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The GeoDataFrame to plot
    
    column : str
        The column to plot
    
    cmap : str
        The colormap to use
    
    title : str
        The title of the plot
    
    figsize : tuple
        The size of the plot
    
    **kwargs
        Additional keyword arguments to pass to the plot function
        **kwargs
            Additional keyword arguments to pass to the plot function.
            Possible kwargs for this function include:
            - legend_kwds: Additional keyword arguments for customizing the legend
            - classification_kwds: Additional keyword arguments for customizing the classification
    """
    gdf_crs = gdf.to_crs(epsg=3857)
    # Create subplots
    fig, ax = plt.subplots(1, 1, figsize = figsize)

    # Plot data
    ax = gdf_crs.plot(figsize=figsize, alpha=0.9, column = column,
        ax = ax,
        cmap = cmap,
        legend = True,
        legend_kwds = kwargs['legend_kwds'] if 'legend_kwds' in kwargs else {},
        scheme=None if 'classification_kwds' not in kwargs else "User_Defined",
        classification_kwds = kwargs['classification_kwds'] if 'classification_kwds' in kwargs else {})

    cx.add_basemap(ax)

    # Set title
    ax.set_title(title, fontdict = {'fontsize': '20', 'fontweight' : '4'})

    return fig, ax

def explore_gdf(gdf: gpd.GeoDataFrame, column: str, cmap: str = 'viridis', title: str = 'Map', figsize: tuple = (10, 10),
                search_bar: bool = True,
                bins: list = None, bin_labels: list = None, bin_column: str = '_bin') -> folium.Map:
    """
    Explore a GeoDataFrame with a specified column and colormap.
    If bins, bin_labels, and bin_column are provided, the data will be classified into bins, and the bins will be plotted.
    
    Warning:
    The binned column will also be added to the GeoDataFrame. Feel free to drop this column if you don't need it. 

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        The GeoDataFrame to plot
    
    column : str
        The column to plot
    
    cmap : str
        The colormap to use
    
    title : str
        The title of the plot
    
    figsize : tuple
        The size of the plot

    bins : list
        The bins to use for classification
    
    bin_labels : list
        The labels for the bins
    
    bin_column : str
        The column to store the bin values
    """
    if bins is None or len(bins) == 0:
        m = gdf.explore(column = column, cmap = cmap, figsize = figsize, title = title)
        return m

    if bin_labels is None or len(bin_labels) == 0:
        bin_labels = bins

    bins_true_min, bins_true_max = 0, len(bins)
    bins_true_length = bins_true_max - bins_true_min + 1

    gdf[bin_column] = np.digitize(gdf[column], bins=bins, right=False)
    cmap_listed = plt.colormaps[cmap].resampled(bins_true_length)
    # legend_elements = [Patch(facecolor=cmap_listed(i), edgecolor='black', 
    #                          label=bin_labels[i]) for i in range(len(bin_labels))]
    colors = [rgb2hex(cmap_listed(i)) for i in range(bins_true_length)]

    m = gdf.explore(bin_column, cmap=cmap, legend = False, vmin=bins_true_min, vmax=bins_true_max, figsize=figsize, title=title)
    _categorical_legend(
        m=m,
        title=title,
        categories=bin_labels,
        colors=colors
    )

    if search_bar:
        Geocoder().add_to(m)

    return m