import os
import arcpy

os.chdir("C:\\Users\\J.Paul\\Desktop\\EstudioDeCobertura\\Febrero")

shapefile_path = 'MPCEIP-DSG-2025-0432-E-GOMEZ SANCHEZ-SABANDO CASTRO\\GS-SC-2-1.shp'

cursor = arcpy.da.SearchCursor(shapefile_path, ["SHAPE@"])
row = cursor.next() # Get the first row (assuming you want the area of the first polygon - adjust if needed)
geometry = row[0]
area_sq_units = geometry.area
spatial_ref = arcpy.Describe(shapefile_path).spatialReference
linear_unit_name = spatial_ref.linearUnitName

if linear_unit_name.lower() == "meter":
    area_hectares = area_sq_units / 10000.0
elif linear_unit_name.lower() in ["foot", "feet", "u.s. survey foot"]:
    area_hectares = area_sq_units * 0.000009290304
else:
    area_hectares = area_sq_units
    print "Warning: Linear unit '{}' not recognized for hectare conversion. Area reported in shapefile's units.".format(linear_unit_name)

print "Total Area in Hectares:", area_hectares
print "Total Area in Original Units ({}):".format(linear_unit_name), area_sq_units

del cursor # Important to clean up the cursor
del row
del geometry