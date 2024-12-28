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