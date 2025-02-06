# Import arcpy
import arcpy

try:
    # Input feature class (replace with your actual path)
    input_features = "C:/path/to/your/geodatabase.gdb/InputPoints"

    # Output feature class (where the buffered features will be created)
    output_features = "C:/path/to/your/geodatabase.gdb/OutputBuffers"

    # Buffer distance (e.g., 100 meters)
    buffer_distance = "100 Meters"

    # Execute the Buffer tool
    arcpy.Buffer_analysis(input_features, output_features, buffer_distance)

    print "Buffer operation completed successfully!"

except arcpy.ExecuteError:
    # If geoprocessing tool fails
    print "Geoprocessing error occurred:"
    print arcpy.GetMessages(2)  # Print detailed error messages
except Exception as e:
    # Handle other potential errors
    print "An unexpected error occurred:"
    print e.message # or str(e) for more general error info
