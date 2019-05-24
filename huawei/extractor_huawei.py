# -*- coding: utf-8 -*-
from util.util import Util
from bs4 import BeautifulSoup
import re
import json
import traceback


class HWExtractor(object):

    def __init__(self):
        self.util = Util()
        self.writed_content = list()

    def run(self):
        pass

    def judge_page_num(self, html):
        """
        判断共有多少页
        """
        try:
            soup = BeautifulSoup(html, 'lxml')
            page_item = soup.select('div.dotline-btn > p,content span span')
            if page_item:
                page = re.findall(u'结果共(.*?)条', page_item[0].text)
                if page:
                    page = int(page[0]) / 24 + 1
                    return page
        except:
            print("judge_page_num error")
            traceback.print_exc()

    def get_each_app_url(self, html):
        """
        解析每个app的链接
        """
        try:
            app_url_list = list()
            soup = BeautifulSoup(html, 'lxml')
            app_items = soup.select('div.list-game-app div.game-info-ico a')
            if app_items:
                for item in app_items:
                    app_url_list.append('http://app.hicloud.com' + item.get('href'))
            return app_url_list
        except:
            print('get_each_app_url error')
            traceback.print_exc()

    def extractor_info(self, url, result):
        """
        解析需要获取的内容:公司名/游戏名/分类/包名(id)
        游戏名,包名,类型,公司名,orgame,apkCode,appId,media
        """
        com_name = '-'  # 公司名
        apk_type = '-'  # 软件类别
        app_name = '-'  # 软件名
        apk_name = '-'  # 包名
        app_down_count = '-'
        apkCode = '-'
        appId = '-'
        media = url['media']
        try:
            soup = BeautifulSoup(result['result'], 'lxml')

            # com_name
            intro_items = soup.select('ul.app-info-ul li.ul-li-detail')
            if intro_items:
                for item in intro_items:
                    if u"开发者" in item.text:
                        com_name_item = item.select('span')
                        if com_name_item:
                            com_name = com_name_item[0].get('title')

            # app_name
            app_name_item = soup.select('ul.app-info-ul span.title')
            if app_name_item:
                app_name = app_name_item[0].text

            # apk_name
            apk_name_item = soup.select('a.mkapp-btn')
            if apk_name_item:
                apk_name_item_t = apk_name_item[0].get('onclick')
                if apk_name_item_t:
                    apk_name = '.'.join(apk_name_item_t.split(',')[-2].split('/')[-1].split('?')[0].split('.')[0:-2])

            content = ','.join([app_name, apk_name, com_name, apk_type, app_down_count, apkCode, appId, media, url['keyword']])
            self.util.write_data(content)
        except:
            print('extractor_info error')
            traceback.print_exc()


if __name__ == '__main__':
    extractor = HWExtractor()
    body = """<!DOCTYPE html>
<html>
<head>
<script type="text/javascript">
   var servererror = new Array();
    servererror['servererror'] = "系统忙，请稍后再试！";
</script>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="奥特曼传奇英雄,奥特曼传奇英雄下载,奥特曼传奇英雄安卓版,奥特曼传奇英雄手机版,奥特曼传奇英雄免费下载,应用市场" />
<meta name="description" content=" " />
<title>奥特曼传奇英雄免费下载_华为应用市场|奥特曼传奇英雄安卓版&#40;1.3.7&#41;下载</title>
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />
<link rel="shortcut icon" href="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/10/7b9b828f89b9f312944153225e527ddb_fvaicon.ico" />
<link rel="stylesheet" href="/publish/static/plugin/appstore/template/css/prettyPhoto.css?v4.13"
type="text/css" />
<link rel="stylesheet" href="/publish/static/plugin/appstore/template/css/skin.css?v4.13"
type="text/css"></link>

<link rel="stylesheet" type="text/css"
href="/publish/static/theme/appstore/css/compress5css.css?v4.13" />

<script src="/publish/static/plugin/appstore/template/js/hisuite_api.js?v4.13" type="text/javascript"></script>
<script src="/publish/static/theme/appstore/js/jquery.min.js?v4.13" type="text/javascript"></script>
<script src="/publish/static/theme/appstore/js/jquery.jsonp.js?v4.13" type="text/javascript" type="text/javascript"></script>
<script src="/publish/static/plugin/appstore/template/js/jquery.ae.image.resize.js?v4.13" type="text/javascript"></script>
<script src="/publish/static/plugin/appstore/template/js//jquery.prettyPhoto.js?v4.13" type="text/javascript"></script>
<script type="text/javascript">

    var jsResource = new Array();
    jsResource['cloud.downAppError']="您的请求正在处理中，请不要重复提交。";
    jsResource['cloud.collection.confirmCancel']='确定取消收藏？';
    jsResource['cloud.collection.cancelDone']='取消收藏成功!';
    jsResource['cloud.collection.addDone']='添加收藏成功!';
    jsResource['cloud.collection.cancelRepeatOperation']='该收藏已被取消，不需要重复操作！';
    jsResource['cloud.collection.repeatAddOperation']='该应用已收藏成功，不需要重复操作！';
    jsResource['cloud.badOperation']="操作异常，请刷新页面再试。";
    jsResource['cloud.detail.close']="关闭"
    jsResource['cloud.detail.contentnotnull']="分享内容不能为空！"
    jsResource['cloud.detail.contenttolong']="搜索内容过长，请控制在50字以内"
    jsResource['cloud.detail.contenterrorofchar']="请不要输入非法字符"
    jsResource['cloud.page.count'] = "共"
    jsResource['cloud.page.numbers'] = "条记录"
    jsResource['cloud.page.last_page'] = "上一页"
    jsResource['cloud.page.next_page'] = "下一页"
    jsResource['cloud.page.pages'] = "页"
    jsResource['cloud.page.first'] = "首页";
    jsResource['cloud.page.last'] = "尾页";
    jsResource['cloud.msg.ok']="确定";
    jsResource['cloud.msg.cancel']="取消";
    jsResource['cloud.msg.message']="提示";
    jsResource['cloud.detail.close']="关闭";

            $(function() {
          $( ".showimg" ).aeImageResize({ width: 194,isH:false });
        });
         
    </script>

<script src="/publish/static/plugin/appstore/template/js/appsearch_appdetail.js?v4.13" type="text/javascript"></script>

<script src="/publish/static/plugin/appstore/template/js/api.js?v4.13" type="text/javascript"></script>
<style>
.showimg {
-ms-interpolation-mode: bicubic;
display: none;
}

.canvas {
display: none;
}

.imgliv {
float: left;
display: inline;
margin-left: 12px;
}

.imgul {
position: relative;
float: left;
}

.zl2 {
position: absolute;
top: 6px;
left: -112px;
}
</style>
</head>
<body id="bodyonline">
<input type="hidden" id="url_img" value="//app.hicloud.com/publish/static/plugin/appstore/template" />
<input type="hidden" id="basePath"
value="/" />
<input type="hidden" id="appId" value="C100165147" />
<input type="hidden" id="typeId" value="20" />
<input type="hidden" id="typeName" value="角色扮演" />
<input type="hidden" id="isNoneApp" value="0" />
<input type="hidden" id="appName" value="奥特曼传奇英雄" />
<input type="hidden" id="t" value="" />
<input type="hidden" id="ver" value="" />
<div class="lay-body">
<script src="/publish/static/theme/appstore/js/jquery.jsonp.js?v4.13" type="text/javascript"></script><script type="text/javascript">
    var str ="";
    str +='<noscript><div class="script_error_divMask"></div>';
    str +='<div class="script_error"><div class="log_win"><div class="script_error_info">';
    str +='<div class="script_error_info_span">访问本网站需要开启JavaScript支持，请开启或更换浏览器后重新访问。 </div>';
    str +='</div><div class="loginlogo"><img src="?v4.13" />';
    str +='</div></div></div></noscript>';
</script>
<script type="text/javascript">
 var searchResourse = new Array();
     searchResourse['cloud.search.error'] = "请输入您要搜索的内容！";
     searchResourse['cloud.search.prompt'] = "搜索";
     searchResourse['cloud.search.contenttoerrorchar'] = "输入内容有误，请重新输入";
     searchResourse['cloud.search.contenttolong'] = "搜索内容过长，请控制在50字以内";
     searchResourse['cloud.browse.continue'] = "继续";
     searchResourse['basePath'] = "//app.hicloud.com/";
     searchResourse['usedl'] = "1";
     var myReg = /[|&;$%@<>()+,'"]/;
</script>
<div class="huawei-cookie" id="huawei-cookie" style="display: none;background: #f0f2f5;padding: 3px 20px;position: relative;">
    <div class="huawei-cookie-cnt" style="max-width: 1100px;width:90%;margin:10px auto;position: relative;">
        <div class="huawei-cookie-txt" style="font-size: 12px;color:#000;text-align: center;">
            <i class="icon icon-broser-warn" style="box-sizing: border-box; -moz-box-sizing: border-box; -ms-border-sizing: border-box; display: inline-block; border: none; background-image: url(http://emuirom.hicloud.com/dl/emuirom123/attachment/2019/02/18/icons.png); background-position: -182px 0; width: 40px; height: 33px; margin-right: 10px; vertical-align: middle;"></i>
            <span style="color: #6c7175; font-size: 14px;">温馨提醒：本网站使用cookies。继续浏览本网站即表示您同意我们使用cookies。更多信息，请阅读</span>
            <a href="https://consumer.huawei.com/cn/legal/cookie-policy/" style="color: #0ea5f3;font-size:14px;font-family: inherit;">隐私政策</a>
            <span class="agree-btn" id="agree-btn" style="min-width: 100px;min-height: 28px;background:#e63c3c;color:#fff;border-radius:21px;font-size:14px;line-height: 28px;border:none;outline:none;margin-left:40px;cursor:pointer;box-shadow:0 1px 5px 0 rgba(230,60,60,.3);text-align:center;display: inline-block;">同意</span>
        </div>
    </div>
    <svg class="huawei-cookie-close" id="huawei-cookie-close" xmlns="http://www.w3.org/2000/svg" style="display:inline-block;position:absolute;top:50%;right: 20px;height:32px;width:32px;transform:translateY(-50%);cursor:pointer;">
        <g fill="#3C3C3C" fill-rule="evenodd" style="fill: #BFC4CC;">
            <path d="M8 7l17 17-1 1L7 8z"></path>
            <path d="M7 24L24 7l1 1L8 25z"></path>
        </g>
    </svg>
</div>
<script type="text/javascript">
    var search = "agreed-huawei-cookiepolicy=1";
    if(document.cookie.indexOf(search) < 0){
        document.getElementById("huawei-cookie").style.display="block";
    }
    document.getElementById("huawei-cookie-close").addEventListener("click",function(){
         document.getElementById("huawei-cookie").style.display="none";
    });
    document.getElementById("agree-btn").addEventListener("click",function(){
         document.getElementById("huawei-cookie").style.display="none";
         var date=new Date();
         var expiresDays=365;
         date.setTime(date.getTime()+expiresDays*24*3600*1000);
         document.cookie="agreed-huawei-cookiepolicy=1; expires="+date.toGMTString()+";path=/";
         if(document.cookie.indexOf("cs6k_langid=en_us") < 0){
             document.cookie="cs6k_langid=zh_cn; expires="+date.toGMTString()+";path=/"+";domain=."+document.domain;
         }else{
             document.cookie="cs6k_langid=en_us; expires="+date.toGMTString()+";path=/"+";domain=."+document.domain;
         }
    });
</script>
<div class="topbar" style="z-index: 105;position:relative;">
    <div class="topbar-wrap" style="z-index: 103;position:relative;">
        <div class="topnav">
            <div class="topnav-item">
                <a target="_blank" rel="noopener noreferrer" href="http://consumer.huawei.com/cn/">华为官网</a>
            </div>
            <div class="topnav-item">
                <a target="_blank" rel="noopener noreferrer" class="nav1" href="http://honor.cn/">华为荣耀</a>
            </div>
            <div class="topnav-item">
                <a target="_blank" rel="noopener noreferrer" href="http://www.vmall.com/">华为商城</a>
            </div>
            <div id="center" class="center">
                <a class="topnav-item cur"  href="" onclick="return false;">
                    <span data-bind="commonlang.soft-center">软件应用</span>
                </a>
                <div class="soft-info-arrow" id="soft-info"></div>
                <ul class="soft-center" id="soft-center">
                    <li>
                        <a target="_blank" rel="noopener noreferrer" href="http://emui.huawei.com/cn">EMUI</a>
                    </li>
                    <li>
                        <a target="_blank" rel="noopener noreferrer" href="http://cloud.huawei.com">华为终端云空间</a>
                    </li>
                    <li>
                        <a href="//app.hicloud.com">应用市场</a>
                    </li>
                    <li>
                        <a target="_blank" rel="noopener noreferrer" href="http://skytone.vmall.com/">天际通</a>
                    </li>
                    <li>
                        <a target="_blank" rel="noopener noreferrer" href="http://developer.huawei.com/">开发者联盟</a>
                    </li>
                </ul>
            </div>
            <div class="topnav-item">
                <a target="_blank" rel="noopener noreferrer" href="http://club.huawei.com/cn">花粉俱乐部</a>
            </div>
        </div>
        <div class="topbar-login">
            <div class="language-info" id="languagetipId">
                <div class="language-info-label">选择区域 / 语言</div>
                <div class="language-info-arrow" id="language-info-arrow"></div>
                <ul id="lang_list" class="language-list">
                     <a href="/lang/zh_cn" class="zh">中文</a>
                     <a href="/lang/en_us">English</a>
                </ul>
            </div>
        </div>
    </div>
</div>


<input type="hidden" value="/" id="basePath" />
<input type="hidden" value="" id="login_url" />
<input type="hidden" value="zh_cn" id="lang" />
<input type="hidden" value="https:&#x2F;&#x2F;wwwtest1.hicloud.com:38443" id="cloud_url" />
<input type="hidden" value="detail" id="currentAct" />
<input type="hidden" value="2" id="parentId" />
<input type="hidden" value="42" id="mcc"/>
<input type="hidden" value="" id="mobileModel"/>
<input type="hidden" value="" id="uid" />
<input type="hidden" value="" id="uacc" />
<input type="hidden" value="24" id="siteid" />
<input type="hidden" value="" id="s_deviceId"/>

<input type="hidden" value="http:&#x2F;&#x2F;hwid1test.vmall.com:8083" id="vmallloginurl"/>
<input type="hidden" value="" id="loginignore"/>
<div class="lay-head">
    <div class="logo-wrap" style="z-index: 101;position:relative;">
        <div class="theme-logo">
            <a target="_blank" rel="noopener noreferrer" href="http://consumer.huawei.com/cn/">
                <img class="theme-pic" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/17772b886af157cf777d8f9c7ea641b2_logo.png"/>
            </a>
        </div>
        <div class="sprt-logo">
            <img class="sprt-pic" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/9456873af2ba274e0337605a67101cfd_separate.png"/>
        </div>
        <div class="porallogo">
            <a href="/">
                <img class="porallogo-pic" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/33eec5d387e7fa0c8f5268e249742ff8_porallogo.png"/>
            </a>
        </div>
        <div class="search-bar">
            <form id="searchForm" method="post" onsubmit="return false;">
                <input style="cursor:text;color:#666666;text-indent: 1px;"
                       class="search-txt" type="text" id="searchText" name="searchText" value=""
                        onfocus="zhytools.onFocus()" onblur="zhytools.onBlur()" 
                       onkeypress="zhytools.do_search_key(event);"/>
                <div class="searchSubSpan">
                    <input type="button" class="search-btn" id="btnSearch" onclick="zhytools.toSearchResult(this);"/>
                </div>
            </form>
        </div>
            <label for="searchText" id="labelPlaceholder" >搜索</label>
        <div class="hot-word">

                                    <a title="购物" href="javascript:void(0);"
               onclick="zhytools.searchHotKeys('/','购物');">购物</a>
                                                <a title="贷款" href="javascript:void(0);"
               onclick="zhytools.searchHotKeys('/','贷款');">贷款</a>
                                                <a title="租房" href="javascript:void(0);"
               onclick="zhytools.searchHotKeys('/','租房');">租房</a>
                                                                         </div>
    </div>
</div>

<script type="text/javascript">
    var temp = '';
    temp += '<div id="browserMaskDIV" class="divMask2" style="display:none;"></div>';
    temp += '<div id="cannotuse" class="allwkg">';
    temp += '<div class="log_win">';
    temp += '<div class="HiCloud_error_info">';
    temp += '<div class="HiCloud_error_info_span">您的浏览器不兼容</div>';
    temp += '<div class="HiCloud_error_info_span2">通过您访问我们网站的信息，我们推荐您使用下列浏览器的最新版本：</div>';
    temp += '<div>';
    temp += '<a href="http://www.google.com/chrome/index.html" target="_blank">Chrome</a>,';
    temp += '<a href="http://www.mozilla.com/en-US/firefox/new/" target="_blank">Firefox</a>,';
    temp += '<a href="http://windows.microsoft.com/zh-CN/internet-explorer/downloads/ie-8" target="_blank">Internet Explorer8</a>';
    temp += '</div>';
    temp += '<ul class="btn_ul btn_ul2"><li>';
    temp += '<a onclick="continueAccessBrowse();" href="javascript:void(0);"><span class="btn_leftli"></span><span class="btn_centerli">' + searchResourse['cloud.browse.continue'] + '</span></a></li></ul>';
    temp += '</div>';
    temp += '<div class="loginlogo">';
    temp += '<img src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/f4b1d72ed5a2c8c2a66d048a919d4674_hicloud_error.gif" />';
    temp += '</div></div></div>';
    $(function () {
        var userHeadPic = $("#userHeadPic").val();
        $("#user_pic").css("background-image", "url(" + userHeadPic + ")");
        $("#center").mouseover(function () {
            $("#soft-center").show();
            $("#soft-info").removeClass("soft-info-arrow");
            $("#soft-info").addClass("soft-info-arrows");
        });
        $("#center").mouseleave(function () {
            $("#soft-center").hide();
            $("#soft-info").removeClass("soft-info-arrows");
            $("#soft-info").addClass("soft-info-arrow");
        });
        $("#userinfoId").mouseover(function () {
            $("#usertip").show();
            $("#user-info-arrow").removeClass("user-info-arrow");
            $("#user-info-arrow").addClass("user-info-arrows");
        });
        $("#userinfoId").mouseleave(function () {
            $("#usertip").hide();
            $("#user-info-arrow").removeClass("user-info-arrows");
            $("#user-info-arrow").addClass("user-info-arrow");
        });
        $("#languagetipId").mouseover(function () {
            $("#lang_list").show();
            $("#language-info-arrow").removeClass("language-info-arrow");
            $("#language-info-arrow").addClass("language-info-arrows");
        });
        $("#languagetipId").mouseleave(function () {
            $("#lang_list").hide();
            $("#language-info-arrow").removeClass("language-info-arrows");
            $("#language-info-arrow").addClass("language-info-arrow");
        });
    });
</script>

<iframe id="iframeLogout" width="0" height="0" style="display:none;"></iframe>
<input type="hidden" value='/' id="basePath"/>
<div class="lay-navi" style="z-index: 102;position:relative;">
    <div class="header-wrap eh-menu" style="z-index: 102;position:relative;">
        <ul class="ul-nav emo_nv cl">
                    <li value="1" class="navnormal" onMouseOut="this.className='navnormal';"  onMouseOver="this.className='navsign1';">
           <a href="/">首页</a></li>
                             <li value="2" id="a" class="navsign">
                <a href="/game/list">游戏</a>
            </li>
                                <li value="3" class="navnormal" onMouseOut="this.className='navnormal';"
                onMouseOver="this.className='navsign1';">
                <a href="/soft/list">软件</a>
            </li>
                                                <li value="4" class="navnormal" onMouseOut="this.className='navnormal';"
                onMouseOver="this.className='navsign1';">
                <a href="/topics">专题</a>
            </li>
                                  <li value="5" class="navnormal" onMouseOut="this.className='navnormal';"
                onMouseOver="this.className='navsign1';">
                <a href="/brands">品牌专区</a>
            </li>
                                </ul>
        <b class="navsign-move ehm-0"></b>
    </div>
</div>
<div class="lay-main">
<h5 class="bar10"></h5>
<div class="lay-left hdn-x">
<div class="unit nofloat prsnRe corner">
<div class="unit-main detail-part">
<h5 class="bar20"></h5>
<div class="app-info flt">
<ul class="app-info-ul nofloat">
<li class="img"><img class="app-ico"
src="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;b0fe93ada650448e848483ed55771431.png"
onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
alt="华为应用市场_奥特曼传奇英雄" /></li>
<li>
<p>
<span class="title">奥特曼传奇英雄</span> <span
class="grey sub">下载：2753万次</span>
</p>
<p>
<span class="score_9"> <em></em>
</span>
</p>
</li>
</ul>
<h5 class="bar15"></h5>
<ul class="app-info-ul nofloat">
<li class="ul-li-detail">大小： <span>296.41MB</span>
</li>
<li class="ul-li-detail">日期： <span>2019-04-14</span>
</li>
<li class="ul-li-detail">开发者： <span title='合肥乐堂动漫信息技术有限公司'>合肥乐堂动漫信...</span>
</li>
<li class="ul-li-detail">版本： <span>1.3.7</span>
</li>
                                        <li class="ul-li-detail1">
<div class="bdsharebuttonbox mtp5">
  <a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a>
  <a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a>
  <a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a>
  <a href="#" class="bds_sqq" data-cmd="sqq" title="分享到QQ好友"></a>
  <a href="#" class="bds_tieba" data-cmd="tieba" title="分享到百度贴吧"></a>
</div>
</li>
                                </ul>
</div>
<h5 class="bar10 nofloat"></h5>
<div class="app-function nofloat">
							
<a class="mkapp-btn mab-download" title="下载到电脑" href="javascript:void(0);" onclick="zhytools.downloadApp('C100165147', '奥特曼传奇英雄', 'appdetail_dl', '20', '角色扮演' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;b0&#x2F;b0fe93ada650448e848483ed55771431&#x2F;com.joym.legendhero.huawei.1904131543.apk?sign=portal@portal1557799315473&amp;source=portalsite' , '1.3.7');">
<b class="b-lt"></b>
<span> <em class="flt pc-special"></em>
下载到电脑
</span>
<b class="b-rt"></b>
</a>
							
</div>
<h5 class="bar30 dotline-btn"></h5>
<h4 class="sub">
<span class="title">奥特曼传奇英雄 截图</span>
</h4>
<div class="app-images prsnRe nofloat">

<div id="contentImages" class="app-images-item inrow-v">
<ul class="imgul"><li class="imgliv"><a rel="prettyPhoto[gallery]"
href="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut1&#x2F;b0fe93ada650448e848483ed55771431.jpg"> <img class="defaultimg"
src="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut1&#x2F;b0fe93ada650448e848483ed55771431.jpg">
<img class="showimg" src="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut1&#x2F;b0fe93ada650448e848483ed55771431.jpg">
<canvas class="canvas"></canvas>
</a></li>
<li class="imgliv"><a rel="prettyPhoto[gallery]"
href="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut2&#x2F;b0fe93ada650448e848483ed55771431.jpg"> <img class="defaultimg"
src="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut2&#x2F;b0fe93ada650448e848483ed55771431.jpg">
<img class="showimg" src="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut2&#x2F;b0fe93ada650448e848483ed55771431.jpg">
<canvas class="canvas"></canvas>
</a></li>
<li class="imgliv"><a rel="prettyPhoto[gallery]"
href="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut3&#x2F;b0fe93ada650448e848483ed55771431.jpg"> <img class="defaultimg"
src="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut3&#x2F;b0fe93ada650448e848483ed55771431.jpg">
<img class="showimg" src="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut3&#x2F;b0fe93ada650448e848483ed55771431.jpg">
<canvas class="canvas"></canvas>
</a></li>
<li class="imgliv"><a rel="prettyPhoto[gallery]"
href="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut4&#x2F;b0fe93ada650448e848483ed55771431.jpg"> <img class="defaultimg"
src="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut4&#x2F;b0fe93ada650448e848483ed55771431.jpg">
<img class="showimg" src="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;screenshut4&#x2F;b0fe93ada650448e848483ed55771431.jpg">
<canvas class="canvas"></canvas>
</a></li>
</ul>
</div>
<a hideFocus="true" href="javascript:void(0);" id="leftAct"
class="prsnAb img-ctrl lt" style="display: none;"></a> <a
hideFocus="true" href="javascript:void(0);" id="rightAct"
class="prsnAb img-ctrl rt"></a>

<script type="text/javascript">
                        $("a[rel^='prettyPhoto']").prettyPhoto({
                            animation_speed: 'fast',
                            theme: 'facebook',
                            default_width: 300,
                            default_height: 450,
                            slideshow: 3000,
                            social_tools: false,
                            allow_resize: false,
                            show_title: false,
                            gallery_markup: ''
                        });
                                                scrollimg();
                        function scrollimg() {
                                    var img_count = $(".imgliv").length;
                                    var ul_w = 194 * img_count + img_count * 12;
                                    $(".imgul").css("width", ul_w);
                                    if (img_count > 3) {
                                        $(".imgliv").eq(0).addClass("scroll_on");
                                    }
                                    $("#rightAct").bind("click", function () {
                                        var curr = $(".app-images-item .scroll_on").index();
                                        if (curr < 0)
                                            return;
                                        if ((img_count - curr) > 3) {
                                            $(".app-images-item .scroll_on").removeClass("scroll_on");
                                            $(".app-images-item li").eq(curr + 1).addClass("scroll_on");
                                            $(".app-images-item ul").animate({ left: -(194 * (curr + 1) + 12 * (curr + 1)) }, 300);
                                            if (img_count - curr - 1 == 3) {
                                                $("#rightAct").hide();
                                            }
                                        }
                                        $("#leftAct").show();
                                    });
                                    $("#leftAct").bind("click", function () {
                                        var curr = $(".app-images-item .scroll_on").index();
                                        if (curr < 0)
                                            return;
                                        if (curr > 0) {
                                            $(".app-images-item .scroll_on").removeClass("scroll_on");
                                            $(".app-images-item li").eq(curr - 1).addClass("scroll_on");
                                            $(".app-images-item ul").animate({ left: -(194 * (curr - 1) + 12 * (curr - 1)) }, 300);
                                            if (curr == 1) {
                                                $("#leftAct").hide();
                                            }
                                            $("#rightAct").show();
                                        }
                                    });
                                }
                         </script>
</div>
<h4 class="sub">
<span class="title">奥特曼传奇英雄 介绍</span>
</h4>
<div class="content">
<div id="app_strdesc">春日派对开启 银河公会战来袭  <br />
     又是一年春暖花开时，传奇奥特曼们在光之国举行了盛大的春日派对，登陆好礼拿不停，每日通关惊喜送，绝版道具限时放送，宇宙boss追捕杀竞赛，更有热爱对决的英雄们期待已久的银河公会战，大战在即，一触即发，尽在传奇英雄全新版本！<br />
<br />
捷德豪勇形态登场  加拉特隆王来袭<br />
    捷得奥特曼新解锁豪勇形态，通过收集奥特之父、赛罗奥特曼胶囊即可解锁，超能力以及光线技能的威力都被提升的最强战斗形态，助你所向披靡，同时全新的贝利亚融合兽加拉德隆王也将登场，由金古桥和加拉德隆的胶囊融合升华而成。结合了两大怪兽超强力的能量，过去型的佩丹尼姆发射器的威力也增加了好几倍，让我们再一次和捷德一起，捍卫我们的地球！<br />
<br />
奥特兄弟集结 小队协同作战<br />
   游戏中战斗不再是循规蹈矩的简单对决，取而代之的是自由的组合搭配，玩家不再限制于角色对战，全新的轮换系统，各种强大不同的奥特曼英雄任你选择更多的队伍搭配，让你拥有无限可能，组建自己的奥特战队，横扫一切对手，赢取最后的胜利！
</div>
<div id="app_desc" style="display: none;">春日派对开启 银河公会战来袭  <br />
     又是一年春暖花开时，传奇奥特曼们在光之国举行了盛大的春日派对，登陆好礼拿不停，每日通关惊喜送，绝版道具限时放送，宇宙boss追捕杀竞赛，更有热爱对决的英雄们期待已久的银河公会战，大战在即，一触即发，尽在传奇英雄全新版本！<br />
<br />
捷德豪勇形态登场  加拉特隆王来袭<br />
    捷得奥特曼新解锁豪勇形态，通过收集奥特之父、赛罗奥特曼胶囊即可解锁，超能力以及光线技能的威力都被提升的最强战斗形态，助你所向披靡，同时全新的贝利亚融合兽加拉德隆王也将登场，由金古桥和加拉德隆的胶囊融合升华而成。结合了两大怪兽超强力的能量，过去型的佩丹尼姆发射器的威力也增加了好几倍，让我们再一次和捷德一起，捍卫我们的地球！<br />
<br />
奥特兄弟集结 小队协同作战<br />
   游戏中战斗不再是循规蹈矩的简单对决，取而代之的是自由的组合搭配，玩家不再限制于角色对战，全新的轮换系统，各种强大不同的奥特曼英雄任你选择更多的队伍搭配，让你拥有无限可能，组建自己的奥特战队，横扫一切对手，赢取最后的胜利！</div>

<br />
【权限】
<ul class="hidepermission">
<li class="hide">检测出此应用获取6个敏感隐私权限：</li><li class="hide">· 修改或删除存储卡中的内容</li>

<li class="hide">· 发送短信</li>

<li class="hide">· 访问大致位置信息（使用网络进行定位）</li>

<li class="hide">· 获取设备识别码和状态</li>

<li class="hide">· 读取存储卡中的内容</li>

<li class="hide">· 显示在其他应用上面</li>

<li class="hide">敏感隐私权限用途说明：</li><li class="hide">1. 允许应用修改或删除存储卡中的内容。</li>
<li class="hide">2. 允许应用发送短信&#x2F;彩信。此权限可能导致意外收费。恶意应用可能未经您确认而发送短信&#x2F;彩信，由此产生相关费用。</li>
<li class="hide">3. 允许应用根据网络来源（例如基站和 WLAN 网络）获取您的位置信息。您的手机必须支持并开启这些位置信息服务，此应用才能使用这些服务。</li>
<li class="hide">4. 允许应用访问设备的电话功能。此权限可让应用确定本机号码和设备 ID、是否正处于通话状态以及拨打的号码。</li>
<li class="hide">5. 允许应用读取存储卡中的内容。</li>
<li class="hide">6. 显示弹框、全屏界面到其他应用上面</li>
<span class="per-more" class="ctrl">
<a class="link-blue per-margin" href="javascript:void(0);">
展开 <em class="ico txt-open">&nbsp;</em>
</a>
</span>
<span class="per-less" class="ctrl">
<a class="link-blue per-margin" href="javascript:void(0);">
收起 <em class="ico txt-close">&nbsp;</em>
</a>
</span>
</ul>
<br>
<script type="text/javascript">
hide();
function hide() {
var per_count = $(".hidepermission li").length;
for (var i = 0; i < 3; i++) {
$(".hidepermission li").eq(i).addClass("pblock");
}
if (per_count>3) {
$(".hidepermission li").eq(2).text($(".hidepermission li").eq(2).text()+' ...');
$(".per-more").css("display", "block");
}
}
$(".per-more").bind("click", function () {
    var per_count = $(".hidepermission li").length;
    $(".hidepermission .pre-point").css("display","none");
    $(".per-more").css("display","none");
    $(".per-less").css("display", "block");
    $(".hidepermission li").eq(2).text($(".hidepermission li").eq(2).text().slice(0,-3));
    for (var i =2 ; i < per_count; i++) {
    	$(".hidepermission li").eq(i).addClass("pblock");
    	
    }
    
});
$(".per-less").bind("click", function () {
    var per_count = $(".hidepermission li").length;
    $(".hidepermission .pre-point").css("display","block");
    $(".per-more").css("display","block");
    $(".per-less").css("display", "none"); 
    $(".hidepermission li").eq(2).text($(".hidepermission li").eq(2).text()+' ...');
    for (var i =3 ; i < per_count; i++) {
    	$(".hidepermission li").eq(i).removeClass("pblock");
    }
});
</script>							
<style type="text/css">
.per-more,.per-less{
display: none;
float: right;
}
.hide{
display: none;
}
.pblock{
display: block;
}
.hidepermission li{
list-style-type:none
}
</style>	
</div>
<div id="comment_list">
<a name="comment" id="comment"></a>
<script type="text/javascript">
    var commentResource = new Array();
    commentResource['cloud.detail.comment_null'] = "评论内容不能为空";
    commentResource['cloud.detail.commenttolong'] = "评论内容过长，请控制在100个字以内".replace("&#039;", "'");
    commentResource['cloud.detail.commentWrongCharacter'] = "评论内容不能包含字符：%&";
    var commentReg = /[%&]/;
</script>
<input type="hidden" value="100" id="contentLength"/>
<form
        action="//app.hicloud.com/comment/commentAction.action"
        id="commentForm" method="post" onsubmit="return false;">
    <h4 class="sub nofloat">
        <span class="title">
                        华为应用市场用户对奥特曼传奇英雄的评论
            : </span>
        <input type="hidden" value="" id="score" name="score"/>
    </h4>
    <input type="hidden" id="hid_comment"/>
    <!--[if IE]>
    <script type="text/javascript">
        var c = zhytools.readCookie("comment");
        if ("" != c) {
            $("#commentText").val(c);
            zhytools.delCookie("comment");
        }
    </script>
    <![endif]-->
    <!--[if !IE]>
    <script type="text/javascript">
        if ("#comment" == window.location.hash) {
            var c = zhytools.readCookie("comment");
            if ("" != c) {
                $("#commentText").val(c);
                zhytools.delCookie("comment");
                window.location.hash = "";
            }
        }
    </script>
    <!--<![endif]-->
</form>

<div class="center">暂无评论</div>

<div class="page-ctrl ctrl-app" id="commentListPage">
    </div></div>
</div>
</div>
</div>
<div class="lay-right">
<div class="unit nofloat corner">
<h5 class="bar20"></h5>
<div class="yellow-board">
<h5 class="bar40"></h5>
<p title="捷德新形态王者威严荣耀来袭">捷德新形态王者威严荣耀来袭</p>
</div>
<div class="unit-title nofloat">
<span class="title flt ft-yh">相关推荐</span>
</div>
<h5 class="bar10 top-line mrg-10"></h5>
<div class="unit-main nofloat">
<h5 class="bar10"></h5><div class="app-sweatch  nofloat">
<div class="open nofloat" style="display: block">
<em class="num-red">1</em>
<div class="open-ico">
<a href="/app/C100263709">
<img title="奥特曼正义降临" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;5300db9387a84e49bf4258f772c47b15.png" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png" onerror="show_app_defult(this,'//app.hicloud.com/publish/static/plugin/');" alt="奥特曼正义降临" width="48px" height="48px" />
</a>
</div>
<div class="open-info">
<p class="name">
<a href="/app/C100263709" title="奥特曼正义降临">奥特曼正义降临</a>
</p>
<h5 class="bar6"></h5>
<p class="sort">
<a class="btn-mini m-down down" onclick="zhytools.downloadApp('C100263709','奥特曼正义降临' , 'newPopular_dl','18','动作射击' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;53&#x2F;5300db9387a84e49bf4258f772c47b15&#x2F;com.huale.justicearrive.huawei.1905070934.apk?sign=portal@portal1557799315506&amp;source=portalsite' , '1.2.4','06');">
<em class="blt"></em>
<span>下载</span>
<em class="brt"></em>
</a>
</p>
</div>
</div>
<div style="display: none" class="close nofloat">
<em class="num-red">1</em>
<a class="title" title="奥特曼正义降临">奥特曼正义降临</a> <span class="num">316万次</span>
</div>
</div>
<div class="app-sweatch  nofloat">
<div class="open nofloat" style="display: none">
<em class="num-red">2</em>
<div class="open-ico">
<a href="/app/C100534065">
<img title="奥特曼热血英雄" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;e7103083ab564d189bbfca4b29b9115a.png" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png" onerror="show_app_defult(this,'//app.hicloud.com/publish/static/plugin/');" alt="奥特曼热血英雄" width="48px" height="48px" />
</a>
</div>
<div class="open-info">
<p class="name">
<a href="/app/C100534065" title="奥特曼热血英雄">奥特曼热血英雄</a>
</p>
<h5 class="bar6"></h5>
<p class="sort">
<a class="btn-mini m-down down" onclick="zhytools.downloadApp('C100534065','奥特曼热血英雄' , 'newPopular_dl','20','角色扮演' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;e7&#x2F;e7103083ab564d189bbfca4b29b9115a&#x2F;com.clgame.atmrxyx.huawei.1904191113.apk?sign=portal@portal1557799315507&amp;source=portalsite' , '1.06','06');">
<em class="blt"></em>
<span>下载</span>
<em class="brt"></em>
</a>
</p>
</div>
</div>
<div style="display: block" class="close nofloat">
<em class="num-red">2</em>
<a class="title" title="奥特曼热血英雄">奥特曼热血英雄</a> <span class="num">318万次</span>
</div>
</div>
<div class="app-sweatch  nofloat">
<div class="open nofloat" style="display: none">
<em class="num-red">3</em>
<div class="open-ico">
<a href="/app/C100080755">
<img title="奥特曼英雄归来" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;0244447e496d4f65bf76a2e26e2657c9.png" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png" onerror="show_app_defult(this,'//app.hicloud.com/publish/static/plugin/');" alt="奥特曼英雄归来" width="48px" height="48px" />
</a>
</div>
<div class="open-info">
<p class="name">
<a href="/app/C100080755" title="奥特曼英雄归来">奥特曼英雄归来</a>
</p>
<h5 class="bar6"></h5>
<p class="sort">
<a class="btn-mini m-down down" onclick="zhytools.downloadApp('C100080755','奥特曼英雄归来' , 'newPopular_dl','20','角色扮演' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;02&#x2F;0244447e496d4f65bf76a2e26e2657c9&#x2F;com.caohua.atm.huawei.1905101203.apk?sign=portal@portal1557799315507&amp;source=portalsite' , '1.31.10','06');">
<em class="blt"></em>
<span>下载</span>
<em class="brt"></em>
</a>
</p>
</div>
</div>
<div style="display: block" class="close nofloat">
<em class="num-red">3</em>
<a class="title" title="奥特曼英雄归来">奥特曼英雄归来</a> <span class="num">578万次</span>
</div>
</div>
<div class="app-sweatch  nofloat">
<div class="open nofloat" style="display: none">
<em class="num-grey">4</em>
<div class="open-ico">
<a href="/app/C100302883">
<img title="奥特曼格斗之热血英雄" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;9266d44ab59d48b18ec6c0a0ff87e02f.png" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png" onerror="show_app_defult(this,'//app.hicloud.com/publish/static/plugin/');" alt="奥特曼格斗之热血英雄" width="48px" height="48px" />
</a>
</div>
<div class="open-info">
<p class="name">
<a href="/app/C100302883" title="奥特曼格斗之热血英雄">奥特曼格斗之热...</a>
</p>
<h5 class="bar6"></h5>
<p class="sort">
<a class="btn-mini m-down down" onclick="zhytools.downloadApp('C100302883','奥特曼格斗之热血英雄' , 'newPopular_dl','18','动作射击' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;92&#x2F;9266d44ab59d48b18ec6c0a0ff87e02f&#x2F;com.sg.atmrxyx.huawei.1905071457.apk?sign=portal@portal1557799315507&amp;source=portalsite' , '2.8.0','06');">
<em class="blt"></em>
<span>下载</span>
<em class="brt"></em>
</a>
</p>
</div>
</div>
<div style="display: block" class="close nofloat">
<em class="num-grey">4</em>
<a class="title" title="奥特曼格斗之热血英雄">奥特曼格斗之热...</a> <span class="num">219万次</span>
</div>
</div>
<div class="app-sweatch  nofloat">
<div class="open nofloat" style="display: none">
<em class="num-grey">5</em>
<div class="open-ico">
<a href="/app/C100327655">
<img title="奥特曼酷跑之王" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;996054513c684e699c0c99f82326988a.png" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png" onerror="show_app_defult(this,'//app.hicloud.com/publish/static/plugin/');" alt="奥特曼酷跑之王" width="48px" height="48px" />
</a>
</div>
<div class="open-info">
<p class="name">
<a href="/app/C100327655" title="奥特曼酷跑之王">奥特曼酷跑之王</a>
</p>
<h5 class="bar6"></h5>
<p class="sort">
<a class="btn-mini m-down down" onclick="zhytools.downloadApp('C100327655','奥特曼酷跑之王' , 'newPopular_dl','18','动作射击' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;99&#x2F;996054513c684e699c0c99f82326988a&#x2F;com.sg.atmkpzw.game.huawei.1905071556.apk?sign=portal@portal1557799315508&amp;source=portalsite' , '3.9.0','06');">
<em class="blt"></em>
<span>下载</span>
<em class="brt"></em>
</a>
</p>
</div>
</div>
<div style="display: block" class="close nofloat">
<em class="num-grey">5</em>
<a class="title" title="奥特曼酷跑之王">奥特曼酷跑之王</a> <span class="num">75万次</span>
</div>
</div>
<div class="app-sweatch  nofloat">
<div class="open nofloat" style="display: none">
<em class="num-grey">6</em>
<div class="open-ico">
<a href="/app/C100300235">
<img title="奥特曼英雄传说" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;d1d022fd8cea4d6bba22e1a9102f920d.png" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png" onerror="show_app_defult(this,'//app.hicloud.com/publish/static/plugin/');" alt="奥特曼英雄传说" width="48px" height="48px" />
</a>
</div>
<div class="open-info">
<p class="name">
<a href="/app/C100300235" title="奥特曼英雄传说">奥特曼英雄传说</a>
</p>
<h5 class="bar6"></h5>
<p class="sort">
<a class="btn-mini m-down down" onclick="zhytools.downloadApp('C100300235','奥特曼英雄传说' , 'newPopular_dl','18','动作射击' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;d1&#x2F;d1d022fd8cea4d6bba22e1a9102f920d&#x2F;com.hq.Ultramanyxcs.huawei.1901171232.apk?sign=portal@portal1557799315508&amp;source=portalsite' , '1.3.0','06');">
<em class="blt"></em>
<span>下载</span>
<em class="brt"></em>
</a>
</p>
</div>
</div>
<div style="display: block" class="close nofloat">
<em class="num-grey">6</em>
<a class="title" title="奥特曼英雄传说">奥特曼英雄传说</a> <span class="num">433万次</span>
</div>
</div>
<div class="app-sweatch  nofloat">
<div class="open nofloat" style="display: none">
<em class="num-grey">7</em>
<div class="open-ico">
<a href="/app/C100551909">
<img title="奥特曼之格斗超人" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;8b02c82a434c4bd8a6e41ff33c5f1410.png" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png" onerror="show_app_defult(this,'//app.hicloud.com/publish/static/plugin/');" alt="奥特曼之格斗超人" width="48px" height="48px" />
</a>
</div>
<div class="open-info">
<p class="name">
<a href="/app/C100551909" title="奥特曼之格斗超人">奥特曼之格斗超...</a>
</p>
<h5 class="bar6"></h5>
<p class="sort">
<a class="btn-mini m-down down" onclick="zhytools.downloadApp('C100551909','奥特曼之格斗超人' , 'newPopular_dl','20','角色扮演' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;8b&#x2F;8b02c82a434c4bd8a6e41ff33c5f1410&#x2F;com.joym.combatman.huawei.1905051123.apk?sign=portal@portal1557799315508&amp;source=portalsite' , '1.0.8','06');">
<em class="blt"></em>
<span>下载</span>
<em class="brt"></em>
</a>
</p>
</div>
</div>
<div style="display: block" class="close nofloat">
<em class="num-grey">7</em>
<a class="title" title="奥特曼之格斗超人">奥特曼之格斗超...</a> <span class="num">436万次</span>
</div>
</div>
<div class="app-sweatch  nofloat">
<div class="open nofloat" style="display: none">
<em class="num-grey">8</em>
<div class="open-ico">
<a href="/app/C100041071">
<img title="奥特曼传说之战" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;ece52d5dff2e4d74a47fab8788940847.png" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png" onerror="show_app_defult(this,'//app.hicloud.com/publish/static/plugin/');" alt="奥特曼传说之战" width="48px" height="48px" />
</a>
</div>
<div class="open-info">
<p class="name">
<a href="/app/C100041071" title="奥特曼传说之战">奥特曼传说之战</a>
</p>
<h5 class="bar6"></h5>
<p class="sort">
<a class="btn-mini m-down down" onclick="zhytools.downloadApp('C100041071','奥特曼传说之战' , 'newPopular_dl','18','动作射击' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;ec&#x2F;ece52d5dff2e4d74a47fab8788940847&#x2F;com.hq.Ultramancszzdd.HUAWEI.1901141741.apk?sign=portal@portal1557799315509&amp;source=portalsite' , '1.2.5','06');">
<em class="blt"></em>
<span>下载</span>
<em class="brt"></em>
</a>
</p>
</div>
</div>
<div style="display: block" class="close nofloat">
<em class="num-grey">8</em>
<a class="title" title="奥特曼传说之战">奥特曼传说之战</a> <span class="num">825万次</span>
</div>
</div>
<div class="app-sweatch  nofloat">
<div class="open nofloat" style="display: none">
<em class="num-grey">9</em>
<div class="open-ico">
<a href="/app/C100327535">
<img title="热血奥特曼（暴击僵尸）" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;a6cc625a627941a7ace84e0df26332b4.png" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png" onerror="show_app_defult(this,'//app.hicloud.com/publish/static/plugin/');" alt="热血奥特曼（暴击僵尸）" width="48px" height="48px" />
</a>
</div>
<div class="open-info">
<p class="name">
<a href="/app/C100327535" title="热血奥特曼（暴击僵尸）">热血奥特曼（暴...</a>
</p>
<h5 class="bar6"></h5>
<p class="sort">
<a class="btn-mini m-down down" onclick="zhytools.downloadApp('C100327535','热血奥特曼（暴击僵尸）' , 'newPopular_dl','18','动作射击' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;a6&#x2F;a6cc625a627941a7ace84e0df26332b4&#x2F;com.sg.bjjs.game.huawei.1905071450.apk?sign=portal@portal1557799315509&amp;source=portalsite' , '5.9.0','06');">
<em class="blt"></em>
<span>下载</span>
<em class="brt"></em>
</a>
</p>
</div>
</div>
<div style="display: block" class="close nofloat">
<em class="num-grey">9</em>
<a class="title" title="热血奥特曼（暴击僵尸）">热血奥特曼（暴...</a> <span class="num">141万次</span>
</div>
</div>
<div class="app-sweatch  nofloat">
<div class="open nofloat" style="display: none">
<em class="num-grey">10</em>
<div class="open-ico">
<a href="/app/C10741378">
<img title="奥特曼之热血格斗" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;71764b97a1a74cd098b536786b5575ef.png" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png" onerror="show_app_defult(this,'//app.hicloud.com/publish/static/plugin/');" alt="奥特曼之热血格斗" width="48px" height="48px" />
</a>
</div>
<div class="open-info">
<p class="name">
<a href="/app/C10741378" title="奥特曼之热血格斗">奥特曼之热血格...</a>
</p>
<h5 class="bar6"></h5>
<p class="sort">
<a class="btn-mini m-down down" onclick="zhytools.downloadApp('C10741378','奥特曼之热血格斗' , 'newPopular_dl','18','动作射击' , 'http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;71&#x2F;71764b97a1a74cd098b536786b5575ef&#x2F;com.sg.atmrxgd.huawei.1905071448.apk?sign=portal@portal1557799315512&amp;source=portalsite' , '6.8.0','06');">
<em class="blt"></em>
<span>下载</span>
<em class="brt"></em>
</a>
</p>
</div>
</div>
<div style="display: block" class="close nofloat">
<em class="num-grey">10</em>
<a class="title" title="奥特曼之热血格斗">奥特曼之热血格...</a> <span class="num">511万次</span>
</div>
</div>
<div class="unit-title nofloat">
<span class="title flt ft-yh">角色扮演排行</span>
</div>
<h5 class="bar10 top-line mrg-10"></h5>
<div class="unit-main nofloat">
<h5 class="bar10"></h5><h5 class="bar10"></h5>
</div>
</div>
<h5 class="bar10"></h5>
</div>
</div>
<h5 class="bar10"></h5>
              			</div>
<div class="lay-foot">
    <div class="foot1-foot-left foot-line">
        <div class="foot1-info  nofloat">
          <span class ="footer1_wet">
             <a href="/useragreement" rel="noopener noreferrer" target="_blank">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用户协议</a>
             &nbsp;
             <a href="http://consumer.huawei.com/cn/privacy-policy/index.htm" rel="noopener noreferrer" target="_blank">隐私政策</a>
             &nbsp;
             <a href="https://consumer.huawei.com/cn/legal/cookie-policy/" rel="noopener noreferrer" target="_blank">关于cookies</a>&nbsp;
             版权所有
             <img style="vertical-align:middle;" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2017/01/18/4845b947435a89b86f7f43a550b12dbc_%E7%AC%A6%E5%8F%B7.png?mode=download"/>
             2010-2019
             华为软件技术有限公司保留一切权利
          </span>
        </div>
        <p class="foot1-info  nofloat" style="text-align:center;margin-left:75px;">
            <a href="/suwangwen.htm" class="foot-cor" target="_blank">苏网文&nbsp;[2015]&nbsp;1599-026号</a>
            <em class="ico hd">|</em>
            <a href="http://www.miitbeian.gov.cn/" class="foot-cor" target="_blank" rel="noopener noreferrer">粤ICP备09176709号-16</a>
            <em class="ico hd">|</em>
            <span>苏B2-20130048号</span>
            <em class="ico hd">|</em>
            <a href="https://www.beian.gov.cn/portal/registerSystemInfo?recordcode=32011402010009" class="foot-cor" target="_blank" rel="noopener noreferrer">苏公网安备32011402010009号</a>
            <em class="ico hd">|</em>
            <a href="/busi/Business.htm" class="foot-cor" target="_blank" rel="external nofollow">电子营业执照</a>
        </p>       
        <p class="foot1-info  nofloat" style="text-align:center;margin-left:75px;">
            <a target="_blank" rel="noopener noreferrer"href="http://white.anva.org.cn">
            <img style="height: 20px;width: 20px;vertical-align: bottom;" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2019/02/18/459FCB42930D12308EDCF5572D034AB3.png"/>
            中国反网络病毒联盟应用商店自律组</a>
            <em class="ico hd">|</em>
            <a href="/jiazhang/jzjh.htm" rel="external nofollow" target="_blank">未成年人家长监护体系</a> 
            <em class="ico hd">|</em>            
            违法和不良信息举报电话：4008308300 <em class="ico hd">|</em>
            <a href="http://developer.huawei.com/consumer/cn/devservice/support" rel="noopener noreferrer" target="_blank">商务合作</a> <em class="ico hd">|</em>
            <a href="/contactus" rel="external nofollow" target="_blank">联系我们</a>
            <a class="mlt10" href="http://e.weibo.com/hispacehw" rel="noopener noreferrer" target="_blank">
             <img style="vertical-align:middle;" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/9e0ac143f38d5fd889ed39edf373f4a8_webo-sina.png"
                  onMouseOver="this.src='http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/9e0ac143f38d5fd889ed39edf373f4a8_webo-sina.png'" width="20" height="17"/>
            </a> 
        </p>       
    </div>
</div>

<script type="text/javascript">
    var _paq = _paq || [];
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', '']);
    _gaq.push(['_addOrganic', 'soso', 'w']);
    _gaq.push(['_addOrganic', 'yodao', 'q']);
    _gaq.push(['_addOrganic', 'sogou', 'query']);
    _gaq.push(['_trackPageview']);
</script>
<div id="dynamicElement"></div>
</div>
<script type="text/javascript" id="bdshare_js"
data="type=tools&amp;uid=756728"></script>
<script type="text/javascript" id="bdshell_js"></script>
<script>window._bd_share_config = {
    "common": {
        "bdSnsKey": {},
        "bdText": "",
        "bdComment": "华为应用市场官网，汇聚各种精品安卓(Android)手机软件游戏下载资源，是目前网上最贴心的安卓手机游戏下载站。华为商城购华为手机，为您提供贴心的华为应用市场服务。",
        "bdMini": "2",
        "bdMiniList": false,
        "bdPic": "http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;b0fe93ada650448e848483ed55771431.png",
        "bdStyle": "1",
        "bdSize": "24",
        "bdUrl":"//app.hicloud.com/app/C100165147"
    },
    "share": {}
};
with(document) 0[(getElementsByTagName('head')[0] || body).appendChild(createElement('script')).src = 'http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion=' + ~ ( - new Date() / 36e5)]; 
</script>
</body>
</html>"""
    # extractor.get_each_app_url(body)
    extractor.extractor_info({'media': 'huawei', 'keyword': '1'}, {"result": body})
    html = """
    

<!DOCTYPE html>
<html>
<head>
    <script type="text/javascript">
        var servererror = new Array();
        servererror['servererror'] = "系统忙，请稍后再试！";
    </script>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="keywords" content="应用市场,华为手机,安卓软件,游戏下载"/>
    <meta name="description" content="应用市场是华为推出的一款基于Android智能手机的免费资源共享平台，用户可以在华为官网上搜索、下载各种安卓软件，安卓游戏，安卓应用，游戏攻略。"/>
    <title>"英雄爱三国"的搜索结果 - 安卓软件搜索|游戏搜索|华为应用市场</title>
    <link href='http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/10/7b9b828f89b9f312944153225e527ddb_fvaicon.ico' rel="shortcut icon">
    <link rel="stylesheet" type="text/css" href="/publish/static/theme/appstore/css/compress5css.css?v4.13"/>

    <script src="/publish/static/theme/appstore/js/jquery.min.js?v4.13" type="text/javascript"></script>
    <script src="/publish/static/theme/appstore/js/jquery.jsonp.js?v4.13" type="text/javascript"></script>
    <script type="text/javascript">
        var jsResource = new Array();
        jsResource['cloud.page.count'] = "共";
        jsResource['cloud.page.numbers'] = "条记录";
        jsResource['cloud.page.last_page'] = "上一页";
        jsResource['cloud.page.next_page'] = "下一页";
        jsResource['cloud.page.pages'] = "页";
        jsResource['cloud.page.first'] = "首页";
        jsResource['cloud.page.last'] = "尾页";
        jsResource['cloud.downAppError']="您的请求正在处理中，请不要重复提交。"
        jsResource['cloud.msg.ok']="确定"
        jsResource['cloud.msg.message']="提示"
        jsResource['cloud.detail.close']="关闭"
    </script>
    <script src="/publish/static/plugin/appstore/template/js/app_search.js?v4.13" type="text/javascript"></script>
    </head>
<body>
    <div class="lay-body">
    <script src="/publish/static/theme/appstore/js/jquery.jsonp.js?v4.13" type="text/javascript"></script>
    <script type="text/javascript">
    var str ="";
    str +='<noscript><div class="script_error_divMask"></div>';
    str +='<div class="script_error"><div class="log_win"><div class="script_error_info">';
    str +='<div class="script_error_info_span">访问本网站需要开启JavaScript支持，请开启或更换浏览器后重新访问。 </div>';
    str +='</div><div class="loginlogo"><img src="?v4.13" />';
    str +='</div></div></div></noscript>';
</script>
<script type="text/javascript">
 var searchResourse = new Array();
     searchResourse['cloud.search.error'] = "请输入您要搜索的内容！";
     searchResourse['cloud.search.prompt'] = "搜索";
     searchResourse['cloud.search.contenttoerrorchar'] = "输入内容有误，请重新输入";
     searchResourse['cloud.search.contenttolong'] = "搜索内容过长，请控制在50字以内";
     searchResourse['cloud.browse.continue'] = "继续";
     searchResourse['basePath'] = "//app.hicloud.com/";
     searchResourse['usedl'] = "1";
     var myReg = /[|&;$%@<>()+,'"]/;
</script>
<div class="huawei-cookie" id="huawei-cookie" style="display: none;background: #f0f2f5;padding: 3px 20px;position: relative;">
    <div class="huawei-cookie-cnt" style="max-width: 1100px;width:90%;margin:10px auto;position: relative;">
        <div class="huawei-cookie-txt" style="font-size: 12px;color:#000;text-align: center;">
            <i class="icon icon-broser-warn" style="box-sizing: border-box; -moz-box-sizing: border-box; -ms-border-sizing: border-box; display: inline-block; border: none; background-image: url(http://emuirom.hicloud.com/dl/emuirom123/attachment/2019/02/18/icons.png); background-position: -182px 0; width: 40px; height: 33px; margin-right: 10px; vertical-align: middle;"></i>
            <span style="color: #6c7175; font-size: 14px;">温馨提醒：本网站使用cookies。继续浏览本网站即表示您同意我们使用cookies。更多信息，请阅读</span>
            <a href="https://consumer.huawei.com/cn/legal/cookie-policy/" style="color: #0ea5f3;font-size:14px;font-family: inherit;">隐私政策</a>
            <span class="agree-btn" id="agree-btn" style="min-width: 100px;min-height: 28px;background:#e63c3c;color:#fff;border-radius:21px;font-size:14px;line-height: 28px;border:none;outline:none;margin-left:40px;cursor:pointer;box-shadow:0 1px 5px 0 rgba(230,60,60,.3);text-align:center;display: inline-block;">同意</span>
        </div>
    </div>
    <svg class="huawei-cookie-close" id="huawei-cookie-close" xmlns="http://www.w3.org/2000/svg" style="display:inline-block;position:absolute;top:50%;right: 20px;height:32px;width:32px;transform:translateY(-50%);cursor:pointer;">
        <g fill="#3C3C3C" fill-rule="evenodd" style="fill: #BFC4CC;">
            <path d="M8 7l17 17-1 1L7 8z"></path>
            <path d="M7 24L24 7l1 1L8 25z"></path>
        </g>
    </svg>
</div>
<script type="text/javascript">
    var search = "agreed-huawei-cookiepolicy=1";
    if(document.cookie.indexOf(search) < 0){
        document.getElementById("huawei-cookie").style.display="block";
    }
    document.getElementById("huawei-cookie-close").addEventListener("click",function(){
         document.getElementById("huawei-cookie").style.display="none";
    });
    document.getElementById("agree-btn").addEventListener("click",function(){
         document.getElementById("huawei-cookie").style.display="none";
         var date=new Date();
         var expiresDays=365;
         date.setTime(date.getTime()+expiresDays*24*3600*1000);
         document.cookie="agreed-huawei-cookiepolicy=1; expires="+date.toGMTString()+";path=/";
         if(document.cookie.indexOf("cs6k_langid=en_us") < 0){
             document.cookie="cs6k_langid=zh_cn; expires="+date.toGMTString()+";path=/"+";domain=."+document.domain;
         }else{
             document.cookie="cs6k_langid=en_us; expires="+date.toGMTString()+";path=/"+";domain=."+document.domain;
         }
    });
</script>
<div class="topbar" style="z-index: 105;position:relative;">
    <div class="topbar-wrap" style="z-index: 103;position:relative;">
        <div class="topnav">
            <div class="topnav-item">
                <a target="_blank" rel="noopener noreferrer" href="http://consumer.huawei.com/cn/">华为官网</a>
            </div>
            <div class="topnav-item">
                <a target="_blank" rel="noopener noreferrer" class="nav1" href="http://honor.cn/">华为荣耀</a>
            </div>
            <div class="topnav-item">
                <a target="_blank" rel="noopener noreferrer" href="http://www.vmall.com/">华为商城</a>
            </div>
            <div id="center" class="center">
                <a class="topnav-item cur"  href="" onclick="return false;">
                    <span data-bind="commonlang.soft-center">软件应用</span>
                </a>
                <div class="soft-info-arrow" id="soft-info"></div>
                <ul class="soft-center" id="soft-center">
                    <li>
                        <a target="_blank" rel="noopener noreferrer" href="http://emui.huawei.com/cn">EMUI</a>
                    </li>
                    <li>
                        <a target="_blank" rel="noopener noreferrer" href="http://cloud.huawei.com">华为终端云空间</a>
                    </li>
                    <li>
                        <a href="//app.hicloud.com">应用市场</a>
                    </li>
                    <li>
                        <a target="_blank" rel="noopener noreferrer" href="http://skytone.vmall.com/">天际通</a>
                    </li>
                    <li>
                        <a target="_blank" rel="noopener noreferrer" href="http://developer.huawei.com/">开发者联盟</a>
                    </li>
                </ul>
            </div>
            <div class="topnav-item">
                <a target="_blank" rel="noopener noreferrer" href="http://club.huawei.com/cn">花粉俱乐部</a>
            </div>
        </div>
        <div class="topbar-login">
            <div class="language-info" id="languagetipId">
                <div class="language-info-label">选择区域 / 语言</div>
                <div class="language-info-arrow" id="language-info-arrow"></div>
                <ul id="lang_list" class="language-list">
                     <a href="/lang/zh_cn" class="zh">中文</a>
                     <a href="/lang/en_us">English</a>
                </ul>
            </div>
        </div>
    </div>
</div>
    

<input type="hidden" value="/" id="basePath" />
<input type="hidden" value="" id="login_url" />
<input type="hidden" value="zh_cn" id="lang" />
<input type="hidden" value="https:&#x2F;&#x2F;wwwtest1.hicloud.com:38443" id="cloud_url" />
<input type="hidden" value="index" id="currentAct" />
<input type="hidden" value="PARENT_ID" id="parentId" />
<input type="hidden" value="42" id="mcc"/>
<input type="hidden" value="" id="mobileModel"/>
<input type="hidden" value="" id="uid" />
<input type="hidden" value="" id="uacc" />
<input type="hidden" value="24" id="siteid" />
<input type="hidden" value="" id="s_deviceId"/>

<input type="hidden" value="http:&#x2F;&#x2F;hwid1test.vmall.com:8083" id="vmallloginurl"/>
<input type="hidden" value="" id="loginignore"/>
<div class="lay-head">
    <div class="logo-wrap" style="z-index: 101;position:relative;">
        <div class="theme-logo">
            <a target="_blank" rel="noopener noreferrer" href="http://consumer.huawei.com/cn/">
                <img class="theme-pic" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/17772b886af157cf777d8f9c7ea641b2_logo.png"/>
            </a>
        </div>
        <div class="sprt-logo">
            <img class="sprt-pic" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/9456873af2ba274e0337605a67101cfd_separate.png"/>
        </div>
        <div class="porallogo">
            <a href="/">
                <img class="porallogo-pic" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/33eec5d387e7fa0c8f5268e249742ff8_porallogo.png"/>
            </a>
        </div>
        <div class="search-bar">
            <form id="searchForm" method="post" onsubmit="return false;">
                <input style="cursor:text;color:#666666;text-indent: 1px;"
                       class="search-txt" type="text" id="searchText" name="searchText" value="英雄爱三国"
                        onfocus="zhytools.onFocus()" onblur="zhytools.onBlur()" 
                       onkeypress="zhytools.do_search_key(event);"/>
                <div class="searchSubSpan">
                    <input type="button" class="search-btn" id="btnSearch" onclick="zhytools.toSearchResult(this);"/>
                </div>
            </form>
        </div>
            <label for="searchText" id="labelPlaceholder" >搜索</label>
        <div class="hot-word">

                                    <a title="购物" href="javascript:void(0);"
               onclick="zhytools.searchHotKeys('/','购物');">购物</a>
                                                <a title="贷款" href="javascript:void(0);"
               onclick="zhytools.searchHotKeys('/','贷款');">贷款</a>
                                                <a title="租房" href="javascript:void(0);"
               onclick="zhytools.searchHotKeys('/','租房');">租房</a>
                                                                         </div>
    </div>
</div>

<script type="text/javascript">
    var temp = '';
    temp += '<div id="browserMaskDIV" class="divMask2" style="display:none;"></div>';
    temp += '<div id="cannotuse" class="allwkg">';
    temp += '<div class="log_win">';
    temp += '<div class="HiCloud_error_info">';
    temp += '<div class="HiCloud_error_info_span">您的浏览器不兼容</div>';
    temp += '<div class="HiCloud_error_info_span2">通过您访问我们网站的信息，我们推荐您使用下列浏览器的最新版本：</div>';
    temp += '<div>';
    temp += '<a href="http://www.google.com/chrome/index.html" target="_blank">Chrome</a>,';
    temp += '<a href="http://www.mozilla.com/en-US/firefox/new/" target="_blank">Firefox</a>,';
    temp += '<a href="http://windows.microsoft.com/zh-CN/internet-explorer/downloads/ie-8" target="_blank">Internet Explorer8</a>';
    temp += '</div>';
    temp += '<ul class="btn_ul btn_ul2"><li>';
    temp += '<a onclick="continueAccessBrowse();" href="javascript:void(0);"><span class="btn_leftli"></span><span class="btn_centerli">' + searchResourse['cloud.browse.continue'] + '</span></a></li></ul>';
    temp += '</div>';
    temp += '<div class="loginlogo">';
    temp += '<img src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/f4b1d72ed5a2c8c2a66d048a919d4674_hicloud_error.gif" />';
    temp += '</div></div></div>';
    $(function () {
        var userHeadPic = $("#userHeadPic").val();
        $("#user_pic").css("background-image", "url(" + userHeadPic + ")");
        $("#center").mouseover(function () {
            $("#soft-center").show();
            $("#soft-info").removeClass("soft-info-arrow");
            $("#soft-info").addClass("soft-info-arrows");
        });
        $("#center").mouseleave(function () {
            $("#soft-center").hide();
            $("#soft-info").removeClass("soft-info-arrows");
            $("#soft-info").addClass("soft-info-arrow");
        });
        $("#userinfoId").mouseover(function () {
            $("#usertip").show();
            $("#user-info-arrow").removeClass("user-info-arrow");
            $("#user-info-arrow").addClass("user-info-arrows");
        });
        $("#userinfoId").mouseleave(function () {
            $("#usertip").hide();
            $("#user-info-arrow").removeClass("user-info-arrows");
            $("#user-info-arrow").addClass("user-info-arrow");
        });
        $("#languagetipId").mouseover(function () {
            $("#lang_list").show();
            $("#language-info-arrow").removeClass("language-info-arrow");
            $("#language-info-arrow").addClass("language-info-arrows");
        });
        $("#languagetipId").mouseleave(function () {
            $("#lang_list").hide();
            $("#language-info-arrow").removeClass("language-info-arrows");
            $("#language-info-arrow").addClass("language-info-arrow");
        });
    });
</script>

<iframe id="iframeLogout" width="0" height="0" style="display:none;"></iframe>
<input type="hidden" value='/' id="basePath"/>
<div class="lay-navi" style="z-index: 102;position:relative;">
    <div class="header-wrap eh-menu" style="z-index: 102;position:relative;">
        <ul class="ul-nav emo_nv cl">
                    <li value="1" id="a" class="navsign"><a href="/">首页</a></li>
                               <li value="2" class="navnormal a" onMouseOut="this.className='navnormal';"
                onMouseOver="this.className='navsign1';">
                <a href="/game/list">游戏</a>
            </li>
                                <li value="3" class="navnormal" onMouseOut="this.className='navnormal';"
                onMouseOver="this.className='navsign1';">
                <a href="/soft/list">软件</a>
            </li>
                                                <li value="4" class="navnormal" onMouseOut="this.className='navnormal';"
                onMouseOver="this.className='navsign1';">
                <a href="/topics">专题</a>
            </li>
                                  <li value="5" class="navnormal" onMouseOut="this.className='navnormal';"
                onMouseOver="this.className='navsign1';">
                <a href="/brands">品牌专区</a>
            </li>
                                </ul>
        <b class="navsign-move ehm-0"></b>
    </div>
</div>

    <div class="lay-main">
        <h5 class="bar10"></h5>
        <div class="lay-left corner">
            <div class="unit nofloat">

                <div class="unit-main">
                    <div class="dotline-btn list-game-app">
                        <h5 class="bar20"></h5>
                        <p class="content"><span><span class="sres">搜索到"英雄爱三国"的结果共181条</span></span>
                        </p>
                        <h5 class="bar20"></h5>
                    </div>
                                                            <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="新三国"
                               href="/app/C100746365">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;89637363e1734e4fa8bfdacabafdef5f.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_新三国">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="新三国"
                                   href="/app/C100746365">
                                    新三国                                </a>
                                <span class="score_7">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">《新三国》是一款以中国古代作为历史背景的立体三国策略经营手游，带玩家领略历史经典战役。游戏玩法丰富，除常规主线副本、竞技场、帮派系统、武将试练等玩法...</p>
                                <p class="date"><span>发布时间： 2019-05-07</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100746365','新三国','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;89&#x2F;89637363e1734e4fa8bfdacabafdef5f&#x2F;com.xsg.pl.huawei.1905062035.apk?sign=portal@portal1557798501492&amp;source=portalsite','17.56');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:&lt;10000次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="三国之空城计"
                               href="/app/C100427695">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;a6cc5ee2a5e5458c99ee0ce25c505000.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_三国之空城计">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="三国之空城计"
                                   href="/app/C100427695">
                                    三国之空城计                                </a>
                                <span class="score_9">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">《三国之空城计》是一款放置类策略卡牌游戏，以三国时期为背景，经典Q版精美画风，离线策略挂机，战斗升级更轻松，24小时轻松离线挂机，采用自动挂机的即时战...</p>
                                <p class="date"><span>发布时间： 2018-10-24</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100427695','三国之空城计','search_dl','20','角色扮演','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;a6&#x2F;a6cc5ee2a5e5458c99ee0ce25c505000&#x2F;com.bmyx.sgzkcj.huawei.1812171627.apk?sign=portal@portal1557798501492&amp;source=portalsite','1.0.91');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:3万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="鬼武三国志"
                               href="/app/C100029505">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;6d9606d0160f49dcbd4f52a321dd8e65.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_鬼武三国志">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="鬼武三国志"
                                   href="/app/C100029505">
                                    鬼武三国志                                </a>
                                <span class="score_6">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">国内硬派动作手游经典《鬼武三国志》。真硬派操作体验，爆爽快连击手感，重现十年硬派街机梦；东方幻想画风华丽，水墨渲染唯美飘逸，狂砸技能炫动全屏；冲刺斩...</p>
                                <p class="date"><span>发布时间： 2017-08-09</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100029505','鬼武三国志','search_dl','20','角色扮演','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;6d&#x2F;6d9606d0160f49dcbd4f52a321dd8e65&#x2F;com.yxgc.gwsgz.huawei.1708081737.apk?sign=portal@portal1557798501493&amp;source=portalsite','1.32.004');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:2万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="铜雀三国"
                               href="/app/C100492203">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;f554246e4cb9418185502a95e12087a3.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_铜雀三国">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="铜雀三国"
                                   href="/app/C100492203">
                                    铜雀三国                                </a>
                                <span class="score_8">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">东汉末年分三国，烽火连天战乱不休，一个个英雄横空出世揭竿而起，留下的名垂千古的佳话。经典动作策略手游《铜雀三国》以全新的战争策略，气势恢宏的场景刻...</p>
                                <p class="date"><span>发布时间： 2019-03-26</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100492203','铜雀三国','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;f5&#x2F;f554246e4cb9418185502a95e12087a3&#x2F;com.tqsg.chengwan.huawei.1903251641.apk?sign=portal@portal1557798501493&amp;source=portalsite','17.34');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:63万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="三国战天下"
                               href="/app/C100536475">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;f9514ba8f42248d8a98c2e928227a072.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_三国战天下">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="三国战天下"
                                   href="/app/C100536475">
                                    三国战天下                                </a>
                                <span class="score_7">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">《三国战天下》致力于打造一个全新的、不一样的三国世界,作为一款策略游戏,除特色的RPG玩法外，我们一直秉承的设计理念就是：让玩家来决定游戏内容，而我...</p>
                                <p class="date"><span>发布时间： 2019-01-28</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100536475','三国战天下','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;f9&#x2F;f9514ba8f42248d8a98c2e928227a072&#x2F;com.sytx.sgztx.huawei.1901251953.apk?sign=portal@portal1557798501493&amp;source=portalsite','1.2.600');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:1万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="乱！战三国"
                               href="/app/C100568197">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;092f42d05eab4b62822d761e094508da.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_乱！战三国">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="乱！战三国"
                                   href="/app/C100568197">
                                    乱！战三国                                </a>
                                <span class="score_9">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">横穿古代战场巅峰巨作，高度还原历史名将英姿。高品质游戏画面，即时动态阴影，超炫战斗视觉感受，真实细腻的战斗动作，行云流水般的击杀体验。坐拥美人，统领...</p>
                                <p class="date"><span>发布时间： 2019-01-10</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100568197','乱！战三国','search_dl','20','角色扮演','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;09&#x2F;092f42d05eab4b62822d761e094508da&#x2F;com.rylzsg.huawei.1901092016.apk?sign=portal@portal1557798501493&amp;source=portalsite','1.0.0');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:1万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="三国一统天下"
                               href="/app/C100201301">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;50c0d784d70b42889590c32004b3a739.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_三国一统天下">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="三国一统天下"
                                   href="/app/C100201301">
                                    三国一统天下                                </a>
                                <span class="score_7">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">《三国一统天下》是以“国战”为核心玩法的战争策略类游戏。<br>魏、蜀、吴三大势力三分天下, 明确的国家具有浓烈的三国时代带入感，呈现出一个虚拟的弱肉强食...</p>
                                <p class="date"><span>发布时间： 2019-02-25</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100201301','三国一统天下','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;50&#x2F;50c0d784d70b42889590c32004b3a739&#x2F;air.com.qmhygame.yttx.HUAWEI.1902251550.apk?sign=portal@portal1557798501494&amp;source=portalsite','4.5.0');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:1万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="街机三国志"
                               href="/app/C100332929">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;a823ee541f354663b15b2e7996e8b736.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_街机三国志">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="街机三国志"
                                   href="/app/C100332929">
                                    街机三国志                                </a>
                                <span class="score_6">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">这就是三国塔防《街机三国志》，让你回到三国当皇帝，史诗策略玩法看你运筹帷幄！《街机三国志》以三国为背景，重现这段历史充满英雄豪气、波澜壮阔的宏伟世界。...</p>
                                <p class="date"><span>发布时间： 2018-08-01</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100332929','街机三国志','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;a8&#x2F;a823ee541f354663b15b2e7996e8b736&#x2F;com.jjsgz.ysh.pld.huawei.1807311823.apk?sign=portal@portal1557798501494&amp;source=portalsite','3.2.51');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:1万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="鏖战三国"
                               href="/app/C100309565">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;5cd44aa093c44dce95a49cae1ba2a43b.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_鏖战三国">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="鏖战三国"
                                   href="/app/C100309565">
                                    鏖战三国                                </a>
                                <span class="score_8">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">《鏖战三国》是根据三国时代的历史改编的手机横版 PRG 网游，《鏖战三国》将三国时期的各路英雄人物由书面形象刻画为全新的 2D 形象，让威猛的吕布，神勇...</p>
                                <p class="date"><span>发布时间： 2018-07-01</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100309565','鏖战三国','search_dl','20','角色扮演','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;5c&#x2F;5cd44aa093c44dce95a49cae1ba2a43b&#x2F;com.rst.azsg.huawei.1806281018.apk?sign=portal@portal1557798501494&amp;source=portalsite','5.2.6');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:&lt;10000次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="造兵三国"
                               href="/app/C100263279">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;2e258b9feb42498e9e8faeaf5247c5f7.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_造兵三国">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="造兵三国"
                                   href="/app/C100263279">
                                    造兵三国                                </a>
                                <span class="score_8">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">《造兵三国》是一款高自由化的经营策略对战手游。在这里你将扮演乱世中的一位城主，在精美Q萌的3D世界中，建造城市招兵买马，养成骁勇善战的军队，探索世界...</p>
                                <p class="date"><span>发布时间： 2019-01-13</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100263279','造兵三国','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;2e&#x2F;2e258b9feb42498e9e8faeaf5247c5f7&#x2F;com.fingerfun.zbsg.huawei.1901112145.apk?sign=portal@portal1557798501495&amp;source=portalsite','2.4');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:22万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="漫画英雄3D"
                               href="/app/C100041257">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;29d67ca5767d41118e9e04dce9f4e730.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_漫画英雄3D">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="漫画英雄3D"
                                   href="/app/C100041257">
                                    漫画英雄3D                                </a>
                                <span class="score_9">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">二次元漫画英雄乱斗，神话英雄降临科技世界，冲破你的想象<br>哪怕坐在办公室，也能置身于异彩纷呈的冒险世界！<br>★★经典动漫 儿时期待★★<br>拳皇、龙...</p>
                                <p class="date"><span>发布时间： 2018-12-14</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100041257','漫画英雄3D','search_dl','20','角色扮演','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;29&#x2F;29d67ca5767d41118e9e04dce9f4e730&#x2F;com.xinghe.mhyx3d.huawei.1901071247.apk?sign=portal@portal1557798501495&amp;source=portalsite','1.11');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:109万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="群战三国"
                               href="/app/C100745767">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;45cd4592ed4b4bb4b4fd224dc7c121f3.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_群战三国">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="群战三国"
                                   href="/app/C100745767">
                                    群战三国                                </a>
                                <span class="score_10">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">群战三国是一款非常好玩的三国题材的3D塔防策略手游。游戏拥有完整的三国剧情副本，游戏之中在线的玩家非常多，超多的武将、各种阵容任你选择，激情的pk对...</p>
                                <p class="date"><span>发布时间： 2019-05-07</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100745767','群战三国','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;45&#x2F;45cd4592ed4b4bb4b4fd224dc7c121f3&#x2F;com.qzsgtfsgz.huawei.1905061706.apk?sign=portal@portal1557798501495&amp;source=portalsite','3.7.00');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:&lt;10000次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="权御三国"
                               href="/app/C10785180">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;0933839c9ab64c0bb7733ff4ad76d696.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_权御三国">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="权御三国"
                                   href="/app/C10785180">
                                    权御三国                                </a>
                                <span class="score_7">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">全新热门沙盘战略手游——《权御三国》强势来袭！惶惶乱世，群雄并起，智勇与权谋不断交锋，大战一触即发！呼朋引伴，统帅三军，意气风发，万世基业由此起。招名将、...</p>
                                <p class="date"><span>发布时间： 2018-02-07</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C10785180','权御三国','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;09&#x2F;0933839c9ab64c0bb7733ff4ad76d696&#x2F;com.hugenstar.sgzclient.huawei.1803121713.apk?sign=portal@portal1557798501495&amp;source=portalsite','1.18.1.30');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:38万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="激萌三国志"
                               href="/app/C100243397">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;7256d6303b764b72bea65bb0f8f55ac8.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_激萌三国志">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="激萌三国志"
                                   href="/app/C100243397">
                                    激萌三国志                                </a>
                                <span class="score_8">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">同是三国，但，我们不一样！<br>《三国志手游之群雄逐鹿》重拾当年的激情，千万玩家的难忘记忆！一样的经典角色，不一样的呆萌人设，收集卡牌不费力，激情对战有...</p>
                                <p class="date"><span>发布时间： 2018-04-23</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100243397','激萌三国志','search_dl','20','角色扮演','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;72&#x2F;7256d6303b764b72bea65bb0f8f55ac8&#x2F;com.moant.jmsg.huawei.1804230923.apk?sign=portal@portal1557798501496&amp;source=portalsite','1.1');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:2万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="挂机那三国"
                               href="/app/C100063015">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;d900be9944804da5adfeb74fcc0d823e.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_挂机那三国">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="挂机那三国"
                                   href="/app/C100063015">
                                    挂机那三国                                </a>
                                <span class="score_7">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">一款挂机放置类的游戏，游戏玩法虽然休闲，容易上手，但是节奏却很紧凑，内容却很饱满；5分钟上手，10分钟竞技，1小时割据一方，玩家很快就能体验到独霸天下的...</p>
                                <p class="date"><span>发布时间： 2017-11-21</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100063015','挂机那三国','search_dl','20','角色扮演','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;d9&#x2F;d900be9944804da5adfeb74fcc0d823e&#x2F;app.com.pfu.gjnsg.huawei.1711211322.apk?sign=portal@portal1557798501496&amp;source=portalsite','1.0.1');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:43万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="三国霸王大陆"
                               href="/app/C10785591">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;6e5103ee0e6441e6b71078746887888c.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_三国霸王大陆">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="三国霸王大陆"
                                   href="/app/C10785591">
                                    三国霸王大陆                                </a>
                                <span class="score_6">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">《三国霸王大陆》是三国战争策略游戏系列作品。<br>游戏系统沿袭三国群雄割据背景，游戏玩家化身三国名将，引领万马千军，武将征伐、攻城掠地，一统大好河山。<...</p>
                                <p class="date"><span>发布时间： 2017-08-31</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C10785591','三国霸王大陆','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;6e&#x2F;6e5103ee0e6441e6b71078746887888c&#x2F;com.android.sgbwdl.huawei.1708301743.apk?sign=portal@portal1557798501496&amp;source=portalsite','1.12');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:4万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="雷霆英雄"
                               href="/app/C100345085">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;2d5f284763d945e2ab592ccbbbca26a9.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_雷霆英雄">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="雷霆英雄"
                                   href="/app/C100345085">
                                    雷霆英雄                                </a>
                                <span class="score_9">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">2019经典复古热血私服手游《雷霆英雄》由专业团队打造，百分百经典还原，是一款顶级匠心传承的3D MMORPG 传奇手游之作。游戏以打BOSS爆装备，即...</p>
                                <p class="date"><span>发布时间： 2018-12-29</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100345085','雷霆英雄','search_dl','20','角色扮演','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;2d&#x2F;2d5f284763d945e2ab592ccbbbca26a9&#x2F;com.wanjie.ltyx.huawei.1905131403.apk?sign=portal@portal1557798501496&amp;source=portalsite','1.0.6310');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:34万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="三国群英传-霸王之业"
                               href="/app/C100086549">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;4279c2a71b164dfa9d6c6d2ddba87dd9.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_三国群英传-霸王之业">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="三国群英传-霸王之业"
                                   href="/app/C100086549">
                                    三国群英传-霸王之业                                </a>
                                <span class="score_6">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">《三国群英传-霸王之业》是一款官方正版授权的三国军争策略变革手游。游戏拥有精细写实的美术表现，激烈的城战抢夺活动，为玩家带来最为真实刺激的三国争霸...</p>
                                <p class="date"><span>发布时间： 2018-08-30</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100086549','三国群英传-霸王之业','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;42&#x2F;4279c2a71b164dfa9d6c6d2ddba87dd9&#x2F;com.tencent.tmgp.sgqyz.1808291924.apk?sign=portal@portal1557798501497&amp;source=portalsite','1.9.5');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:65万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="叫我三国迷"
                               href="/app/C10316066">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;78a6a45c59884b30be95eab840d84cd2.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_叫我三国迷">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="叫我三国迷"
                                   href="/app/C10316066">
                                    叫我三国迷                                </a>
                                <span class="score_9">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">以三国为题材全球同服万人在线的平民级三国、攻城、国战、策略的打仗战争游戏。游戏以东汉末年为背景，划分六州势力，多国争霸，千军破、王朝霸域、三十六计等...</p>
                                <p class="date"><span>发布时间： 2017-07-19</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C10316066','叫我三国迷','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;78&#x2F;78a6a45c59884b30be95eab840d84cd2&#x2F;com.fingerfly.sanguo.huawei.1707190957.apk?sign=portal@portal1557798501497&amp;source=portalsite','3.15');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:6万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="出击英雄岛"
                               href="/app/C100606287">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;5a57142c28ea46fe92c8114f12b92a0b.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_出击英雄岛">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="出击英雄岛"
                                   href="/app/C100606287">
                                    出击英雄岛                                </a>
                                <span class="score_7">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">出击英雄岛是一款动作冒险游戏，你将扮演一名遭受磨难的特工，为了寻找幕后的黑手潜入岛神秘组织当中，寻找凶手，在敌人的牢笼之中不断的寻找真相并且逃脱...</p>
                                <p class="date"><span>发布时间： 2019-02-22</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100606287','出击英雄岛','search_dl','20','角色扮演','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;5a&#x2F;5a57142c28ea46fe92c8114f12b92a0b&#x2F;com.wqhz.hjtg.huawei.1902231832.apk?sign=portal@portal1557798501497&amp;source=portalsite','1.0.4');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:71万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="步战三国"
                               href="/app/C100247721">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;4fcd3b2ee9854a899debe53d32a4d206.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_步战三国">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="步战三国"
                                   href="/app/C100247721">
                                    步战三国                                </a>
                                <span class="score_6">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">步战三国是一款Q版萌系RPG挂机卡牌手游。该作以三国题材为时代故事背景，充分还原三国内容，该作拥有极其丰富的人物属性、热血的打斗挂机玩法、多样的...</p>
                                <p class="date"><span>发布时间： 2019-03-12</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100247721','步战三国','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;4f&#x2F;4fcd3b2ee9854a899debe53d32a4d206&#x2F;com.baimagames.buzhansanguo.huawei.1903121544.apk?sign=portal@portal1557798501497&amp;source=portalsite','1.0.79');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:11万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="三国戏赵云传"
                               href="/app/C100695415">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;d2d33d661f894a2b864a2edffe029bf1.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_三国戏赵云传">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="三国戏赵云传"
                                   href="/app/C100695415">
                                    三国戏赵云传                                </a>
                                <span class="score_7">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">这是一个三国历史题材的回合制策略类游戏，游戏以战国历史为背景，像素风格。<br>三国时期，群雄争霸，各路豪杰征战沙场斗智斗勇，在这里你将扮演三国时...</p>
                                <p class="date"><span>发布时间： 2019-05-07</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100695415','三国戏赵云传','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;d2&#x2F;d2d33d661f894a2b864a2edffe029bf1&#x2F;com.game.kr.sgzzyz.huawei.1905071022.apk?sign=portal@portal1557798501498&amp;source=portalsite','1.0.1');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:186万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="逐鹿三国之君临天下"
                               href="/app/C10201540">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;ba1615e99e234a3aba8f182cb500d79d.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_逐鹿三国之君临天下">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="逐鹿三国之君临天下"
                                   href="/app/C10201540">
                                    逐鹿三国之君临天下                                </a>
                                <span class="score_7">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">全球同服的三国策略手游《君临天下》历经两年的沉淀，获得香港地区、日本等多个地区畅销榜首席！<br>2015年获得多个奖项：2015金翎奖 • 玩家最关注的移动网...</p>
                                <p class="date"><span>发布时间： 2017-05-12</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C10201540','逐鹿三国之君临天下','search_dl','20','角色扮演','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;ba&#x2F;ba1615e99e234a3aba8f182cb500d79d&#x2F;com.u9time.jltx.huawei.1705121805.apk?sign=portal@portal1557798501498&amp;source=portalsite','2.3.0');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:53万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                                        <div class="list-game-app dotline-btn nofloat">
                        <h5 class="bar25"></h5>
                        <div class="game-info-ico">
                            <a title="三国急攻防"
                               href="/app/C100162707">
                                <img class="app-ico" lazyload="http:&#x2F;&#x2F;appimg.hicloud.com&#x2F;hwmarket&#x2F;files&#x2F;application&#x2F;icon144&#x2F;726a580275524112b6a5fa6b5d617cc2.png"
                                     src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/133350dcdbe25b434c403d2fa33be5be_app_defult.png"
                                     onerror="show_app_defult(this , '//app.hicloud.com/publish/static/plugin/');"
                                     alt="华为应用市场_三国急攻防">
                            </a>
                        </div>
                        <div class="game-info  whole">
                            <h4 class="title">
                                <a title="三国急攻防"
                                   href="/app/C100162707">
                                    三国急攻防                                </a>
                                <span class="score_7">
                                        <em></em>
                                    </span>
                            </h4>
                            <div class="game-info-dtail part">
                                <p class="content">《三国急攻防》是一款三国题材策略塔防手机网游。本作由一群玩家组成的开发团队打造，萌系人物角色立体精致，场景画面清新唯美，融合多种全新玩法，创新塔防...</p>
                                <p class="date"><span>发布时间： 2018-04-24</span></p>
                            </div>
                            <div class="app-btn">
                                                                
                                <a class="btn-blue down" onclick="zhytools.downloadApp('C100162707','三国急攻防','search_dl','16','经营策略','http:&#x2F;&#x2F;appdlc.hicloud.com&#x2F;dl&#x2F;appdl&#x2F;application&#x2F;apk&#x2F;72&#x2F;726a580275524112b6a5fa6b5d617cc2&#x2F;com.tiantu.sgjgf.HUAWEI.1804222202.apk?sign=portal@portal1557798501498&amp;source=portalsite','4.0.1');">
                                    <span>下载</span>
                                </a>
                                                                
                                <span>下载:3万次</span>
                            </div>
                            <h5 class="bar25"></h5>
                        </div>
                    </div>
                    
                    <div class="page-ctrl ctrl-app" id="searchListPage">
                        <script type="text/javascript">
                            freshPage('searchListPage',
                                    '3',
                                    '181',
                                    '24',
                                    '//app.hicloud.com/search/英雄爱三国/');
                        </script>
                    </div>
                    
                    <h5 class="bar10"></h5>
                </div>
            </div>
        </div>

        <div class="lay-right corner">
            <div class="unit nofloat">
                <div class="unit-title  nofloat">
                    <span class="title flt ft-yh">搜索热词</span>
                </div>
                <div class="unit-main nofloat">
                                                            <div class="app-sweatch  nofloat">
                        <div class="close nofloat">
                            <em class="num-red">1</em>
                                                        <a title="购物" href="javascript:void(0);"
                               onclick="zhytools.searchHotKeys('//app.hicloud.com/','购物');">购物</a>
                        </div>
                    </div>
                                                            <div class="app-sweatch  nofloat">
                        <div class="close nofloat">
                            <em class="num-red">2</em>
                                                        <a title="贷款" href="javascript:void(0);"
                               onclick="zhytools.searchHotKeys('//app.hicloud.com/','贷款');">贷款</a>
                        </div>
                    </div>
                                                            <div class="app-sweatch  nofloat">
                        <div class="close nofloat">
                            <em class="num-red">3</em>
                                                        <a title="租房" href="javascript:void(0);"
                               onclick="zhytools.searchHotKeys('//app.hicloud.com/','租房');">租房</a>
                        </div>
                    </div>
                                                            <div class="app-sweatch  nofloat">
                        <div class="close nofloat">
                            <em class="num-grey">4</em>
                                                        <a title="视频" href="javascript:void(0);"
                               onclick="zhytools.searchHotKeys('//app.hicloud.com/','视频');">视频</a>
                        </div>
                    </div>
                                                            <div class="app-sweatch  nofloat">
                        <div class="close nofloat">
                            <em class="num-grey">5</em>
                                                        <a title="新闻" href="javascript:void(0);"
                               onclick="zhytools.searchHotKeys('//app.hicloud.com/','新闻');">新闻</a>
                        </div>
                    </div>
                                    </div>
                <h5 class="bar20"></h5>
            </div>
        </div>
        <h5 class="bar40"></h5>
    </div>
</div>

<div class="lay-foot">
    <div class="foot1-foot-left foot-line">
        <div class="foot1-info  nofloat">
          <span class ="footer1_wet">
             <a href="/useragreement" rel="noopener noreferrer" target="_blank">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用户协议</a>
             &nbsp;
             <a href="http://consumer.huawei.com/cn/privacy-policy/index.htm" rel="noopener noreferrer" target="_blank">隐私政策</a>
             &nbsp;
             <a href="https://consumer.huawei.com/cn/legal/cookie-policy/" rel="noopener noreferrer" target="_blank">关于cookies</a>&nbsp;
             版权所有
             <img style="vertical-align:middle;" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2017/01/18/4845b947435a89b86f7f43a550b12dbc_%E7%AC%A6%E5%8F%B7.png?mode=download"/>
             2010-2019
             华为软件技术有限公司保留一切权利
          </span>
        </div>
        <p class="foot1-info  nofloat" style="text-align:center;margin-left:75px;">
            <a href="/suwangwen.htm" class="foot-cor" target="_blank">苏网文&nbsp;[2015]&nbsp;1599-026号</a>
            <em class="ico hd">|</em>
            <a href="http://www.miitbeian.gov.cn/" class="foot-cor" target="_blank" rel="noopener noreferrer">粤ICP备09176709号-16</a>
            <em class="ico hd">|</em>
            <span>苏B2-20130048号</span>
            <em class="ico hd">|</em>
            <a href="https://www.beian.gov.cn/portal/registerSystemInfo?recordcode=32011402010009" class="foot-cor" target="_blank" rel="noopener noreferrer">苏公网安备32011402010009号</a>
            <em class="ico hd">|</em>
            <a href="/busi/Business.htm" class="foot-cor" target="_blank" rel="external nofollow">电子营业执照</a>
        </p>       
        <p class="foot1-info  nofloat" style="text-align:center;margin-left:75px;">
            <a target="_blank" rel="noopener noreferrer"href="http://white.anva.org.cn">
            <img style="height: 20px;width: 20px;vertical-align: bottom;" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2019/02/18/459FCB42930D12308EDCF5572D034AB3.png"/>
            中国反网络病毒联盟应用商店自律组</a>
            <em class="ico hd">|</em>
            <a href="/jiazhang/jzjh.htm" rel="external nofollow" target="_blank">未成年人家长监护体系</a> 
            <em class="ico hd">|</em>            
            违法和不良信息举报电话：4008308300 <em class="ico hd">|</em>
            <a href="http://developer.huawei.com/consumer/cn/devservice/support" rel="noopener noreferrer" target="_blank">商务合作</a> <em class="ico hd">|</em>
            <a href="/contactus" rel="external nofollow" target="_blank">联系我们</a>
            <a class="mlt10" href="http://e.weibo.com/hispacehw" rel="noopener noreferrer" target="_blank">
             <img style="vertical-align:middle;" src="http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/9e0ac143f38d5fd889ed39edf373f4a8_webo-sina.png"
                  onMouseOver="this.src='http://emuirom.hicloud.com/dl/emuirom123/attachment/2016/11/07/9e0ac143f38d5fd889ed39edf373f4a8_webo-sina.png'" width="20" height="17"/>
            </a> 
        </p>       
    </div>
</div>

<script type="text/javascript">
    var _paq = _paq || [];
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', '']);
    _gaq.push(['_addOrganic', 'soso', 'w']);
    _gaq.push(['_addOrganic', 'yodao', 'q']);
    _gaq.push(['_addOrganic', 'sogou', 'query']);
    _gaq.push(['_trackPageview']);
</script>

<div id="dynamicElement"></div>
</body>
</html>"""
    # extractor.get_next_page(html)
    # extractor.judge_page_num(html)