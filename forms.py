from flask_wtf import FlaskForm #引入FlaskForm类，作为自定义Form类的基类，
# 是一个用于表单处理,校验并提供csrf验证的功能的扩展库
'''
作用: Flask-wtf能保护所有表单免受跨站请求伪造的攻击(Cross-Site Request Forgery,CSRF),恶意网站会把请求发送到被攻击者登录的
其他网站就会引起CSRF攻击,因此我们需要实现CSRF保护机制,Flask-wtf采用的做法是为程序设置一个秘钥,Flask-WTF 使用这个密钥生成加
密令牌,再用令牌验证请求中表单数据的真伪。
'''
 #StringField对应HTML中type="text"的<input>元素，SubmitField对应type='submit'的<input>元素
from wtforms import StringField,SubmitField,SelectField
#引入验证函数,我感觉就是对用户输入的一种检查：排除非法输入
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired
#
class GetAgentSecretKeyForm(FlaskForm):
    #GetAgentSecretKeyForm表单有四个字段，
    # 字段（StringField和SubmitField）的构造函数的第一参数对应HTML的标号（用以显示的字）
    #SelectField，下拉列表
    agent_id = StringField('商家ID',validators=[DataRequired()])
    agent_create_time = StringField('商家创建时间',validators=[DataRequired()])
    secret_key_type = SelectField(label='密钥类型',choices=[('sm4','新国密'),('old','旧密钥')],coerce=str,default='old')
    submit = SubmitField('提交')

class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')

class GetCheckCodeForm(FlaskForm):
    input_string = StringField('请按接口文档要求输入拼接好的字符串',validators=[DataRequired()])
    submit = SubmitField('提交')

class FileDecryptForm(FlaskForm):
    file = FileField(label='选择加密文件',validators=[FileRequired(),])
    submit = SubmitField('单击解密')

class LoginForm(FlaskForm):
    #基本参数
    ipport = SelectField(label='安全接入', choices=[('1', '江苏'), ('2', '吉林')], coerce=str, default='江苏')
    PartnerId = StringField('商家id', validators=[DataRequired()])
    TimeStamp = StringField('时间戳', validators=[DataRequired()])
    SerialNum = StringField('序列号', validators=[DataRequired()])
    Version = StringField('版本号', validators=[DataRequired()])
    Token = StringField('token', validators=[DataRequired()])
    #业务参数
    UserId=StringField('用户id',validators=[DataRequired()])
    LoginPass = StringField('用户密码', validators=[DataRequired()])
    LoginType = StringField('logintype', validators=[DataRequired()])
    MacAddress=StringField('mac地址', validators=[DataRequired()])
    secret_key = StringField('秘钥', validators=[DataRequired()])
    submit = SubmitField('提交')