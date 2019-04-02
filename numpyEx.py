import arcpy, numpy
arcpy.env.workspace = r"C:\Users\jsb13207\devops\GEOG408E\Week_10\Example_Data.gdb"

aF = "LandParcels"
aSum = 0
aCount = arcpy.GetCount_management(aF)

with arcpy.da.SearchCursor(aF, ["TaxValue04"]) as aC:
   for i in aC:
       aSum += i[0]

print aSum #sum
print (aSum / int(str(aCount))) #average

del i
del aC

print "EOF!\n"