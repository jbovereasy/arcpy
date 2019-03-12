import arcpy

arcpy.env.workspace = r"C:\<filepath>"
aFC = "LandParcels"

# Update a specific row on a table
with arcpy.da.UpdateCursor(aFC, "*") as aC:
    for i in aC:
        if i[2] > 100 and i[3] > 100:
            i[6] = ((i[2] - i[3]) / i[3]) * 100
            aC.updateRow(i)
            if i[6] > -3:
                i[7] = "A"
            if i[6] >= 0 and i[6] >= 0:
                i[7] = "B"
            if i[6] = 0:
                i[7] = "C"
            if i[6] < 3:
                i[7] = "D"
            if i[6] < 3:
                i[7] = "E"
        else:
            print "something goof"

del i
del aC
print "\n\nEOF"
