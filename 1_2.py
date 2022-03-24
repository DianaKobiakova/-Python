t = int(input("Enter time in seconds:"))
h = t //3600
m = (t - h*3600)//60
s = t - (h*3600 + m*60)
print(f"Time in the format hh:mm:ss - {h}:{m}:{s}")