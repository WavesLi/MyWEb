#   flask 中的路由相关

### 1——>flask url_for() 和 redirect的区别
>   1、edirect直接是url，就是app.route的路径参数。

>   2、url_for()是对函数进行操作。获取的是该函数对应的路由信息

        from flask import Flask,request,redirect,url_for,render_template,Response,jsonify,make_response
        app = Flask(__name__)
        
        
        @app.route('/a')
        def a():
            return redirect(url_for('ccc222'))#url_for直接对函数访问
        
        @app.route('/b')
        def b():
            return redirect("http://127.0.0.1:5000/ccc111")#redirect直接对route的路径访问
        
        
        @app.route('/ccc111')
        def ccc222():
            return "我是ccc"
        
        
        if __name__ == '__main__':
            app.debug = True # 设置调试模式，生产模式的时候要关掉debug
            app.run()
>   访问127.0.0.1/a和127.0.0.1/b都能成功显示"我是ccc"，但是

>   a使用return redirect(url_for('ccc222'))

>   b使用return redirect("http://127.0.0.1:5000/ccc111")  

>   url_for()还可以用来构造url，就比如说，url('static',filename='1.png')，代表我访问static/1.png就可以直接访问到这张图片，还是很有用的这个函数。
        

   
   
### 2——>flask 中的转换器 [具体见详情](https://www.jianshu.com/p/1ebaf00f6df0)