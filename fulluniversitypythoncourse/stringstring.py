data = "    from:	Freelancer.com <noreply@notifications.freelancer.com May 24, 2021, 6:07 AM"

datarep = data.replace("from", "anwar")

print(datarep)

indexa = data.find("@")
print(indexa)
indexspace = data.find(" ", indexa)
print(indexspace)
print(data.startswith("from"))
school = data[indexa+1 : indexspace]
print(school)

print(data.strip())#for the beginner or end   #ltrip( for the beginner)  or lstrip(for the end space)

print(type(data))
print(dir(data))