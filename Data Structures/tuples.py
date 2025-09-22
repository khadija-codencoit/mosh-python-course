
point = (1,2)
print(type(point))


# Problem: Storing Coordinates

# You are building a GPS tracking system. Each location is represented by a pair of latitude and longitude.
# Requirements:
# Store multiple locations in a tuple.
# Each location cannot be changed once recorded (read-only).
# Print all stored locations.



def coordinate(location1,location2):
    return (location1,location2)

location = coordinate(23.8103, 90.4125)
print(location)