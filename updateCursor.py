import arcpy

arcpy.env.workspace = r"C:\<filepath>"
aFC = "LandParcels"

with arcpy.da.UpdateCursor(aFC, "*") as aC:
    for i in aC:
        if i[2] > 100 and i[3] > 100:
            i[6] = ((i[2] - i[3]) / i[3]) * 100
            aC.updateRow(i)
            if [6] < 3:
                i[7] = "A"
        else:
            print "goof"

del i
del aC

print "/n/nEOF"
