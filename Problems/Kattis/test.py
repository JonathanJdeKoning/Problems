import json
data = None
with open("C:/Users/jj720/Documents/PythonScripts/CompetitiveProgramming/Problems/Problems/Kattis/table.json", "r", encoding="utf-8") as file:
    data = json.load(file)

mp = {}
elems = data["elements"]
for elem in elems:
    mp[elem["symbol"]] = elem["number"]

print(mp)