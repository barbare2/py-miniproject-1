მოცემული API-დან (https://www.fbi.gov/wanted/api) წამოღებულია 20 ძებნილი ადამიანის ოფიციალური ინფორმაცია. 
კოდში ხდება რიქუესთის გაგზავნა მოცემულ API-ზე და response ობიექტზე რამდენიმე ატრიბუტი ფუნქციის გამოყენება. 
წამოღებული ინფორმაცია ინახება JSON ფაილში, შესაბამისად ფორმატირებული. API-დან წამოღებული ინფორმაციიდან 
იბეჭდება განცხადების სათაური, ჯილდოს ტექსტი, გამოქვეყნების თარიღი, განცხადების URL მისამართი (მეტი ინფორმაციისთვის) 
და გაფრთხილება კონკრეტულ ძებნილ პიროვნებაზე.
საბოლოოდ, იქმნება sql ბაზა (ცხრილი), სადაც ინახება მოცემულ 20 პიროვნებაზე 
შესაბამისი ინფორმაცია (სათაური, რასა, ეროვნება, სქესი, თვალის ფერი, თმის ფერი, წონა და მინიმალური და მაქსიმალური სიმაღლე).



From the given API (https://www.fbi.gov/wanted/api) official information of 20 wanted people is taken. The code sends a request 
to the given API and uses several attribute functions on the response object. The extracted information is stored in a JSON file, 
formatted accordingly. Information obtained from the API prints the title of the announcement, the text of the award, the date of publication, 
the URL of the announcement (for more information) and a warning to a specific wanted person.
Finally, a sql database (table) is created, which stores relevant information about the given 20 individuals (title, race, nationality, 
sex, eye color, hair color, weight, and minimum and maximum height).
