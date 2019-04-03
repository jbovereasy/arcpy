import arcpy, datetime, os

cGDB = r"\Assignment_04.gdb"
nGDB = r"\PCS_Data.gdb"
aPath = r"C:\Users\jsb13207\devops\GEOG408E\Assignments\4\Assignment_04"
arcpy.env.workspace = aPath  + cGDB
aFC = aPath + nGDB + r"\SFV_BG_P"
print "starting"

def newGdb():
   if arcpy.Exists(aPath + nGDB):
      arcpy.Delete_management(aPath + nGDB)
   arcpy.CreateFileGDB_management(aPath, nGDB)

def checkProjection():
   for i in arcpy.ListFeatureClasses():
       desc = arcpy.Describe(i)
       pList = desc.spatialReference.type
       rName = aPath + nGDB + "\\" + i + "_P"
       arcpy.Project_management(i, rName, arcpy.SpatialReference(26917))
      
def newField():
    arcpy.AddField_management(aFC, "divIndex", "DOUBLE")

def calcIndex ():
    aList = ["POP_16", "WHITE", "BLACK", "HISPANIC", "AMERI_ES", "ASIAN", "HAWN_PI", "OTHER", "MULTI_RACE", "divIndex"]
    with arcpy.da.UpdateCursor(aFC, aList, "POP_16 > 0") as aC:
        for i in aC:
            i[9] = 1 - (((i[3]/i[0])**2) + ((i[1]/i[0])**2) + ((i[2]/i[0])**2) + ((i[4]/i[0])**2) + ((i[5]/i[0])**2) + ((i[6]/i[0])**2) + ((i[7]/i[0])**2) + ((i[8]/i[0])**2))
            aC.updateRow(i)
    del i
    del aC


newGdb()
checkProjection()
newField()
calcIndex()

print datetime.datetime.now()
print "EOF!!!\n"
