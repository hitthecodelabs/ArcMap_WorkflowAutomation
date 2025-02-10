import arcpy

shapefile_path = "C:/Users/J.Paul/Desktop/EstudioDeCobertura/Febrero/MPCEIP-DSG-2025-0432-E-GOMEZ SANCHEZ-SABANDO CASTRO/GS-SC-2-1.shp" # **Make sure this path is EXACTLY correct**

try:
    desc = arcpy.Describe(shapefile_path)
    spatial_ref = desc.spatialReference

    print "Spatial Reference Information for: {}".format(shapefile_path)
    print "-----------------------------------------"
    print "Name:", spatial_ref.name
    print "Type:", spatial_ref.type
    print "Linear Unit Name:", spatial_ref.linearUnitName
    print "Geographic Coordinate System Name:", spatial_ref.GCSName # Added to get GCS name
    print "Projected Coordinate System Name:", spatial_ref.PCSName # Added to get PCS name (if projected)
    print "Authority Code:", spatial_ref.authorityCode
    print "Authority Factory Code:", spatial_ref.factoryCode

except Exception as e:
    print "Error getting spatial reference information:", e