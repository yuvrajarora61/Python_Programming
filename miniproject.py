import numpy as np

#PROJECT 1:

data = np.genfromtxt("sensor_data.csv",delimiter=",",skip_header=1,usecols=(1,2,3,4))
print(data)

temperature = data[:, 0]
distance = data[:, 1]
battery = data[:, 2]
humidity = data[:, 3]

print("Average Temperature:", np.mean(temperature))
print("Minimum Temperature:", np.min(temperature))
print("Maximum Temperature:", np.max(temperature))
print("\nAverage Distance:", np.mean(distance))
print("Minimum Distance:", np.min(distance))
print("Maximum Distance:", np.max(distance))
print("\nAverage Battery:", np.mean(battery))
print("Minimum Battery:", np.min(battery))
print("Maximum Battery:", np.max(battery))
print("\nAverage Humidity:", np.mean(humidity))
print("Minimum Humidity:", np.min(humidity))
print("Maximum Humidity:", np.max(humidity))

timedata = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, usecols=(0),dtype=str)
print(timedata)
max_tempidx=np.argmax(temperature)
print(max_tempidx)
print("Time Of Max Temperature:", timedata[max_tempidx])

print("Battery Less Than 30(count):", np.sum(battery < 30))

with open("sensor_data!.csv", "w") as f:
    f.write(f"Average Temperature = {np.mean(temperature)}\n")
    f.write(f"Maximum Temperature = {np.max(temperature)}\n")
    f.write(f"Minimum Temperature = {np.min(temperature)}\n\n")
    f.write(f"Average Distance = {np.mean(distance)}\n")
    f.write(f"Maximum Distance = {np.max(distance)}\n")
    f.write(f"Minimum Distance = {np.min(distance)}\n\n")
    f.write(f"Average Battery = {np.mean(battery)}\n")
    f.write(f"Maximum Battery = {np.max(battery)}\n")
    f.write(f"Minimum Battery = {np.min(battery)}\n\n")
    f.write(f"Average Humidity = {np.mean(humidity)}\n")
    f.write(f"Maximum Humidity = {np.max(humidity)}\n")
    f.write(f"Minimum Humidity = {np.min(humidity)}\n\n")
    f.write(f"Time Of Max Temperature =  {timedata[max_tempidx]}\n\n")
    f.write(f"Battery Less Than 30(count) = {np.sum(battery < 30)}")


#PROJECT 2:

path = np.genfromtxt("robot_path.csv", delimiter=",", skip_header=1)
print(path)

diffs = np.diff(path, axis=0)
distances = np.sqrt(np.sum(diffs**2, axis=1))
total_distance = np.sum(distances)

print("Total Distance:",total_distance)


dist_from_origin = np.sqrt(np.sum(path**2, axis=1))
idx = np.argmax(dist_from_origin)
print("Farthest Point From Origin:",path[idx])


revisited = "YES" if len(np.unique(path, axis=0))< len(path) else "NO"
print("Revisited:",revisited)


with open("robot_path!.csv", "w") as f:
    f.write(f"Total Distance : {total_distance}\n")
    f.write(f"Farthest Point From Origin : {path[idx]}\n")
    f.write(f"Revisited = {revisited}\n")

