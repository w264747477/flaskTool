import asyncio
import aiohttp
from flask import Blueprint
from flask import request
from lxml import etree
import requests
import re
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  国内镜像
mahua = Blueprint('mahua', __name__)
async def getTrueM3u8(truePageUrl):
    # 执行异步操作获取真正的m3u8
    # 点击进入播放页面
    async with aiohttp.ClientSession() as session:
        async with session.get(truePageUrl) as resp:
    truePageResp = requests.get(truePageUrl)
    truePageResp.encoding = 'utf-8'
    # 定义re的解析数据
    reRule = re.compile(
        r'.*?"link_pre":.*?, "url":(?P<videoM3u8>.*?),"url_next":', re.S)
    res = reRule.finditer(truePageResp.text)
    for it in res:
        # print(it.group('name'))
        # print(it.group('year').strip())
        # print(it.group('average').strip())
        # print(it.group('personNum').strip())
        dic = it.groupdict()
        dic['videoM3u8'] = dic['videoM3u8'].strip()
        trueUrl = repr(dic['videoM3u8'])
        print(trueUrl)


@mahua.route('/', methods=['GET'])
def mainMahua():
    video_name = request.args.get('videoName')
    videoFormat = eval(video_name)
    preurl = 'https://www.mahua110.com/search/-------------.html?wd=' + videoFormat + '&submit='
    asyncio.run(query_by_name(preurl))


async def query_by_name(preurl):
    returnlist = []  # 返回数组
    # 根据用户传过来的影片名字搜索
    resp = requests.get(preurl)
    resp.encoding = 'utf-8'
    html = etree.HTML(resp.text)
    # 获取搜索的视频资源 li
    searchLis = html.xpath('//*[@id="searchList"]/li')
    for sLi in searchLis:
        tasks = []  # 异步任务数组
        sliUrl = sLi.xpath('.//div[2]/p[5]/a[2]/@href')
        liUrl = sliUrl[0]
        # 获取详情页
        detailPageUrl = 'https://www.mahua110.com' + liUrl
        # 点击进入详情页
        detailResp = requests.get(detailPageUrl)
        detailResp.encoding = 'utf-8'
        htmlDetail = etree.HTML(detailResp.text)
        # 详情页获取所有集数
        playPageList = htmlDetail.xpath('//*[@id="play_down1"]/ul/li')
        for playPage in playPageList:
            playPageUrl = playPage.xpath('./a/@href')
            for playP in playPageUrl:
                truePageUrl = 'https://www.mahua110.com' + playP
                tasks.append(getTrueM3u8(truePageUrl))
                print(truePageUrl)
                # 执行异步操作获取真正的m3u8
                # 点击进入播放页面
                # truePageResp = requests.get(turePageUrl)
                # truePageResp.encoding = 'utf-8'
                # # 定义re的解析数据
                # reRule = re.compile(
                #     r'.*?"link_next": "\/play\/18529-1-2.html", "link_pre": "", "url":(?P<videoM3u8>.*?),"url_next":', re.S)
                # res = reRule.finditer(truePageResp.text)
                # for it in res:
                #     # print(it.group('name'))
                #     # print(it.group('year').strip())
                #     # print(it.group('average').strip())
                #     # print(it.group('personNum').strip())
                #     dic = it.groupdict()
                #     dic['videoM3u8'] = dic['videoM3u8'].strip()
                #     trueUrl = repr(dic['videoM3u8'])
                #     print(trueUrl )
            await asyncio.wait(tasks)
    return {
        "code": '000000',
        "msg": '获取麻花-' + video_name + '-影视资源成功',
        "url": 'ggg',
    }
