
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from mysql_connector import conn,sql
import json
sql = conn.cursor()
options = Options() 
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1420,1080')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
city_start = 0
child_num_max = [12, 29, 12, 7, 13, 14, 18, 29, 26, 13, 20, 19, 37, 38, 33, 16, 13, 6, 6, 4]
city_num = [1,2,3,4,5,6,7,8,10,11,12,13,14,16,17,18,20,21,22,23]
for i in range(0,19):
    try:
        test = "0"
        if city_num[i] >= 10:
            test = "0"
        else:
            test = "00"
        city_start = int(str(6001) + test + str(city_num[i])+"001")
        for i in range(0, child_num_max[i]):
            try:
                city_start += i
                for page in range(1,3):
                    print(city_start)
                    chrome.get("https://www.104.com.tw/jobs/search/?area=" + str(city_start) + "&page="+ str(page))
                    try:
                        content = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.ID, 'js-job-content')))
                    except:
                        print("no found")
                        continue
                    soup = BeautifulSoup(chrome.page_source, "html.parser")
                    content_data = soup.find("div", id = "js-job-content")
                    content_data = content_data.find_all("article")
                    for i in content_data:
                        try:
                            title = i["data-job-name"] + i["data-cust-name"]
                            print(title)
                            url = "https://" + i.find("a", class_ = "js-job-link")["href"].split("//")[1]
                            print(url)
                            chrome.get(url)
                            try:
                                content = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-header')))
                            except:
                                print("no found")
                                continue
                            soup1 = BeautifulSoup(chrome.page_source, "html.parser")
                            data = soup1.find("div", class_ = "job-address")
                            work_time = data["workperiod"].split(",")[0]
                            if data["latitude"] != "":
                                location = data["latitude"] + "|" + data["longitude"]
                            else:
                                location = ""
                            print(location)
                            salary = 0
                            if "~" in data["salary"]:
                                salary = data["salary"].replace("月薪","")
                                salary = salary.replace("元", "")
                                salary = salary.replace(",", "")
                                salary = salary.split("~")
                            elif "待遇面議" in data["salary"]:
                                salary = [-1,-1]
                            else:
                                continue
                            print(salary)
                            address = data.find("span").text.replace(" ", "")
                            with open("rent_option.json") as file_data:
                                region_data = json.load(file_data)["region"]
                            if len(address) >= 6:
                                region = address[0] + address[1] + address[2]
                                if address[4] == "區":
                                    area = address[3] + address[4]
                                else:
                                    area = address[3] + address[4] + address[5]
                                if "台" in area:
                                    area = area.replace("台","臺")
                                if "三地門" in area:
                                    area = area +"鄉"
                                with open("region_children.json") as file_data:
                                    children_option = json.load(file_data)[region]
                                region = region_data[region]
                                if region == 12 or region == 4:
                                    area = 0
                                else:
                                    for name in children_option:
                                        if name["label"] == area:
                                            area = name["value"]
                                print(region)
                                print(area)
                            print(address)
                            required = soup1.find("div", class_ = "job-requirement-table row")
                            required = required.find_all("div", class_ = "list-row row mb-2")
                            required = required[0].text.replace(" ", "")
                            required = required.split("工作經歷")[1]
                            if "不拘" in required:
                                required = 99
                            else:
                                required = required.split("年以上")[0]
                            print(required)
                            sql.execute("INSERT INTO job_data (title, region, area, address, salary_min, worktime, workexp, salary_max, url, location) VALUES('%s', '%s', '%s','%s',%s,'%s',%s,'%s','%s', '%s')" % (i["data-job-name"] + " " + i["data-cust-name"], region, area, address, salary[0], work_time, required, salary[1], url, location))
                            conn.commit()
                        except Exception as e:
                            print(e)
                            continue
            except Exception as e:
                print(e)
                continue
    except Exception as e:
        print(e)
        continue
chrome.close()

