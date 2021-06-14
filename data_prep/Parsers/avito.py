import requests
# coord = '{lon},{lat}'
def getjobsam(job, coord = '', rad = 1): #,station = ''):
    url = 'https://www.avito.ru/moskva/rezume'

    mydata = ''
    d = 0
    if(coord != ''):
        rad = 1
        d = 55
        mydata = {'geoCoords':f"{coord}", 'q':f'{job}', 'radius':f'{rad}'}
    # elif(station != ''):
    #     metro = genmetrodict() # сделать словарь для авито
    #     d = 18
    #     mydata = {'metro':f"{metro[station]}", 'q':f'{job}'}
    else: 
        return 'error'

    res = requests.get(url, mydata).text
    t = res.find("page-title-count") + d
    am = res[t:t + res[t:].find("<")]
    return am
