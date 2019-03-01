import arcpy

arcpy.env.workspace = r".gdb"
outFile = open(r".txt", "w")
print "\n\n"
fList = arcpy.ListFeatureClasses()
fList.sort(reverse=False)

for x in fList:
    desc = arcpy.Describe(x)
    sList = desc.shapeType
    cList = arcpy.GetCount_management(x)
    pList = desc.spatialReference.type
    rName = x+"_P"
    if pList == 'Geographic':
        if arcpy.Exists(rName):
            arcpy.Delete_management(rName)
            # print "Deleted a projected file"
            # outFile.write("Deleted a projected file\n")
        arcpy.Project_management(x, rName, arcpy.SpatialReference(26917))
        chan = "not projected"
        print "{0} feature class is {1} type and has {2} features. It is {3}. It has been projected to {4}.".format(x, sList.lower(), cList, chan, rName)
        outFile.write("{0} feature class is {1} type and has {2} features. It is {3}. It has been projected to {4}.\n".format(x, sList.lower(), cList, chan, rName))
    else:
        print "{0} feature class is {1} type and has {2} features. It is {3}.".format(x, sList.lower(), cList, str(pList))
        outFile.write("{0} feature class is {1} type and has {2} features. It is {3}.\n".format(x, sList.lower(), cList, str(pList)))

print "EOF\n"


# #### Returns the number of feature in a feature class or rows in a table ####
#print arcpy.GetCount_management(aFC)

# #### since featuretype and shapetype needs describe. Avoid repetition #####
# aDesc = arcpy.Describe(aFC)
#print aDesc.featureType #Simple
#print aDesc.shapeType #Point

# #### CHECK THE REFERENCE NAME OF THE TYPE. EX GCS_Nor.._Am.._1983#####
#print aDesc.SpatialReference.name

# #### CURRENT SPATIAL REFERENCE: PROJECTED OR NAH #####
#print "Current type of " + aFC + " is " + aDesc.SpatialReference.type

# #### CHECK THE CODE OF THE REFERENCE #####
#print str(aDesc.SpatialReference.factoryCode)
