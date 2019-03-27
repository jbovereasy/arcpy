import arcpy

fPath = r"C:\Users\jsb13207\devops\GEOG408E\Assignments\4\Assignment_04"
cGdb = "Assignment_04.gdb"
nGdb = "PCS_Data.gdb"
arcpy.env.workspace = fPath + "\\" + cGdb

# def newGdb():
#     arcpy.CreateFileGDB_management(r"C:\Users\jsb13207\devops\GEOG408E\Assignments\4\Assignment_04", "PCS_Data.gdb")
#     arcpy.env.workspace = r"C:\Users\jsb13207\devops\GEOG408E\Assignments\4\Assignment_04\PCS_Data.gdb"
    
def checkProjection():
    fList = arcpy.ListFeatureClasses()
    for i in fList:
        desc = arcpy.Describe(i)
        pList = desc.spatialReference.type
        rName = fPath + "\\" + nGdb + "\\" + i + "_P"
        if pList == 'Geographic':
            if arcpy.Exists(rName):
                arcpy.Delete_management(rName)
            arcpy.Project_management(i, rName, arcpy.SpatialReference(26945))
        else:
            print "you goofed something" 

# newGdb()
checkProjection()

print "EOF!!!\n"
