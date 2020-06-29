from flask import Flask
from flask import request,render_template

import requests
from hzjflask.util import access_tool
from hzjflask.util import myrequest
from flask_bootstrap import  Bootstrap
import forms

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'hard to guess string'        #设置app的config字典
#采用字典的方式存储框架,扩展和程序本身的配置变量,一般秘钥不直接写入代码,放在环境变量增加安全性.
# @app.route('/')
# def hello_world():
#     return 'Hello World!aaa'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route("/aa",methods=['GET','POST'])
def aa():
    name = None
    form = forms.NameForm()
    if form.validate_on_submit():
    #服务器收到没有表单数据的GET请求 ，因此form.validate_on_submit() == False
        name = form.name.data
    #不执行，跳过
        form.name.data=''
    #不执行 ，跳过
    return render_template('aa.html',name=name,form=form)
    #把name,form变量传入模板，渲染，返回给客户端
@app.route('/get.html')
def get_html():
    # 使用render_template()方法重定向到templates文件夹下查找get.html文件
    return render_template('get.html')

# 配置路由，当请求post.html时交由post_html()处理
@app.route('/post.html')
def post_html():
    # 使用render_template()方法重定向到templates文件夹下查找post.html文件
    return render_template('post.html')

# 配置路由，当请求deal_request时交由deal_request()处理
# 默认处理get请求，我们通过methods参数指明也处理post请求
# 当然还可以直接指定methods = ['POST']只处理post请求, 这样下面就不需要if了
@app.route('/deal_request', methods = ['GET', 'POST'])
def deal_request():
    if request.method == "GET":
        # get通过request.args.get("param_name","")形式获取参数值
        get_q = request.args.get("q","")
        return render_template("result.html", result=get_q)
    elif request.method == "POST":
        # post通过request.form["param_name"]形式获取参数值
        post_q = request.form["q"]
        return render_template("result.html", result=post_q)

@app.route('/getAgentSecretKey/',methods=['GET','POST'])
def get_agent_secret_key():
    '''
    :return: 商家密钥
    '''
    secret_key = None
    form = forms.GetAgentSecretKeyForm()
    if form.validate_on_submit():
        agent_id = form.agent_id.data
        agent_create_time = form.agent_create_time.data
        if form.secret_key_type.data == 'sm4':
            secret_key = access_tool.get_new_agent_key(agent_id,agent_create_time)
        elif form.secret_key_type.data == 'old':
            secret_key = access_tool.get_agent_key(agent_id,agent_create_time)
    return render_template('getAgentKey.html', form=form, secret_key=secret_key)

@app.route('/getCheckCode/',methods=['GET','POST'])
def get_check_code():
    check_code = None
    form = forms.GetCheckCodeForm()
    if form.validate_on_submit():
        input_string = form.input_string.data
        form.input_string.data = ''
        check_code = access_tool.get_check_code(input_string)
    return render_template('getCheckCode.html',form=form,check_code=check_code)

@app.route('/fileDecrypt/',methods=['GET','POST'])
def file_decrypt():
    decrypt_file_content = None
    form = forms.FileDecryptForm()
    if form.validate_on_submit():
        encypte_file_content = form.file.data.read()
        decrypt_file_content = access_tool.file_content_decrypt(encypte_file_content)
    return render_template('fileDecrypt.html', form=form, decrypt_file_content=decrypt_file_content)

@app.route('/login/',methods=['GET','POST'])
def login():
    response = None
    form = forms.LoginForm(PartnerId='00101',TimeStamp='2016-10-24 15:10:10',secret_key='92DD0FDBB4FD73DD29F0696F')
    if form.validate_on_submit():

        req_content = {
            "PartnerId": form.PartnerId.data,
            "TimeStamp": form.TimeStamp.data,
            "SerialNum": form.SerialNum.data,
            "Version": form.Version.data,
            "Token": form.Token.data,
            "ReqContent": {
                "Userid": form.UserId.data,
                "LoginPass": form.LoginPass.data,
                "LoginType": form.LoginType.data,
                "MacAddress":form.MacAddress.data
            }
        }

        secret_key=form.secret_key.data
        if form.ipport.data == '1':

            url = "http://10.10.32.236:8941/secret/common/lottLogin?partnerId="+ form.PartnerId.data+"&hashType=md5&hash="

        else:
            url = "http://10.10.22.236:8941/secret/common/lottLogin?partnerId="+ form.PartnerId.data+"&hashType=md5&hash="
        response = myrequest.myrequest().post(url, req_content, secret_key)

    return render_template('login.html',form=form,response=response)


if __name__ == '__main__':
    app.run()

