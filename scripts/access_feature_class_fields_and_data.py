# Script Name: access_feature_class_fields_and_data.py
# Description: Lists fields in a feature class and iterates through features to print field values.

# Import arcpy
import arcpy

try:
    # Feature class path (replace with your path)
    feature_class = "C:/path/to/your/geodatabase.gdb/YourFeatureClass"

    # List fields in the feature class
    fields = arcpy.ListFields(feature_class)
    print "Fields in", feature_class, ":"
    for field in fields:
        print "  -", field.name, "(", field.type, ")"

    # Example: Iterate through features and print values of a specific field (e.g., "Name")
    fieldNameOfInterest = "Name"  # Replace with an actual field name
    if fieldNameOfInterest in [f.name for f in fields]: # Check if field exists
        with arcpy.da.SearchCursor(feature_class, [fieldNameOfInterest]) as cursor:
            print "\nValues in field '{}':".format(fieldNameOfInterest)
            for row in cursor:
                print "  -", row[0] # Access the first field in the row (which is fieldNameOfInterest)
    else:
        print "\nField '{}' not found in {}".format(fieldNameOfInterest, feature_class)


except arcpy.ExecuteError:
    print "Geoprocessing error:"
    print arcpy.GetMessages(2)
except Exception as e:
    print "Error:", e.message
