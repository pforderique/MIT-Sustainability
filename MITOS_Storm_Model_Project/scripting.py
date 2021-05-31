# Purpose: Determine the length of intersection of MIT Buildings layer and  2 ft of all rain depths layer

# Import system modules
import arcpy
 
try:
    # Set the workspace (to avoid having to type in the full path to the data every time)
    arcpy.env.workspace = 'C:/Users/fabri/OneDrive/Documents/ArcGIS/Projects/MITOS Project/MITOS_PROJECT.gdb'
    
    # Process: Find all stream crossings (points)
    inFeatures = ["roads", "streams"]
    intersectOutput = "stream_crossings"
    clusterTolerance = 1.5    
    arcpy.Intersect_analysis(inFeatures, intersectOutput, "", clusterTolerance, "point")
 
    # Process: Buffer all stream crossings by 100 meters
    bufferOutput = "stream_crossings_100m"
    bufferDist = "100 meters"
    arcpy.Buffer_analysis(intersectOutput, bufferOutput, bufferDist)
 
    # Process: Clip the vegetation feature class to stream_crossing_100m
    clipInput = "vegetation"
    clipOutput = "veg_within_100m_of_crossings"
    arcpy.Clip_analysis(clipInput, bufferOutput, clipOutput)
 
    # Process: Summarize how much (area) of each type of vegetation is found
    #within 100 meter of the stream crossings
    statsOutput = "veg_within_100m_of_crossings_stats"
    statsFields = [["shape_area", "sum"]]
    caseField = "veg_type"
    arcpy.Statistics_analysis(clipOutput, statsOutput, statsFields, caseField)
 
except Exception as err:
    print(err.args[0])