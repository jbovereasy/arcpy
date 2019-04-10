# Calculate 7% tax for 2014 and 8% for 2016 that has values greater than 100

import arcpy, numpy, os
arcpy.env.workspace = r"C:\Users\jsb13207\devops\GEOG408E\Exam\Exam-04\Exam_04.gdb"
OF = open(r"C:\Users\jsb13207\devops\GEOG408E\Exam\Exam-04\msg.txt", "w")
print "starting..."

aFC = "LandParcels"
aFields = ["TaxVal04", "TaxVal06"]

def longWay():
    arr = arcpy.da.FeatureClassToNumPyArray(aFC, aFields, 'TaxVal04 > 100')
    print numpy.sum(arr["TaxVal04"]) * 0.07
    OF.write("Total collected tax for 2004 is $" + str(numpy.sum(arr["TaxVal04"]) * 0.07))

    arr1 = arcpy.da.FeatureClassToNumPyArray(aFC, aFields, 'TaxVal06 > 100')
    aTax06 = [ i * 0.08 for i in arr1["TaxVal06"]]   #List comprehension
    print numpy.sum(aTax06)
    OF.write("\nTotal collected tax for 2006 is $" + str(numpy.sum(aTax06)))
    
def shortWay():
    arr = arcpy.da.FeatureClassToNumPyArray(aFC, aFields)
    print numpy.sum(arr[arr["TaxVal04"] > 100]["TaxVal04"] * 0.07)
    print numpy.sum(arr[arr["TaxVal06"] > 100]["TaxVal06"] * 0.08)

longWay()
shortWay()
OF.close()
print "EOF!\n"
