#John Baltazar
#GEOG408D

import arcpy

workEnv = r"/Users/johnbaltazar/Downloads/Assignment_01/Assignment_01.gdb"
arcpy.env.workspace = workEnv
OutFile = open(r"/Users/johnbaltazar/Downloads/Assignment_01/Assignment_01.gdb", "w")
print "\nCurrent directory is {0}".format(workEnv)

fList = arcpy.ListFeatureClasses() # list all feature classes
for x in fList:
   dList = arcpy.Describe(x).shapeType # list feature type: point, shape, etc..
   cList = arcpy.GetCount_management(x) # list num of counts on a feature
   pList = arcpy.Describe(x).spatialReference.type # list if projected or geographic

   if pList == 'Geographic':
      print "{0} feature class is {1} type and has {2} features. It is not projected.".format(x, dList.lower(), cList)
      OutFile.write("{0} feature class is {1} type and has {2} features. It is not projected".format(x, dList.lower(), cList))   
   else:
      print "{0} feature class is {1} type and has {2} features. It is {3}.".format(x, dList.lower(), cList, pList.lower())
      OutFile.write("{0} feature class is {1} type and has {2} features. It is {3}.".format(x, dList.lower(), cList, pList.lower()))
   
OutFile.close()
print "EOF\n"
