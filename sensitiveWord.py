#!/usr/bin/python
#-*- coding:utf-8 -*-
# README:
# prepare:
#   brew install tesseract / apt-get install tesseract-ocr
#   pip install Pillow
#   pip install pytesseract
from PIL import Image
import pytesseract

import os
import sys
import getopt

imgExt = ['.gif', '.jpg', '.jpeg', '.png', '.bmp']

sensitiveWords = ["最", "最佳", "最具", "最爱", "最赚", "最优", "最优秀", "最好", "最大", "最大程度", "最高", "最高级", "最高端", "最奢侈", "最低", "最低级", "最低价", "最底", "最便宜", "史上最低价", "最流行", "最受欢迎", "最时尚", "最聚拢", "最符合", "最舒适", "最先", "最先进", "最先进科学", "最后", "最新", "最新技术", "最新科学  ", "第一", "中国第一", "全网第一", "销量第一", "排名第一", "唯一", "第一品牌", "NO.1", "TOP1", "独一无二", "全国第一", "遗留", "一天", "仅此一次", "仅此一款", "最后一波", "全国X大品牌之一", "销冠", "国家级", "国际级", "世界级", "千万级", "百万级", "星级", "5A", "甲级", "超甲级  ", "顶级", "顶尖", "尖端", "顶级享受", "高级", "极品", "极佳", "绝佳", "绝对", "终极", "极致", "致极", "极具", "完美", "绝佳", "极佳", "至", "至尊", "至臻", "臻品", "臻致", "臻席", "压轴", "问鼎", "空前", "绝后", "绝版", "无双", "非此莫属", "巅峰", "前所未有", "无人能及", "顶级", "鼎级", "鼎冠", "定鼎", "完美", "翘楚之作", "不可再生", "不可复制", "绝无仅有", "寸土寸金", "淋漓尽致", "无与伦比", "唯一", "卓越", "卓著", "前无古人后无来者", "绝版", "珍稀", "臻稀", "稀少", "绝无仅有", "绝不在有", "稀世珍宝", "千金难求", "世所罕见", "不可多得", "空前绝后", "寥寥无几", "屈指可数", "独家", "独创", "独据", "开发者", "缔造者", "创始者", "发明者", "首个", "首选", "独家", "首发", "首席", "首府", "首选", "首屈一指", "全国首家", "国家领导人", "国门", "国宅", "首次", "填补国内空白", "国际品质  ", "首家", "首", "黄金旺铺", "黄金价值", "黄金地段", "金钱", "金融汇币图片", "外国货币  ", "大牌", "金牌", "名牌", "王牌", "领先上市", "巨星", "著名", "掌门人", "领袖品牌", "至尊", "冠军", "王", "之王", "王者楼王", "墅王", "皇家", "领头羊", "世界领先", "领先", "遥遥领先", "领导者", "领袖", "引领", "创领", "领航", "耀领", "史无前例", "前无古人", "永久", "万能", "百分之百", "绝无仅有", "特供", "专供", "专家推荐", "国家xx领导人推荐", "点击领奖", "恭喜获奖", "全民免单", "点击有惊喜", "点击获取", "点击转身", "领取奖品", "抽奖", "售罄", "售空", "再不抢就没了", "史上最低价", "不会再便宜", "没有他就xx", "错过不再", "错过即无", "错过就没机会了", "未曾有过的", "万人疯抢", "全民疯抢", "全民抢购", "免费领", "免费住", "0首付", "免首付", "零距离", "价格你来定"]

class Usage(Exception):
    def __init__(self, msg=''):
        self.msg = msg

def scan(path):
    dir = os.path.abspath(path)
    if not os.path.exists(dir):
        exit ("Error: %s is not Exist" % (dir))
    for (root, dirs, files) in os.walk(dir):
        for filename in files:
            filter(os.path.join(root,filename))
        for dirc in dirs:
            scan(os.path.join(root,dirc))

def filter(file):
    (filename,extension) = os.path.splitext(file)
    if extension in imgExt:
        lines = pytesseract.image_to_string(Image.open(file), lang='chi_sim').encode('utf-8')
        lines = lines.split("\n")
        for line in lines:
            for word in sensitiveWords:
                if line.find(word)>=0:
                    print file, lines
    else:
        f = open(file)
        lines = f.readlines()
        cnt = 0
        for line in lines:
            cnt += 1
            if not line:
                break
            for word in sensitiveWords:
                if line.find(word)>=0:
                    print word, file, 'Line: ', cnt, line
        f.close()

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hr:", ["help", "dir="])
            for o, a in opts:  
                if o in ("-h", "--help"):
                    exit ("Usage: python sensitiveWord.py [-d] /path/to/scan/dir")
                if o in ("-r", "--dir"):
                    scan(a)
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())