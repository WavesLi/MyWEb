#   flask-cors的使用方式
####    相关连接-https://blog.csdn.net/qq_37193537/article/details/90787198

## flask-cors.CORS 是用来全局指定跨域许可方式
>####    1、CORS(app) 指定全局跨域，权限为：所有域到所有routes
>####    2、CORS(app, resources={r"/api/\*": {"origins": "*"}})
                r"/api/\*": 指定所有以 api/的toutes
                {"origins": "*"}: 指定所有的域的访问来源
## 适用@cross_origin()装饰器
        @app.route("/")
        @cross_origin()
        def helloWorld():
          return "Hello, cross-origin-world!"