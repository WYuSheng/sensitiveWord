FROM tesseractshadow/tesseract4re
# COPY sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python python-pip python-dev build-essential
RUN pip install Pillow
RUN pip install pytesseract

ADD sensitiveWord.py /home/work/sensitiveWord.py
