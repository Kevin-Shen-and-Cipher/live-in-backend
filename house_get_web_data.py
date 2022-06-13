
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from mysql_connector import conn as mydb
from mysql_connector import sql as cursor
from bs4 import BeautifulSoup
import json
with open("rent_option.json",encoding="utf-8") as rent_file:
    json_data = json.load(rent_file)
    area_data = json_data["multi_area"]
    region_data = json_data["region"]
    kind_data = json_data["rent_kind"]
    shape_data = json_data["shape"]
from selenium.webdriver.common.by import By
#display = Display(visible=0, size=(1366, 768))
#display.start()
options = Options()
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1420,1080')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
for region_name,region in region_data.items():
    if region in [1,2,3,4,5,6,7]:
        continue
    chrome.get("https://rent.591.com.tw/?region="+str(region))
    print(region)
    try:
        content = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'vue-list-rent-item')))
    except:
        print("no found")
        chrome.refresh()
        continue
    nowrow = 0
    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    try:
        totalrow = soup.find("a", class_ = "pageNum-form").attrs["data-total"]
        if int(totalrow) >= 510:
            totalrow = 510
        else:
            totalrow = int(totalrow)
    except:
        totalrow = 510
    while True:
        chrome.get("https://rent.591.com.tw/?region="+str(region)+"&firstRow="+str(nowrow)+"&totalRows="+str(totalrow))
        try:
            content = WebDriverWait(chrome, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'vue-list-rent-item')))
        except:
            print("no found")
            chrome.refresh()
            continue
        soup = BeautifulSoup(chrome.page_source, 'html.parser')
        print(totalrow)
        print(nowrow)
        row = 0
        section_data = soup.find_all("section", class_= "vue-list-rent-item")
        for i in section_data:
            row += 1
            print(row)
            try:
                data_bind = i["data-bind"]
                cursor.execute("SELECT id FROM rent_house WHERE data_bind = '%s'" % data_bind)
                result = cursor.fetchall()
                if len(result) == 1:
                    print("repeat" + data_bind)
                    continue
                rent_url = i.find("a")["href"]
                print(rent_url)
                style_data = i.find("div", class_ = "rent-item-right").find("ul", class_ = "item-style").find_all("li")
                kind = kind_data[style_data[0].text]
                room = None
                if len(style_data) == 4:
                    room = style_data[1].text.split("房")[0]
                    area = style_data[2].text.split("坪")[0]
                    floor = style_data[3].text.split("/")
                else:
                    area = style_data[1].text.split("坪")[0]
                    floor = style_data[2].text.split("/")
                try:
                    area = int(area)
                except:
                    area = 0
                if len(floor) == 2:
                    floor[0] = floor[0].split("F")[0]
                    floor[1] = floor[1].split("F")[0]
                    floor = "%s,%s"% (floor[0], floor[1])
                else:
                    try:
                        floor[0] = int(floor[0])
                    except:
                        floor[0] = 0
                    floor = "%s," %(floor[0])
                region_child = (i.find("div" , class_ = "item-area").find("span").text).split("-")[0]
                with open("region_children.json",encoding="utf-8") as child:
                    child_data = json.load(child)
                child_region = child_data[region_name]
                try:
                    price = i.find("div",class_ = "item-price").text.split("元")[0]
                except:
                    price = -1
                for i in child_data[region_name]:
                    if i["label"] == region_child:
                        region_child = i["value"]
                chrome.get(rent_url)
                try:
                    title = WebDriverWait(chrome, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'house-title')))
                    title = str(title.find_element(By.TAG_NAME, "h1").text)
                except Exception as e:
                    title = ""
                    print(e)
                    continue
                soup1 = BeautifulSoup(chrome.page_source, 'html.parser')
                try:
                    map_section = soup1.find("div", class_= "jump-google-map")
                    location = map_section.find("div", class_ = "lat-lng").text
                except:
                    location = "0°0'0\"N 0°0'0\"E"
                corrd = location.split(" ")
                location = "[%s,%s,%s,%s,%s,%s]" % (corrd[0].split("°")[0], corrd[0].split("°")[1].split("'")[0], corrd[0].split("°")[1].split("'")[1].split("\"")[0], corrd[1].split("°")[0], corrd[1].split("°")[1].split("'")[0], corrd[1].split("°")[1].split("'")[1].split("\"")[0])
                option_section = soup1.find_all("div" , class_ = "service-list-item del")
                offer_list = {"冰箱" : 1, "洗衣機" : 1, "電視" : 1,"冷氣" : 1,"熱水器" : 1,"床" : 1,"衣櫃" : 1,"第四台" : 1,
                "網路" : 1, "天然瓦斯" : 1,"沙發" : 1,"桌椅" : 1,"陽台" : 1,"電梯" : 1,"車位" : 1}
                for option_section_data in option_section:
                    offer_list[option_section_data.find("div", class_ = "text").text] = 0
                try:
                    shape = soup1.find("div", class_ = "house-pattern").find_all("span")
                    shape = shape[len(shape)-1].text
                    shape = shape_data[shape]
                except:
                    shape = "5"
                notice_id = 1
                try:
                    rent_rule = soup1.find("div", class_ = "service-rule").find("span").text
                    if "此房屋限男生租住" in rent_rule:
                        notice_id = 2
                    elif "此房屋限女生租住" in rent_rule:
                        notice_id = 1
                except:
                    print("no rule")
                try:
                    cursor.execute("INSERT INTO option_data (cold, washer, icebox, hotwater, naturalgas, broadband, bed) VALUES('%s', '%s','%s','%s','%s','%s','%s')" % (offer_list["冷氣"], offer_list["洗衣機"], offer_list["洗衣機"], offer_list["熱水器"], offer_list["天然瓦斯"], offer_list["網路"], offer_list["床"]))
                    mydb.commit()
                    option_id = cursor.lastrowid
                    cursor.execute("INSERT INTO other_data (cartplace, lift, balcony_1) VALUES('%s', '%s', '%s')" % (offer_list["車位"], offer_list["電梯"], offer_list["陽台"]))
                    mydb.commit()
                    other_id = cursor.lastrowid
                    cursor.execute("SELECT id FROM rent_house WHERE data_bind = '%s'" % (data_bind))
                    result = cursor.fetchall()
                    cursor.execute("INSERT INTO rent_house (region, region_value, price, area, floor, notice_id, room, option_data_id, other_id, kind, shape, rent_url, data_bind, location, title) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s')" % (region, region_child, price, area, floor, notice_id, room, option_id, other_id, kind, shape, rent_url,data_bind ,location, title))
                    result = cursor.rowcount
                    if result == 1:
                        print("insert finish")
                    mydb.commit()
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        if int(nowrow) + 30 >= int(totalrow) :
            break
        else:
            nowrow += 30
chrome.close()
