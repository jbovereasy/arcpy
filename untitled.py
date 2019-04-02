import arcpy, os

cGDB = r"\Assignment_04.gdb"
nGDB = r"\PCS_Data.gdb"
aPath = r"C:\Users\jsb13207\devops\GEOG408E\Assignments\4\Assignment_04"
arcpy.env.workspace = aPath + "\\" + cGDB
print "starting"

def newGdb():
#    if arcpy.Exists(aPath + nGDB)
#        arcpy.Delete_management(aPath + nGDB)
   arcpy.CreateFileGDB_management(aPath, nGDB)

def checkProjection():
   for i in arcpy.ListFeatureClasses():
       desc = arcpy.Describe(i)
       pList = desc.spatialReference.type
       rName = aPath + nGDB + "\\" + i + "_P"
       if pList == 'Geographic':
           if arcpy.Exists(rName):
               arcpy.Delete_management(rName)
           arcpy.Project_management(i, rName, arcpy.SpatialReference(26917))
       else:
           print "you goofed something"

# def withConversion():

newGdb()
checkProjection()
# withConversion()

print "EOF!!!\n"