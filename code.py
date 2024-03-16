#It is important to note that we are not using the maths module in order to use the expression of lines-
#we are using the module to deal with the case of lines with slope inifinty, and the square root function.
import math as mathematics
import matplotlib.pyplot as plt
#this function simply uses high school mathematics to calculate the distance between a point and a line.
#NOTE :  a point is represented using an array with [0] being the latitude and [1] being the longitude.
#NOTE :  a line is represented using an array with [0] being the slope and [1] being a point lying on the line.
def distance(point, line):
    # Extracting components of the point and line
    x, y = point;slope, intercept = line
    # If the line is vertical, the distance is the horizontal distance
    if slope == float('inf') or slope == float('-inf'):return abs(x - intercept)
    # Calculating the distance
    distance = float(abs(slope * x - y + intercept) / mathematics.sqrt(slope**2 + 1));return distance
#opening the dataset in the code and saving the data in 2 lists, longtitude_list and latitude_list.
f = open("/Users/arjunchetanpandya/Desktop/Coding/EPOCH_HACKATHON/longitude.txt", 'r')
long_list = f.read().split()
f.close()
f = open("/Users/arjunchetanpandya/Desktop/Coding/EPOCH_HACKATHON/latitude.txt", 'r')
lat_list = f.read().split()
f.close()
#making a list of the all the points given to us in the dataset.
point_list=[]
for i in range(0,len(lat_list)):
    long_list[i]=float(long_list[i])
    lat_list[i]=float(lat_list[i])
    point=[lat_list[i],long_list[i]]
    point_list.append(point)
#making a list of (almost) all the lines which are possible in this dataset.
line_list = []
for i in range(1, len(long_list)):
    if ((float(long_list[i]) - float(long_list[0])) != 0):
        m = (float(lat_list[i]) - float(lat_list[0])) / (float(long_list[i]) - float(long_list[0]))
        c = float(lat_list[0]) - m * float(long_list[0])
        line = [m, c]
        line_list.append(line)
    else:
        continue
#calculating the line which satisfies the condition in objective one, it is the line returned by the function efficient.
#objective one
distance_list=[]
for i in line_list:
    d = 0.00
    for j in point_list:
        d+=distance(j,i)
    distance_list.append(d)
def efficient(distance_list):
    min_distance=min(distance_list)
    for i in range(0,len(distance_list)):
        if distance_list[i]==min_distance:
            minindex=i
            break
    return line_list[minindex]
print(efficient(distance_list))
#calculating the line which satisfies the condition in objective two, it is the line stored in the variable taskTwoAnswer.
#objective two
distance_list2=[]
for i in line_list:
    distance_list = []
    for j in range(0,len(point_list)):
        distance_list[j]=distance(point_list[j],i)
    distance_list2.append(max(distance_list))
min_distance=min(distance_list2)
for i in range(0,len(distance_list2)):
    if distance_list2[i]==min_distance:
        minindex=i
        break
taskTwoanswer = line_list[minindex]
print(taskTwoanswer)
#calculating the line which satisfies the condition in objective three, it is the line stored in the variable ans3.
#objective three
distance_list3=[]
taskThreeAnswer=[]
def multiple_efficient(k):
    for i in range(k):
        taskThreeAnswer.append(efficient(distance_list3))
        distance_list3.pop(distance_list3.index(efficient(distance_list3)))
ans3=taskThreeAnswer
print(ans3)

# Plotting the points
#x_values = [point[1] for point in point_list]
#y_values = [point[0] for point in point_list]
#plt.scatter(x_values, y_values)
#plt.xlabel('Longitude')
#lt.ylabel('Latitude')
#plt.title('Points')
#plt.show()
