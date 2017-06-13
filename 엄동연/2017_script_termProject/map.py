import folium
from urllib import request, parse
from xml.etree import ElementTree
import webbrowser
global x, y

def show_map(loc):
    global x, y
    address = parse.quote(loc)
    url = "http://api.vworld.kr/req/address?service=address&version=2.0&request=getcoord&key=483E0418-2F46-3223-80A1-F66D16A24685&format=xml&type=road&address="+str(address)+"&refine=true&simple=false&crs=epsg:4326"
    res = request.urlopen(url).read()
    tree = ElementTree.fromstring(res)
    itemElements = tree.getiterator("point")
    print(res)
    for item in itemElements:
        x = item.find('x')
        y = item.find('y')

    # 위도 경도 지정
    map_osm = folium.Map(location=[y.text, x.text], zoom_start=13)
    # 마커 지정
    folium.Marker([y.text, x.text], popup='Mt. Hood Meadows').add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')

    # 지도 열기
    webbrowser.open('osm.html')

