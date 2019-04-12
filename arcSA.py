import arcpy
from arcpy.sa import * 

arcpy.env.workspace = r"C:\Users\jsb13207\devops\GEOG408E\Week_12\Example_Data.gdb"
arcpy.env.overwriteOutput = False # if true, it will overwrite everything

rList = arcpy.ListRasters()
for i in rList:
    rasterObj = arcpy.Raster(i)
    print "{} has RAT {} ".format(rasterObj.name, rasterObj.hasRAT)

print "EOF\n"    
