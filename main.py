import netway

#netway.debug.url("https://google.com") # Debug For URL

url = "pakkan.com.tr"


nw = netway.get(url)

print(nw.text)
