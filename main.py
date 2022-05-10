import requests
import json
import sqlite3

response = requests.get('https://api.fbi.gov/wanted/v1/list')
print(response.status_code)
print(response.content)
print(response.headers)
data = json.loads(response.content)
result = data.get("items")
final_data = json.dumps(result, indent=4)
with open('fbi_data.json', 'w') as file:
    file.write(final_data)

for i in range(0, 20):
    print(f"Title: {result[i].get('title')}")
    print(f"Reward text: {result[i].get('reward_text')}")
    print(f"Publication: {result[i].get('publication')}")
    print(f"More info: {result[i].get('url')}")
    print(f"Caution: {result[i].get('caution')}")





# ცხრილში ინახება FBI-ის მიერ ძებნილი ადამიანის ოფიციალური ინფორმაცია სათაური, რასა,
# ეროვნება, სქესი, თვალის ფერი, თმის ფერი, წონა და მინიმალური და მაქსიმალური სიმაღლე.

conn = sqlite3.connect("fbi_wanted_data.sqlite")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE FBI_WANTED_PEOPLE
                    (title VARCHAR(100),
                    race VARCHAR(100),
                    nationality VARCHAR(100),
                    sex VARCHAR(100),
                    eyes_raw VARCHAR(100),
                    hair VARCHAR(100),
                    weight INTEGER,
                    height_min INTEGER,
                    height_max INTEGER);''')

query = '''INSERT INTO FBI_WANTED_PEOPLE (title, race, nationality, sex,
                                          eyes_raw, hair, weight, height_min, height_max)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'''
for i in range(0, 20):
    values = (result[i].get('title'), result[i].get('race'), result[i].get('nationality'),
              result[i].get('sex'), result[i].get('eyes_raw'), result[i].get('hair'),
              result[i].get('weight'), result[i].get('height_min'), result[i].get('height_max'))
    cursor.execute(query, values)
    conn.commit()

conn.close()
