import urllib.request

try:
    # main data set
    url = 'https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD'  
    urllib.request.urlretrieve(url, './data/Chicago_Crimes.csv')
    
    # location of Chicago Police Stations
    url = 'https://data.cityofchicago.org/api/views/z8bn-74gv/rows.csv?accessType=DOWNLOAD'  
    urllib.request.urlretrieve(url, './data/Police_Stations.csv')
    
    # geojson of Chicago Police Districts
    url = 'https://data.cityofchicago.org/api/geospatial/fthy-xz3r?method=export&format=GeoJSON'
    urllib.request.urlretrieve(url, './data/Boundaries_Police_Districts')
    
    # geojson of Chicago Community Areas
    url = 'https://data.cityofchicago.org/api/geospatial/cauq-8yn6?method=export&format=GeoJSON'
    urllib.request.urlretrieve(url, './data/Boundaries_Community_Areas')
except:
    print('Error occurred.') 
    print('The data can be manually downloaded from https://data.cityofchicago.org/')