## 一个基于Flask的Restful应用程序模板

包含用户表、用户登录、用户注册、用户登出和用户验证的一个Startup模板。


#运行
`
pipenv install
pipenv shell

python app.py
`

在Linux下部署时使用

参考文章
https://blog.csdn.net/whatday/article/details/106471551

`
gunicorn app:app -b 0.0.0.0:5000 -D -p app.pid -w 4 --reload
`

代理设置参考

https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/#proxy-setups


参考文章

[1] [RESTful API 最佳实践](https://www.dreamer.im/2019/04/13/%E9%9A%8F%E7%AC%94/RESTful%20API%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/)



