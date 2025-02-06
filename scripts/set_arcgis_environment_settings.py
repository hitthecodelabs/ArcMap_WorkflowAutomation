# Script Name: set_arcgis_environment_settings.py
# Description: Demonstrates setting workspace and overwriteOutput environment settings in ArcGIS.

# Import arcpy
import arcpy

try:
    # Set workspace (where output data will be created by default)
    output_gdb = "C:/path/to/your/output_geodatabase.gdb"
    arcpy.env.workspace = output_gdb

    # Set overwrite output to True (allows tools to overwrite existing datasets)
    arcpy.env.overwriteOutput = True

    # Now, any geoprocessing tool that creates output will by default:
    # 1. Create output in 'output_gdb' if not specified otherwise.
    # 2. Overwrite existing datasets with the same name if they exist.

    # Example: Create a feature class (it will be created in 'output_gdb')
    output_fc_name = "TestFeatureClass"
    arcpy.CreateFeatureclass_management(output_gdb, output_fc_name, "POINT")
    print "Feature class '{}' created in '{}'".format(output_fc_name, output_gdb)


except arcpy.ExecuteError:
    print "Geoprocessing error:"
    print arcpy.GetMessages(2)
except Exception as e:
    print "Error:", e.message
