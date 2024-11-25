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
* `docker-compose 
* 填入重要資訊給 env
```env
# PostgreSQL
POSTGRES_HOST= #填入 database 的 container name 
POSTGRES_DB=live_in_backend
POSTGRES_USER= # 填入 docker-compose.yml 中的 `service>database>environment>POSTGRES_USER`
POSTGRES_PASSWORD= # 填入 docker-compose.yml 中的 `service>database>environment>POSTGRES_PASSWORD`
POSTGRES_PORT=5432

# Google API
GOOGLE_MAP_API_KEY=

# SECRET_KEY
SECRET_KEY= # 任意填入， django 用於加密用

```
* 使用 `docker-compose up --build` 開啟
    * 如果兩個服務中有東西建立失敗，可用 `docker-compose exec <container name> bash` 來見查