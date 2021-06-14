import overpy
api = overpy.Overpass()

def getarea(lon, lat, lonend, latend):
    coord = f"{lon},{lat},{lonend},{latend}"
    #[out:json];
    string = f"""
    (
        node[shop]({coord}); 
        node[amenity = 'cafe']({coord});
    );
    out;
    """

    data = api.query(string)
    return data.nodes

#https://wiki.openstreetmap.org/wiki/RU:%D0%9A%D0%B0%D0%BA_%D0%BE%D0%B1%D0%BE%D0%B7%D0%BD%D0%B0%D1%87%D0%B8%D1%82%D1%8C
# Пример вывода данных
# zone = getarea()
# for node in zone:
#     if 'amenity' in node.tags:
#         print(f"amen= {node.tags['amenity']}")
#     if 'shop' in node.tags:
#         print(f"shop= {node.tags['shop']}")
#     print(f"lon= {node.lon} lat={node.lat} ")
