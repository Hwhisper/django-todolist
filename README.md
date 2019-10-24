# django-todolist

1. 打开todolist/settings.py文件，注册todo应用, 安装djangorestframework 和django-cors-headersh后，更新INSTALLED_APPS：

![imag](https://github.com/Hwhisper/django-todolist/blob/master/image/settings1.png)

根据报错信息添加如下代码：

![imag](https://github.com/Hwhisper/django-todolist/blob/master/image/settings2.png)

![imag](https://github.com/Hwhisper/django-todolist/blob/master/image/settings3.png)

2. 定义todo应用模型，打开文件todo/model.py,编写模型：

![imag](https://github.com/Hwhisper/django-todolist/blob/master/image/models.png)

3. 配置todo应用并注册（todo/admin.py)：

![imag](https://github.com/Hwhisper/django-todolist/blob/master/image/admin.png)

4. 创建序列化程序将模型实例转换为JSON，以便前端可以轻松处理接收到的数据。在todo目录下创建新文件serializers.py：

![imag](https://github.com/Hwhisper/django-todolist/blob/master/image/JSON.png)

5. 创建view视图，提供CRUD操作的实现，以及指定序列化程序类和查询集。在todo/views.py创建Todoview类：

![imag](https://github.com/Hwhisper/django-todolist/blob/master/image/views.png)

6. 编写todolist/urls.py文件:使得路由器类允许以下查询：

/todos/ 这将返回所有Todo项的列表：

![imag](https://github.com/Hwhisper/django-todolist/blob/master/image/urls.png) 
