import urllib.parse
import requests
import datetime
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Ht2bjrkAxFFZ9eDO1NFj4FzSJ4jbblty"
 
while True:
    orig = input("Direccion Inicial: ")
    if orig == "Salir" or orig == "s":
        break
    dest = input("Destino: ")
    if dest == "Salir" or dest == "s":
         break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
 
    if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("=============================================")
            print("Direccion desde " + (orig) + " hasta " + (dest))
            print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
            print("Kilometros:      " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")