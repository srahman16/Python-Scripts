'''Title: Getting band information using ArcPy (in ArcGIS Pro) using Python
Created by: Shahriar Rahman
Email: shahriar.env12@gmail.com'''

import arcpy

raster_path = "XXX:/.../.../XYZ.tif" ## change according to your drive location for the .tiff file

def get_raster_band_min_max(raster_path):
    try:
        for band_index in range(1, 4):
            band_name = f"Band_{band_index}" # I didn't gave any title for my bands (so it was a default, e.g., "Band_1", "Band_2")
            result_min = arcpy.GetRasterProperties_management(raster_path, "MINIMUM", band_name) # getting the minimum raster value of the band
            min_value = result_min.getOutput(0)
            result_max = arcpy.GetRasterProperties_management(raster_path, "MAXIMUM", band_name)
            max_value = result_max.getOutput(0)
            print(f"{band_name}:")
            print(f"  Minimum value: {min_value}")
            print(f"  Maximum value: {max_value}")
    except Exception as e:
        print(f"An error occurred: {e}")

get_raster_band_min_max(raster_path) ## calling the function will give the following output

'''Output:
Band_1:
  Minimum value: -4.56
  Maximum value: 2.36
Band_2:
  Minimum value: -7.17
  Maximum value: 10.27
Band_3:
  Minimum value: -7.89
  Maximum value: 8.01
  '''
