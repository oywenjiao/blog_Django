# 项目说明

> ## Django操作

- 生成项目依赖组件详情文件: <pre>pip freeze > requirements.tx</pre> 该命令会在项目根目录生成 <code>requirements.tx</code> 文件

- 安装项目依赖:
<pre>
pip install -r requirements.txt
</pre>

- 收集静态文件命令:
<pre>
python manage.py collectstatic
</pre>

- 创建数据库文件:
<pre>
python manage.py migrate
</pre>

- 更改数据模型后执行数据迁移:
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>

- 创建后台管理员超级用户：
<pre>
python manage.py createsuperuser
</pre>

- 配置MySQL数据库：
<pre>
1.安装mysql模块：pip install pymysql
2.在项目文件夹中的 __ini__.py 文件处导入mysql模块：
	import pymysql
	pymysql.install_as_MySQLdb()
3.修改 setting.py 文件中的 DATABASES 配置
</pre>

> ## Uwsgi操作

- 安装uwsgi:
<pre>
pip install uwsgi
</pre>

- 启动django项目：
<pre>
1.启动：uwsgi --ini uwsgi.ini
2.重载：uwsgi --reload uwsgi/uwsgi.pid
</pre>

- 关闭全部进程：
<pre>
pkill -f uwsgi -9
</pre>


> ## nginx配置

- 新增 <code>blog.conf</code> 文件，并写入以下配置内容:
```nginx
server {
        listen 80;	# 监听端口
        server_name  blog.test;	# 访问域名地址
        access_log      /data/logs/nginx/blog_access.log;
        error_log       /data/logs/nginx/blog_error.log;
        location / {
            include /data/apps/nginx/conf/uwsgi_params;
            uwsgi_pass 127.0.0.1:8008;
            uwsgi_read_timeout 2;
        }
        # 配置静态文件路径
        location /static {
            alias /data/htdocs/djangoProject/blog/static;
            index index.html index.htm;
        }
}
```


