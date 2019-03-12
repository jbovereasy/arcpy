import arcpy, datetime

arcpy.env.workspace = r"C:\Users\jsb13207\devops\GEOG408E\Assignments\3\Assignment_03\Assignment_03.gdb"
aFC = "LandParcels"

OF = open(r"C:\Users\jsb13207\devops\GEOG408E\Assignments\3\Assignment_03\msg.txt", "w")

with arcpy.da.UpdateCursor(aFC, "*") as aC:
    for i in aC:
        if i[2] > 100 and i[3] > 100:
            i[6] = ((i[2] - i[3]) / i[3]) * 100
            if i[6] < -3:
                i[7] = "A"
            if i[6] >= -3 and i[6] < 0:
                i[7] = "B"
            if i[6] == 0:
                i[7] = "C"
            if i[6] > 0 and i[6] <= 3:
                i[7] = "D"
            if i[6] > 3:
                i[7] = "E"
            aC.updateRow(i)
            
del i
del aC

print datetime.datetime.now()
OF.write(str(datetime.datetime.now()))
OF.close()

print "EOF\n"
