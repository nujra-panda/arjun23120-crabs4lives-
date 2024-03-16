#dataset obtained for latitude.txt and longitude.txt
from sklearn.datasets import fetch_california_housing

california_housing = fetch_california_housing(as_frame=True)
california_housing.frame.head()
california_housing.data.head()
california_housing.target.head()
california_housing.frame.info()
features_of_interest = ["Latitude", "Longitude"]
a=0
long_list=list(california_housing.frame.Longitude)
lat_list=list(california_housing.frame.Latitude)
for i in lat_list:
    print(i,end=" ")
print(a)
for i in long_list:
    print(i,end=" ")
print(a)
