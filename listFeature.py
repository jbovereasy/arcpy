#John Baltazar
#GEOG408D

import arcpy

workEnv = r"C:\Users\jsb13207\devops\GEOG408E\Assignments\1\Assignment_01.gdb"
arcpy.env.workspace = workEnv
print "Current directory is {0}".format(arcpy.env.workspace)

fList = arcpy.ListFeatureClasses() # list all feature classes
for x in fList:
   dList = arcpy.Describe(x).shapeType # list feature type: point, shape, etc..
   cList = arcpy.GetCount_management(x) # list num of counts on a feature
   pList = arcpy.Describe(x).spatialReference.type # list if projected or geographic
   print "{0} feature class is {1} type and has {2} features. It is {3}.".format(x, dList.lower(), cList, pList.lower())

   # if arcpy.Describe(x).spatialReference.type == 'Geographic':
   #     print "{0} feature class is {1} type and has {2} features. It is not projected".format(x, dList.lower(), cList))
   # else:

print "\nEOF"