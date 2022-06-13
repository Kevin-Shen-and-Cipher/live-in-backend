
import json


from mysql_connector import conn,sql
import requests
import get_lat_lng


google_map_API_key = "YOUR API KEY"

def area_check(area_size,data):
    print(data)
    out_flag= False
    if data != []:
            out_flag= True
            if "50_" in data:
                if area_size >= 50:
                    out_flag = False
            if "40_50" in data:
                if area_size >= 40 and area_size < 50:
                    out_flag = False
            if "30_40" in data:
                if area_size >= 30 and area_size < 40:
                    out_flag = False
            if "20_30" in data:
                if area_size >= 20 and area_size < 30:
                    out_flag = False
            if "10_20" in data:
                if area_size >= 10 and area_size < 20:
                    out_flag = False
            if "0_10" in data:
                if area_size >= 0 and area_size < 10:
                    out_flag = False
    return out_flag

def floor_check(floor,data):
    try:
        out_flag= False
        if data != []:
                out_flag= True
                floor_data = floor.split(",")
                for floor in floor_data:
                    if "12_" in data:
                        if int(floor) >= 12:
                            out_flag = False
                    if "6_12" in data:
                        if int(floor) >= 6 and int(floor) < 12:
                            out_flag = False
                    if "2_6" in data:
                        if int(floor) >= 2 and int(floor) < 6:
                            out_flag = False
                    if "0_1" in data:
                        if int(floor) >= 0 and int(floor) < 1:
                            out_flag = False
        return out_flag
    except:
        return True

def notice_check(data_id,data):
    print(data)
    out_flag= False
    if data != []:
        if "all_sex" in data:
            if data_id == 1:
                out_flag = False
        if "boy" in data:
            if data_id == 2:
                out_flag = False
        if "girl" in data:
            if data_id == 3:
                out_flag = False
    return out_flag

def price_check(price,data):
    print(data)
    try:
        out_flag= False
        price = int(price)
        print(price)
        if data != []:
                out_flag= True
                if "1000000" in data:
                    if price >= 40000:
                        out_flag = False
                if "40000" in data:
                    if price >= 30000 and price < 40000:
                        out_flag = False
                if "30000" in data:
                    if price >= 20000 and price < 30000:
                        out_flag = False
                if "20000" in data:
                    if price >= 10000 and price < 20000:
                        out_flag = False
                if "10000" in data:
                    if price >= 5000 and price < 10000:
                        out_flag = False
                if "5000" in data:
                    if price >= 0 and price < 5000:
                        out_flag = False
        return out_flag
    except:
        return True


def room_check(room,data):
    print(data)
    out_flag= False
    if data != []:
            out_flag= True
            if "1" in data:
                if room == 1:
                    out_flag = False
            if "3" in data:
                if room == 3:
                    out_flag = False
            if "2" in data:
                if room == 2:
                    out_flag = False
            if "4" in data:
                if room >= 4:
                    out_flag = False
    return out_flag

def option_check(option_id,data):
    print(data)
    if data != []:
        sql.execute("SELECT * FROM option_data WHERE id = '%s'" % option_id)
        result = sql.fetchall()
        result = result[0]
        if "cold" in data:
            if result[1] == 0:
                return True
        if "washer" in data:
            if result[2] == 0:
                return True 
        if "icebox" in data:
            if result[3] == 0:
                return True 
        if "hotwater" in data:
            if result[4] == 0:
                return True 
        if "naturalgas" in data:
            if result[5] == 0:
                return True 
        if "broadband" in data:
            if result[6] == 0:
                return True 
        if "bed" in data:
            if result[7] == 0:
                return True 
        return False
    return False
    
def other_check(other_id,data):
    print(data)
    if data == []:
        return False
    sql.execute("SELECT * FROM other_data WHERE id = '%s'" % other_id)
    result = sql.fetchall()
    result = result[0]
    if "cartplace" in data:
        if result[1] == 0:
            return True
    if "lift" in data:
        if result[2] == 0:
            return True 
    if "balcony_1" in data:
        if result[3] == 0:
            return True 
    return False

def kind_check(kind,data):
    print(data)
    if data == []:
        return False
    if str(kind) not in data:
        return True
    return False

def shape_check(shape,data):
    print(data)
    if data == []:
        return False
    if str(shape) not in data:
        return True
    return False

def get_house(address,area,filter_data):
    with open("/var/www/python-flask/uwsgi/python-flask-test/rent_option.json", encoding="utf-8") as file_data:
        region_data = json.load(file_data)["region"]
    with open("/var/www/python-flask/uwsgi/python-flask-test/region_children.json", encoding="utf-8") as file_data1:
        child_data = json.load(file_data1)
    region_name = ""
    area_name = ""
    origin_location = get_lat_lng.get_corrd(address)
    sql.execute("SELECT data_bind, rent_url ,location, title, price, area, floor, notice_id, room, option_data_id, other_id, kind, shape FROM rent_house WHERE region_value IN (%s)" % (", ".join(area)))
    result = sql.fetchall()
    response_data = []
    house_count = 0
    for i in result:
        if area_check(i[5],filter_data["multi_area"]):
            continue
        if floor_check(i[6],filter_data["multi_floor"]):
            continue
        if notice_check(i[7], filter_data["multi_notice"]):
            continue
        if price_check(i[4], filter_data["multi_price"]):
            continue
        if room_check(i[8], filter_data["multi_room"]):
            continue
        if option_check(i[9], filter_data["option_set"]):
            continue
        if other_check(i[10], filter_data["other"]):
            continue
        if kind_check(i[11], filter_data["rentKind"]):
            continue
        if shape_check(i[12], filter_data["shape"]):
            continue
        location = json.loads(i[2])
        house_count += 1
        #response_data.append({"title": i[3],"url": i[1]})
        lat = float(location[0]) + (float(location[1]) / float(60)) + (float(location[2]) / float(3600))
        lng = float(location[3]) + (float(location[4]) / float(60)) + (float(location[5]) / float(3600))
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+str(origin_location["lat"])+"%2C"+str(origin_location["lng"])+"&destinations="+str(lat)+"%2C"+str(lng)+"&key=" + google_map_API_key
        #print(url)
        response = requests.request("GET", url, headers={}, data={}).json()
        #print(response)
        response_data.append({"title": i[3],"url": i[1], "distance" :response["rows"][0]["elements"][0]["distance"]["text"].split(" ")[0]})
        if house_count >= 10:
            break
    response_data = sorted(response_data, key=lambda x: x['distance'])
    return response_data
