''' We will use this program to find the squared footage of a building.'''

def sqft_calc(buildingName,buildingWidth,buildingLength):
    squarfootage=(buildingLength*buildingWidth*numberOfFloors)
    print "The ", buildingName, "contains ", squarfootage, "sqft."

buildingName= "Nubian Tower"
buildingWidth= 1000
buildingLength=1500
numberOfFloors= 19

sqft_calc(buildingName,buildingWidth,buildingLength)
