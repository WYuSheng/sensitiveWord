### 敏感词扫描docker
Usage:
1. docker run  注意扫描目录需映射进docker内
docker run \
    --name=sensitive-d \
    -itd \
    -v /home/ubuntu/data/github/sensitiveWord/test:/home/work/test \
    --restart=always \
    --privileged \
    sensitive:0.1.0
2. 进入docker, python sensitiveWord.py -r test(相对或绝对路径)



#####附录（可以忽略）
docker run \
    --name=sensitive \
    -itd \
    -v /home/ubuntu/data/github/sensitiveWord:/home/work/sensitiveWord \
    --restart=always \
    --privileged \
    tesseractshadow/tesseract4re:latest