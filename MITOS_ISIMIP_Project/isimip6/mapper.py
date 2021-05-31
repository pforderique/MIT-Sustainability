from math import ceil, floor

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def grid_to_lat(grid_y):
    if grid_y < 0 or grid_y > 360: raise KeyError("Grid lat out of bounds (360, 0)")
    return translate(grid_y, 0, 360, 90, -90) # 90 to -90 bc inverted!

def grid_to_lon(grid_x):
    if grid_x < 0 or grid_x > 720: raise KeyError("Grid lon out of bounds (0, 720)")
    return translate(grid_x, 0, 720, -180, 180)

def lat_to_grid(lat_coor):
    if lat_coor < -90 or lat_coor > 90: raise KeyError("Lat out of bounds (-90, 90)")
    return translate(lat_coor, 90, -90, 0, 360) # 90 to -90 bc inverted!

def lon_to_grid(lon_coor):
    if lon_coor < -180 or lon_coor > 180: raise KeyError("Lon out of bounds (-180, 180)")
    return translate(lon_coor, -180, 180, 0, 720)

def grid_to_coor(grid_y, grid_x):
    return (grid_to_lat(grid_y), grid_to_lon(grid_x))

def coor_to_grid(lat, lon): 
    return (lat_to_grid(lat), lon_to_grid(lon))

def show_grid_calculations():
  MIT_COOR = (42.3588, -71.0934)
  UPPER_LAT = ceil(MIT_COOR[0]*2)/2
  LOWER_LAT = floor(MIT_COOR[0]*2)/2
  UPPER_LON = ceil(MIT_COOR[1]*2)/2
  LOWER_LON = floor(MIT_COOR[1]*2)/2
  print("MIT Coordinates:", MIT_COOR)
  print("\t", LOWER_LAT, "<", MIT_COOR[0], "<", UPPER_LAT)
  print("\t", LOWER_LON, "<", MIT_COOR[1], "<", UPPER_LON)
  print("-----------------------------------------")
  MIT_GRID_COOR = coor_to_grid(*MIT_COOR)
  UPPER_GRID_LAT = ceil(MIT_GRID_COOR[0])
  LOWER_GRID_LAT =  floor(MIT_GRID_COOR[0])
  UPPER_GRID_LON = ceil(MIT_GRID_COOR[1])
  LOWER_GRID_LON =  floor(MIT_GRID_COOR[1])
  print("MIT GRID Coordinates:", MIT_GRID_COOR)
  print("\t", LOWER_GRID_LAT, "<", MIT_GRID_COOR[0], "<", UPPER_GRID_LAT)
  print("\t", LOWER_GRID_LON, "<", MIT_GRID_COOR[1], "<", UPPER_GRID_LON)

if __name__ == "__main__":
    show_grid_calculations()