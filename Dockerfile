FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
#apt-get源 使用163的源
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
    echo "deb http://mirrors.163.com/debian/ jessie main non-free contrib" >/etc/apt/sources.list && \
    echo "deb http://mirrors.163.com/debian/ jessie-proposed-updates main non-free contrib" >>/etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/debian/ jessie main non-free contrib" >>/etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/debian/ jessie-proposed-updates main non-free contrib" >>/etc/apt/sources.list
RUN apt-get update & apt-get install -y nginx

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt

COPY . /code/
RUN cp default /etc/nginx/sites-enabled/

# 设定对外端口
EXPOSE 80
# 设定启动命令
CMD ['/etc/init.d/nginx','restart']
CMD ['uwsgi' ,"--ini",'uwsgi.ini']
CMD ["python3", "manage.py", "collectstatic"]
CMD ['/etc/init.d/nginx','restart']