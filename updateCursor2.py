import arcpy, datetime

arcpy.env.workspace = r"C:\Users\jsb13207\devops\GEOG408E\Exam\Exam-03\Exam_3.gdb"
OF = open(r"C:\Users\jsb13207\devops\GEOG408E\Exam\Exam-03\msg.txt)

aFC = "LandParcels"
aList = ["TaxVal06", "TaxVal00", "Per_Change"]
aQuery = '(TaxVal00 > 0 AND TaxVal06 > 0) AND (UseCode = \'A\' OR UseCode = \'B\')'

with arcpy.da.UpdateCursor(aFC, aList, aQuery) as aC:
    for i in aC:
        i[2] = ((i[0] - float(i[1]))/i[1])*100.00
        aC.updateRow(i)

del i
del aC

OF.write("updated!\n" + str(datetime.datetime.now()))
OF.close()
print datetime.datetime.now()
print "EOF\n"
