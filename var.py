# CONFIG

#['ar', 'uy']
COUNTRY = 'ar'

if COUNTRY == 'uy':
    ZONE = 'montevideo'

arg_places = ["buenos-aires-gba", "capital-federal"]
if COUNTRY == 'ar':
    ZONE = arg_places[1]


#TIME = ['recent', '1d', '7d']



MAXIMIZE = 0

FINAL_LINK = f'https://{COUNTRY}.computrabajo.com/empleos-en-{ZONE}?by=publicationtime&pubdate=1&p='

# XPATH

POSTULATE = "/html/body/main/div[2]/div/div[2]/div[2]/div[2]/div/a"

LOGGIN_TEXT = '/html/body/section/div/form/div[1]/p[3]'

CONTINUE = True

