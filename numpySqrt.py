import arcpy, numpy
arcpy.env.workspace = r"C:\Users\jsb13207\devops\GEOG408E\Exam\Exam_05\Exam_05.gdb"

aFC = "LandParcels"
aQ = 'Zone = \'Zone D\''

def stdVal():
    arr = arcpy.da.FeatureClassToNumPyArray(aFC, "TaxValue06", aQ)
    square = [numpy.square(i) for i in arr['TaxValue06']]
    sum = numpy.sum(square)
    sqrt = numpy.sqrt(sum)
    listItems = [(i / sqrt) for i in arr['TaxValue06']]
    
    for i in listItems:
        print i

stdVal()
print "EOF!!!\n"
