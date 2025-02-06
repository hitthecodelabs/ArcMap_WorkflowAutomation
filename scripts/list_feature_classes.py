# Script Name: list_feature_classes.py
# Description: Lists all feature classes in a specified geodatabase or folder workspace.

# Import arcpy
import arcpy

try:
    # Workspace (Geodatabase or folder) - replace with your path
    workspace = "C:/path/to/your/geodatabase.gdb"
    arcpy.env.workspace = workspace  # Set the workspace environment

    # List all feature classes in the workspace
    feature_classes = arcpy.ListFeatureClasses()

    if feature_classes:
        print "Feature Classes in", workspace, ":"
        for fc in feature_classes:
            print "  -", fc
    else:
        print "No feature classes found in", workspace

except arcpy.ExecuteError:
    print "Geoprocessing error:"
    print arcpy.GetMessages(2)
except Exception as e:
    print "Error:", e.message
