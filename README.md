# 陈阳小草Iss服务器列表

使用 [flask] 构建后台。  
使用 [python-a2s] 查询服务器信息查询。

## 依赖

python-a2s flask-script

## 本地运行

运行 `python3 manage.py runserver -h 0.0.0.0 -p 8090` 用浏览器打开 [http://localhost:8090](http://localhost:8090)

## 部署

关于flask部署 [Deployment Options]。 这里放了一个我正在使用的gunicorn文件 `gunicorn.conf`。

## 更新日志

### 2020年5月27日(ver1.2.2)
- 更新了mod下载列表中的下载服务器，改用阿里云oss，现在下载速度应该不会慢了

### 2020年5月25日(ver1.2.1)
- 把head单独拿出来了
- 添加了腾讯统计

### 2020年5月24日(ver1.2.0)
- 使用flask-script构建项目
- 添加了mod下载的页面
- 添加了合作服务器列表

### 2020年5月23日(ver1.1.2)
- 把nav和footer单独拿出来了

### 2020年5月11日(ver1.1.1)
- 增加了判断服务器是否在线的方法，如果不在线则会在相应的位置留空而不是整体页面显示xx服错误

### 2020年5月10日(ver1.1.0)
- 增加了团子服的显示

### 2020年5月11日(ver1.0.1)
- 修改了templates文件的内容

### 2020年4月29日(ver1.0.0)
- 初版

## License

AGPLv3

[python-a2s]: https://github.com/Yepoleb/python-a2s
[flask]: https://flask.palletsprojects.com/en/1.1.x/
[Deployment Options]: https://flask.palletsprojects.com/en/1.1.x/deploying/
