# ArcMap_WorkflowAutomation

This project contains a collection of Python 2 scripts designed to be used with Esri's ArcMap 10.x software.
ArcMap 10.x utilizes Python 2.7, and these scripts are written to be compatible with that environment,
specifically leveraging the `arcpy` site-package for geoprocessing and ArcGIS functionality.

**Scripts Included:**

1.  **`check_arcpy_version.py`**:
    *   Description: Checks if the `arcpy` module is accessible within ArcMap and prints the installed ArcGIS version to the Python window.
    *   Purpose: Verifies that the `arcpy` environment is correctly set up and functional.

2.  **`run_buffer_tool.py`**:
    *   Description: Executes the `Buffer` geoprocessing tool on a specified input feature class.
    *   Purpose: Demonstrates how to run a basic geoprocessing tool from `arcpy`, taking input and output paths and tool parameters.

3.  **`list_feature_classes.py`**:
    *   Description: Lists all feature classes present within a specified geodatabase or folder workspace.
    *   Purpose: Shows how to interact with workspaces and programmatically discover data within them.

4.  **`access_feature_class_fields_and_data.py`**:
    *   Description: Lists the fields of a given feature class and then iterates through the features to print the values of a specified field.
    *   Purpose: Illustrates how to access feature class schema (fields) and feature attributes using cursors in `arcpy`.

5.  **`get_raster_properties.py`**:
    *   Description: Retrieves and prints various properties of a raster dataset, such as format, band count, cell size, and spatial reference.
    *   Purpose: Demonstrates how to work with raster data in `arcpy` and access raster metadata.

6.  **`set_arcgis_environment_settings.py`**:
    *   Description: Shows how to set ArcGIS environment settings, specifically `workspace` and `overwriteOutput`, which affect the behavior of geoprocessing tools.
    *   Purpose: Explains how to control the geoprocessing environment programmatically for script execution.

**How to Use These Scripts:**

These Python 2 scripts are designed to be run within the ArcMap 10.x environment. You can execute them in the following ways:

*   **ArcMap Python Window:** Open ArcMap, then open the Python Window (usually found on the Geoprocessing toolbar or menu). You can copy and paste the script code directly into the Python Window and press Enter to execute it.
*   **ArcMap Script Tools:** You can create custom script tools within an ArcMap toolbox.  To do this:
    1.  Create a new toolbox or use an existing one.
    2.  Right-click on the toolbox and select "Add" -> "Script...".
    3.  Fill in the tool's name, label, and other properties.
    4.  Browse to the `.py` file containing your script for the "Script File" parameter.
    5.  Define any parameters your script requires in the "Parameters" tab.
    6.  You can then run your script tool from the toolbox within ArcMap.

**Important Notes:**

*   **Python 2.7:** These scripts are specifically written for Python 2.7, which is the version used by ArcMap 10.x. They will likely not work directly with Python 3 without modifications.
*   **`arcpy` Dependency:** These scripts heavily rely on the `arcpy` site-package, which is only available within an ArcGIS environment (ArcMap or ArcGIS Pro).
*   **Data Paths:** Remember to replace placeholder paths in the scripts (e.g., `"C:/path/to/your/geodatabase.gdb/FeatureClass"`) with the actual paths to your ArcGIS data. Use forward slashes (`/`) in paths, even on Windows.
*   **Error Handling:** The scripts include basic `try...except` blocks for error handling, particularly for `arcpy.ExecuteError` which is common for geoprocessing tool failures. Check the Python Window for error messages if a script does not run as expected.

**Disclaimer:**

These scripts are provided as examples and for educational purposes. Always test scripts in a development environment before using them on critical data. Be sure to understand what each script does before running it, especially if it modifies or creates data.
