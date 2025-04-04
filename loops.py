list_of_clouds = ["aws", "azure", "gcp", "ibm", "oracle", "alibaba", "digitalocean", "heroku", "vercel"]

print(list_of_clouds)
print(type(list_of_clouds))
print(len(list_of_clouds))
print(list_of_clouds[0])

list_of_clouds.append("utho") ## add to the end of the list

list_of_clouds.append("IBM")

list_of_clouds.append("Salesforce")

print(list_of_clouds)

##

list_of_clouds.insert(3, "IBM") ## add to the 3rd OR anywhere where you choosen the position index of the list
print(list_of_clouds)

## insert HELLO CLOUD on 0th position

list_of_clouds.insert(0,"HELLO CLOUD")
print(list_of_clouds)

## Iteraition - segerigated with each line wise seperate

for cloud in list_of_clouds:
    print("-",cloud)

for i in range(0,11):
    print(i)
