# 邮件类，用来给指定用户发送邮件，可指定多个收件人，可带附件
import re,smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror,error
from utils.log import logger


class Email:
    def __init__(self,server,sender,password,receiver,title,message=None,path=None):
        """初始化Email
               :param title: 邮件标题，必填。
               :param message: 邮件正文，非必填。
               :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
               :param server: smtp服务器，必填。
               :param sender: 发件人，必填。
               :param password: 发件人密码，必填。
               :param receiver: 收件人，多收件人用“；”隔开，必填。
               """
        self.title = title
        self.message = message
        self.files = path
        self.msg = MIMEMultipart('related')
        self.server = server
        self.sender = sender
        self.receiver = receiver
        self.password = password

    def _attach_file(self,att_file):
        #将单个文件添加到附件中
        att = MIMEText(open('%s' % att_file,'rb').read(),'plain','utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]',att_file)
        att["Content-Disposition"] =  'attachment;filename="%s"'% file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))


    def send(self):
        self.msg['Subject'] = self.title #发送头部信息
        self.msg['From'] = self.sender #发送者
        self.msg['To'] = self.receiver  #接收者

        #邮件正文、
        if self.message:
            self.msg.attach(MIMEText(self.message))

        #添加附件，支持多种附件（传入list),或者单个附件（传入str)
        if self.files:
            if isinstance(self.files,list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files,str):
                self._attach_file(self.files)

        #链接服务器发送
        try:
            smtp_server = smtplib.SMTP(self.server) #链接SMTP服务
        except(gaierror and error) as e: #链接方面的错误
            logger.exception("发送失败，无法连接服务器，检测网络.%s",e)
        else:
            try:
                smtp_server.login(self.sender,self.password)
            except smtplib.SMTPAuthenticationError as e:  #账户验证失败  未开启SMTP或者密码不对 或者没有授权码
                logger.exception("用户密码验证失败！%s" ,e)
            else:
                smtp_server.sendmail(self.sender,self.receiver,self.msg.as_string())#发送邮件
            finally:
                smtp_server.quit()#关闭STMP
                logger.info('发送邮件成功，如没有，请查看垃圾邮箱'.format(self.title,self.receiver))



