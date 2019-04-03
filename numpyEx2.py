import arcpy, numpy
arcpy.env.workspace = r"C:\Users\jsb13207\devops\GEOG408E\Week_10\Example_Data.gdb"
aFC = "LandParcels"

# Create a a list of fields    
fList = ['U_ID', 'LandUse', 'Zone', 'TaxValue04', 'TaxValue06']

# Converts a feature class to NumPy structured array.
aNumpyArray = arcpy.da.FeatureClassToNumPyArray(aFC, fList)
print numpy.mean(aNumpyArray["TaxValue04"])

print "\nEnd of the script!"    
