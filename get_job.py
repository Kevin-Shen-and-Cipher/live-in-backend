from dataclasses import dataclass
import json
from mysql_connector import conn,sql
import requests
import get_lat_lng


google_map_API_key = "YOUR API KEY"

def salary_check(salary_min, salary_max, data):
    if data == []:
        return False
    if "1" == data:
        if salary_min != -1:
            return False
    if "2" == data :
        if salary_max >=30000:
            return False
    if "3" == data:
        if salary_max >=40000:
            return False
    if "4" == data:
        if salary_max >=50000:
            return False
    return True

def exp_check(exp,data):
    if data == []:
        return False
    if "0" in data:
        if exp == 99:
            return False
    if "1" in data:
        if exp >= 1 and exp < 3:
            return False
    if "3" in data:
        if exp >= 3 and exp < 5:
            return False
    if "5" in data:
        if exp >= 5 and exp < 10:
            return False
    if "10" in data:
        if exp >= 10:
            return False
    return True

def work_time_check(work_time,data):
    if data == []:
        return False
    for i in data:
        if i in work_time:
            return False
    return True

def get_job(address, area, filter_data):
    with open("/var/www/python-flask/uwsgi/python-flask-test/region_children.json", encoding="utf-8") as file_data1:
        child_data = json.load(file_data1)
    region_name = ""
    area_name = []
    for name,data in child_data.items():
        for i in area:
            for value in data:
                if value["value"] == int(i):
                    area_name.append(value["label"])
                    region_name = name
    origin_location = get_lat_lng.get_corrd(address=address)
    sql.execute("SELECT title, url, address, location, salary_min, salary_max, workexp, worktime FROM job_data")
    result = sql.fetchall()
    response_data = []
    job_count = 0
    for i in result:
        if salary_check(i[4],i[5],filter_data["salary"]):
            continue
        if exp_check(i[6],filter_data["job-exp"]):
            continue
        if work_time_check(i[7],filter_data["working-hour"]):
            continue
        #判斷該筆資料是否屬於這個市區
        if region_name not in i[2]:
            continue

        #對應該筆資料是否在區域陣列中
        continue_flag = True
        for temp in area_name:
            if temp in i[2]:
                continue_flag = False
        if continue_flag:
            continue

        #有些資料只有地址沒有座標 所以我們需要透過google map api 尋找該筆資料
        if i[3] == "":
            try:
                deslocation = get_lat_lng.get_corrd(i[2])
                url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+str(origin_location["lat"])+"%2C"+str(origin_location["lng"])+"&destinations="+str(deslocation["lat"])+"%2C"+str(deslocation["lng"])+"&key=" + google_map_API_key
            except:
                continue
        else:
            deslocation = i[3].split("|")
            url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+str(origin_location["lat"])+"%2C"+str(origin_location["lng"])+"&destinations="+str(deslocation[0])+"%2C"+str(deslocation[1])+"&key=" + google_map_API_key
        response = requests.request("GET", url, headers={}, data={}).json()
        response_data.append({"title": i[0], "url": i[1], "distance" :float(response["rows"][0]["elements"][0]["distance"]["text"].split(" ")[0])})
        job_count += 1
        if job_count == 10:
            break
    response_data = sorted(response_data, key=lambda x: x['distance'])
    return response_data
