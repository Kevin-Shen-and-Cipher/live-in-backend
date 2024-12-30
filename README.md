# LiveIn Backend
ubuntu 18.04
python 3.6.9
python 2.7.17
mysql 14.14
apache 2.4.29

## Quick Start
### Requirement 
* docker 
* docker-compose 
* 填入重要資訊給 `./live_in_backend/.env`
```env
# PostgreSQL
POSTGRES_HOST= # 如果用 container，直接寫 container name 
POSTGRES_DB=live_in_backend
POSTGRES_USER= # superuser: postgres
POSTGRES_PASSWORD=
POSTGRES_PORT=5432

# Google API
GOOGLE_MAP_API_KEY=

# SECRET_KEY
SECRET_KEY=  # 任意填入， django 用於加密用
```
* 使用 `docker-compose --env-file ./live_in_backend/.env up -d ` 開啟
    * 如果兩個服務中有東西建立失敗，可用 `docker exec -it <container name> bash` 來見查
* **First start 則需要在加入兩個指令**
```
docker exec -it live_in_backend bash
# 進入 live_in_backend container 
live_in_backend# python manage.py migrate
live_in_backend# python manage.py loaddata
```

## API

### Job

#### Get Jobs
- Request Method：GET
- Request URL：`/api/jobs/`
- Request Query String Parameters：
  - required

    ```json5
    {
       // your home address
       // string
       "address": "your-home-address"
    }
    ```
    
  - optional

    ```json5
    {
      // your can find jsons in default_data folder
      // number, refer by pk field in distrcit.json
      "district": 1,
      // job salary
      // number, the minium salary can accept
      "salary": 30000,
      // job position
      // number, refer by pk field in job_position.json
      "job_position": 1,
      // working hour of job
      // number, refer by pk field in working_hour.json
      "working_hour": 1
    }
    ```

#### Create Job
- Request Method：POST
- Request URL：`/api/jobs/`
- Request Body：
  - required

    ``` json5
    {
       // job name
       // string, max length:100
       "name":"test job",
       // job salary
       // number
       "salary": 50000,
       // number of needed working experience
       "tenure": 3,
       // job company address
       // string, max length:100
       "address": "job company address",
       // job company coordinate
       // string, max length:50
       "coordinate":"25.02454,121.30551" ,
       // job url
       // string, max length:300
       "url":"https://www.google.com/",
       // number, refer by pk field in district.json
       "district":1,
       // number, refer by pk field in job_position.json
       "job_position":1,
       // number, refer by pk field in working_hour.json
       "working_hour":1,
       // job benefits
       "benefit":[
          {
             // string, max length:30
             "name": "free bananas"
          }
       ]
    }
    ```

### Apartment

#### Get apartments
- Request Method：GET
- Request URL：`/api/apartments/`
- Request Query String Parameters：
  - required

    ```json5
    {
       // your job address
       // string
       "address": "your-job-address"
    }
    ```
    
  - optional

    ```json5
    {
       // your can find jsons in default_data folder
       // number, refer by pk field in distrcit.json
       "district": 1,
       // apartment price
       // number
       "price": 30000,
       // number, refer by pk field in rent_type.json
       "rent_type": [1],
       // number, refer by pk field in apartment_type.json
       "apartment_type": [1],
       // number, refer by pk field in room_type.json
       "room_type": [1],
       // number, refer by pk field in restrict.json
       "restrict": [1,2],
       // number, refer by pk field in device.json
       "device": [1,2]
    }
    ```

#### Create apartment
- Request Method：POST
- Request URL：`/api/apartments/`
- Request Body：
  - required

    ``` json5
    {
       // apartment name
       // string, max length:100
       "name":"test apartment",
       // number
       "price": 30000,
       // apartment coordinate
       // string, max length:50
       "coordinate":"25.02454,121.30551",
       // apartment url
       // string, max length:300
       "url":"https://www.google.com/",
       // number, refer by pk field in distrcit.json
       "district": 1,
       // number, refer by pk field in rent_type.json
       "rent_type": 1,
       // number, refer by pk field in apartment_type.json
       "apartment_type": 1,
       // number, refer by pk field in room_type.json
       "room_type": 1,
       // number, refer by pk field in restrict.json
       "restrict": 1,
       // number, refer by pk field in device.json
       "device": 1,
       "surrounding_facility":[
         {
             "name":"MRT",
              // number, refer by pk field in facility_type.json
             "facility_type": 1
         }
       ]
    }
    ```


