import pymysql
import pyecharts.options as opts
from pyecharts.charts import Line, Pie

def create_temp():
    db = pymysql.connect(host="localhost", user="root", passwd="Zeng&98426", db="weather", charset='utf8' )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM weather_spider;')
    data = cursor.fetchall()
    max_temp_list = []
    min_temp_list = []
    day_list = []
    for d in data:
        max_temp_list.append(d[3].split('/')[0].replace('℃', ''))
        min_temp_list.append(d[3].split('/')[1].replace('℃', ''))
        day_list.append(d[0][:11])
    line = Line()
    line.add_xaxis(day_list)
    line.add_yaxis("最高温度",max_temp_list)
    line.add_yaxis("最低温度",min_temp_list)
    line.set_global_opts(yaxis_opts=opts.AxisOpts(name="温度（℃）"), title_opts=opts.TitleOpts(title="南京气温变化表"))
    
    line.render('南京2019气温变化表.html')
    print('气温图生成成功')
    db.close()
    cursor.close()

def create_weather():
    db = pymysql.connect(host="localhost", user="root", passwd="Zeng&98426", db="weather", charset='utf8' )
    cursor = db.cursor()
    attr = ["雨", "多云", "晴", "阴", "雪", "雾", "霾"]
    rain = cursor.execute('SELECT * FROM weather_spider WHERE weather_type like "%雨%";')
    cloud = cursor.execute('SELECT * FROM weather_spider WHERE weather_type like "%多云%";')
    sun = cursor.execute('SELECT * FROM weather_spider WHERE weather_type like "%晴%";')
    overcast = cursor.execute('SELECT * FROM weather_spider WHERE weather_type like "%阴%";')
    snow = cursor.execute('SELECT * FROM weather_spider WHERE weather_type like "%雪%";')
    fog = cursor.execute('SELECT * FROM weather_spider WHERE weather_type like "%雾%";')
    smog = cursor.execute('SELECT * FROM weather_spider WHERE weather_type like "%霾%";')
    weather = [rain, cloud, sun, overcast, snow, fog, smog]
    pie = (
        Pie()
        .add("", [list(z) for z in zip(attr, [rain, cloud, sun, overcast, snow, fog, smog])])
        .set_global_opts(title_opts=opts.TitleOpts(title="天气占比表"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    
    pie.render('南京2019天气占比表.html')
    print('天气图生成成功')
    db.close()
    cursor.close()


if __name__ == '__main__':
    create_temp()
    create_weather()