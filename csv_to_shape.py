import arcpy

# Set the workspace
arcpy.env.workspace = r"C:\XY_to_Shape"

# Set the input CSV file
csv_file = "pois_aus.csv"

# Set the output shapefile name
output_shp = "POI_AUS.shp"

# Use the XY Table to Point tool to create a point shapefile
arcpy.management.XYTableToPoint(csv_file, output_shp, "Long", "Lat", "", "")
print("Well done! Shapefile created.")