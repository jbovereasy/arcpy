#John Baltazar
#Geog408D
import arcpy

#### Set environment #####
arcpy.env.workspace = r"C:\Users\jsb13207\devops\GEOG408E\Week_05\Exercise_Data.gdb"
print "\n" + arcpy.env.workspace

#### Instead of for loop; just do one type = Businesses #####
aFC = "Businesses"

#### Returns the number of feature in a feature class or rows in a table ####
print arcpy.GetCount_management(aFC)

#### since featuretype and shapetype needs describe. Avoid repetition #####
aDesc = arcpy.Describe(aFC)
print aDesc.featureType #Simple
print aDesc.shapeType #Point

#### CHECK THE REFERENCE NAME OF THE TYPE. EX GCS_Nor.._Am.._1983#####
print aDesc.SpatialReference.name

#### CURRENT SPATIAL REFERENCE: PROJECTED OR NAH #####
print "Current type of " + aFC + " is " + aDesc.SpatialReference.type

#### CHECK THE CODE OF THE REFERENCE #####
print str(aDesc.SpatialReference.factoryCode)


#### CHECK IF THE TYPE EXISTS; if not project it#####
if arcpy.Exists("Businesess_P"):
    print "Yes its derr"
else:
    arcpy.Project_management(aFC, "Businesess_P", arcpy.SpatialReference(26917))


#### TO DELETE A TYPE AND PROJECT IT #####
if arcpy.Exists("Businesess_P"):
   arcpy.Delete_management("Businesses_P")
   arcpy.Project_management(aFC, "Businesses_P", arcpy.SpatialReference(26917))
   print "re-Projected"
else:
   print "failed projected"

# Script end message
print "End of the script!\n"   
