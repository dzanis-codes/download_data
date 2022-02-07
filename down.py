import requests
url = 'https://www.eurocontrol.int/Economics/Download/States.xlsx'
r = requests.get(url, allow_redirects=True)
open('today.xlsx', 'wb').write(r.content)
