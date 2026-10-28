import requests

#response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
#heroes = response.json()
   
def get_max_height(gender, occupation):
    if type(gender) is not str:
        raise TypeError("gender must be a string value")
    if type(occupation) is not bool:
        raise TypeError("occupation must be a boolean value")
    response = requests.get("https://akabab.github.io/superhero-api/api/all.json", timeout=10)
    response.raise_for_status()
    heroes = response.json()
    max_height = 0
    hero_name = ""
    max_height_str = ""
    for i in heroes:
        has_work = i.get("work").get("occupation") != "-"
        if i.get("appearance").get("gender").lower() == gender.lower():
            if occupation == has_work:
                try:
                    height = float(i.get("appearance").get("height")[1].split()[0])
                except (ValueError, TypeError):
                    continue
                if height >= max_height:
                    max_height = height
                    max_height_str = i.get("appearance").get("height")[1]
                    hero_name = i.get("name")
    if hero_name == "":
        return "Нет героя с заданными параметрами"
    return hero_name, max_height_str