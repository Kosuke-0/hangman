import pytest
import sys
sys.path.append('./src/dao')
from texttojson import TEXTtoJSON
t1 = TEXTtoJSON()

def test_convert():
    assert t1.convert('./resources/format/text.json','./resources/data/20xx-text.text','./resources/data/20xx-text_error.text') == {'data':[
        {'name':"Yamada Taro",'department':"IT",'salary':4004000},
        {'name':"五郎 山本",'department':"漁業",'salary':4756000},
        {'name':"健太 鈴木",'department':"農業",'salary':5912000},
        {'name':"一郎 林",'department':"林業",'salary':350000},
        {'name':"Mike Honda",'department':"サービス",'salary':2590000},
        {'name':"Oliver Alba",'department':"IT",'salary':3600000},
        {'name':"Emma Armstrong",'department':"IT",'salary':7300000}]}

    assert t1.convert('./resources/format/bad-csv.json','./resources/data/20xx-text.text','./resources/data/20xx-text_error.text') == None

    t1.convert('./resources/format/text.json','./resources/data/bad-20xx-text.text','./resources/data/20xx-text_error.text') == '3Taro Yamada 農業 エラー 300000 300000 300000 300000 300000 300000 300000 300000 300000 300000 300000''6Taro Yamada IT 300000 300000 300000 300000 300000 300000 300000 300000 300000 エラー 300000 300000'