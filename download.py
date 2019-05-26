import urllib.request

try:
    # main data set
    url = 'https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD'  
    urllib.request.urlretrieve(url, './data/Chicago_crimes.csv')
    
    # location of police station
    url = 'https://data.cityofchicago.org/api/views/z8bn-74gv/rows.csv?accessType=DOWNLOAD'  
    urllib.request.urlretrieve(url, './data/Police_Stations.csv')
except:
    print('Error occurred.') 
    print('The data can be found at https://data.cityofchicago.org/')