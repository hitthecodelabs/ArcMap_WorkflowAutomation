# Script Name: get_raster_properties.py
# Description: Retrieves and prints properties of a raster dataset.

# Import arcpy
import arcpy

try:
    # Raster dataset path (replace with your path)
    raster_dataset = "C:/path/to/your/raster.tif"

    # Create a Raster object
    raster = arcpy.Raster(raster_dataset)

    # Get raster properties
    print "Raster Properties for:", raster_dataset
    print "  - Format:", raster.format
    print "  - Band Count:", raster.bandCount
    print "  - Cell Size X:", raster.meanCellWidth
    print "  - Cell Size Y:", raster.meanCellHeight
    print "  - Spatial Reference:", raster.spatialReference.name

except arcpy.ExecuteError:
    print "Geoprocessing error:"
    print arcpy.GetMessages(2)
except Exception as e:
    print "Error:", e.message
