import arcpy, numpy, datetime

arcpy.env.workspace = r"C:\Users\jsb13207\devops\GEOG408E\Exam\Exam-06\Exam_06.gdb"
OF = open(r"C:\Users\jsb13207\devops\GEOG408E\Exam\Exam-06\msg.txt", "w")
aFC = 'LandParcels'
aQuery = 'Value_06 > 100'
aQ1 = 'UseCode = \'C\''
aField = 'TAX_06'
print 'running... '

def curs():
    with arcpy.da.UpdateCursor(aFC, "*", aQuery) as cursor:
        for i in cursor:
            i[5] = (i[4] * 0.08)
            cursor.updateRow(i)

def val():
    arr = arcpy.da.FeatureClassToNumPyArray(aFC, aField, aQ1)
    square = [numpy.square(i) for i in arr['TAX_06']]
    sum = numpy.sum(square)
    sqrt = numpy.sqrt(sum)
    listItems = [(i / sqrt) for i in arr['TAX_06']]

    for i in listItems:
        print i
        OF.write(str(i) + '\n')

curs()
val()

OF.close()
print datetime.datetime.now()
print "EOF\n"
