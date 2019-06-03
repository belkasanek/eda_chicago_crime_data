import urllib.request

try:
    # main data set
    url = 'https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD'  
    urllib.request.urlretrieve(url, './data/Chicago_Crimes.csv')
    
    # location of Chicago Police Stations
    url = 'https://data.cityofchicago.org/api/views/z8bn-74gv/rows.csv?accessType=DOWNLOAD'  
    urllib.request.urlretrieve(url, './data/Police_Stations.csv')
    
    # census data about community areas for 2010
    url = 'https://datahub.cmap.illinois.gov/dataset/5700ba1a-b173-4391-a26e-48b198e830c8/resource/b30b47bf-bb0d-46b6-853b-47270fb7f626/download/CCASF12010CMAP.xlsx'
    urllib.request.urlretrieve(url, './data/census_for_community_ares_2010.xlsx')
    
    # geojson of Chicago Police Districts
    url = 'https://data.cityofchicago.org/api/geospatial/fthy-xz3r?method=export&format=GeoJSON'
    urllib.request.urlretrieve(url, './data/Boundaries_Police_Districts')
    
    # geojson of Chicago Community Areas
    url = 'https://data.cityofchicago.org/api/geospatial/cauq-8yn6?method=export&format=GeoJSON'
    urllib.request.urlretrieve(url, './data/Boundaries_Community_Areas')
except:
    print('Error occurred.') 
    print('The data can be manually downloaded from https://data.cityofchicago.org/')