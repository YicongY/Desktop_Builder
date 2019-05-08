# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import DateTime
import datetime
from scrapy.conf import settings
from scrapy.exceptions import DropItem


class AresPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(user=settings['MYSQL_USER'], passwd=settings['MYSQL_PASSWORD'],
                                    db=settings['MYSQL_DB'], host=settings['MYSQL_SERVER'],
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))

        if valid and spider.name == 'neweggcpu':
            self.cursor.execute("""SELECT * FROM cpu WHERE model = %s""", [item['model']])
            checkmodel = self.cursor.fetchall()

            if len(checkmodel) == 0:
                self.cursor.executemany("""INSERT INTO cpu (brand, model, price, url,
                                                              socket, name, rate,
                                                              created_ts)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                                             [(item['brand'],
                                               item['model'],
                                               item['price'],
                                               item['url'],
                                               item['socket'],
                                               item['name'],
                                               item['rating'],
                                               datetime.datetime.now(),
                                                )])
                id = self.cursor.lastrowid
                for review in item['reviews']:
                    self.cursor.executemany("""INSERT INTO cpu_review (board_id,cons, pros, others, rating, time)
                                          VALUES (%s,%s, %s, %s, %s, %s)""", [(int(id), review['cons'],
                                                                               review['pros'],
                                                                               review['others'],
                                                                               review['rating'],
                                                                               review['date'],
                                                                               )])
            self.conn.commit()
        elif valid and spider.name == 'neweggintelboard':
            self.cursor.execute("SELECT * FROM intelboard WHERE model = %s", [item['model']])
            checkmodel = self.cursor.fetchall()

            if len(checkmodel) == 0:
                self.cursor.executemany("""INSERT INTO intelboard (make, price, url, rate, model, name, created_ts,socket)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", [(item['make'],
                                                                                    item['price'],
                                                                                    item['url'],
                                                                                    item['rate'],
                                                                                    item['model'],
                                                                                    item['name'],
                                                                                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                                                    item['socket'],
                                                                                    )])
                id = self.cursor.lastrowid
                for review in item['reviews']:
                    self.cursor.executemany("""INSERT INTO intelboard_review (board_id,cons, pros, others, rating, time)
                                          VALUES (%s,%s, %s, %s, %s, %s)""", [(int(id), review['cons'],
                                                                               review['pros'],
                                                                               review['others'],
                                                                               review['rating'],
                                                                               review['date'],
                                                                               )])
            self.conn.commit()

        elif valid and spider.name == 'neweggamdboard':
            self.cursor.execute("SELECT * FROM amdboard WHERE model = %s", [item['model']])
            checkmodel = self.cursor.fetchall()

            if len(checkmodel) == 0:
                self.cursor.executemany("""INSERT INTO amdboard (make, price, url, rate, model, name, created_ts,socket)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", [(item['make'],
                                                                       item['price'],
                                                                       item['url'],
                                                                       item['rate'],
                                                                       item['model'],
                                                                       item['name'],
                                                                       datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                                       item['socket'],
                                                                       )])
                id = self.cursor.lastrowid
                for review in item['reviews']:
                    self.cursor.executemany("""INSERT INTO amdboard_review (board_id,cons, pros, others, rating, time)
                                          VALUES (%s,%s, %s, %s, %s, %s)""", [(int(id), review['cons'],
                                                                                   review['pros'],
                                                                                   review['others'],
                                                                                   review['rating'],
                                                                                   review['date'],
                                                                                   )])
            self.conn.commit()

        elif valid and spider.name == 'neweggram':
            self.cursor.executemany("""INSERT INTO ram (brand, model, capacity, speed, ram_type, color, led, price, url,
                                                              name, rate,
                                                              created_ts)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                     [(item['brand'],
                                       item['model'],
                                       item['capacity'],
                                       item['speed'],
                                       item['ram_type'],
                                       item['color'],
                                       item['led'],
                                       item['price'],
                                       item['url'],
                                       item['name'],
                                       item['rating'],
                                       datetime.datetime.now(),
                                       )])
            id = self.cursor.lastrowid
            for review in item['reviews']:
                self.cursor.executemany("""INSERT INTO ram_review (board_id,cons, pros, others, rating, time)
                                          VALUES (%s,%s, %s, %s, %s, %s)""", [(int(id), review['cons'],
                                                                               review['pros'],
                                                                               review['others'],
                                                                               review['rating'],
                                                                               review['date'],
                                                                               )])
            self.conn.commit()

        elif valid and spider.name == 'newegggpu':

            self.cursor.executemany("""INSERT INTO gpu (brand, model, price, url,
                                                              socket, name, rate,
                                                              created_ts)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                                    [(item['brand'],
                                      item['model'],
                                      item['price'],
                                      item['url'],
                                      item['socket'],
                                      item['name'],
                                      item['rating'],
                                      datetime.datetime.now(),
                                      )])
            id = self.cursor.lastrowid
            for review in item['reviews']:
                self.cursor.executemany("""INSERT INTO gpu_review (board_id,cons, pros, others, rating, time)
                                          VALUES (%s,%s, %s, %s, %s, %s)""", [(int(id), review['cons'],
                                                                               review['pros'],
                                                                               review['others'],
                                                                               review['rating'],
                                                                               review['date'],
                                                                               )])
            self.conn.commit()

        elif valid and spider.name == 'neweggcase':
            self.cursor.executemany("""INSERT INTO desktop_case (brand, type, compatibility, color,price, url,
                                                              name, rate,
                                                              created_ts)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                    [(item['brand'],
                                      item['type'],
                                      item['compatibility'],
                                      item['color'],
                                      item['price'],
                                      item['url'],
                                      item['name'],
                                      item['rating'],
                                      datetime.datetime.now(),
                                      )])
            id = self.cursor.lastrowid
            for review in item['reviews']:
                self.cursor.executemany("""INSERT INTO case_review (board_id,cons, pros, others, rating, time)
                                          VALUES (%s,%s, %s, %s, %s, %s)""", [(int(id), review['cons'],
                                                                               review['pros'],
                                                                               review['others'],
                                                                               review['rating'],
                                                                               review['date'],
                                                                               )])
            self.conn.commit()


        elif valid and spider.name == 'newegghdd':
            self.cursor.executemany("""INSERT INTO hdd (brand, model, capacity, price, url,
                                                              name, rate, rpm,
                                                              created_ts)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                    [(item['brand'],
                                      item['model'],
                                      item['capacity'],
                                      item['price'],
                                      item['url'],
                                      item['name'],
                                      item['rating'],
                                      item['rpm'],
                                      datetime.datetime.now(),
                                      )])
            id = self.cursor.lastrowid
            for review in item['reviews']:
                self.cursor.executemany("""INSERT INTO hdd_review (board_id,cons, pros, others, rating, time)
                                          VALUES (%s,%s, %s, %s, %s, %s)""", [(int(id), review['cons'],
                                                                               review['pros'],
                                                                               review['others'],
                                                                               review['rating'],
                                                                               review['date'],
                                                                               )])
            self.conn.commit()

        elif valid and spider.name == 'neweggssd':
            if item['images']:
                imageitem = item['images'][0]['path'].replace("full/", "")
            else:
                imageitem = None
            self.cursor.execute("SELECT * FROM A_Storage WHERE modelname = %s", [item['modelname']])
            checkmodel = self.cursor.fetchall()
            if len(checkmodel) > 0:
                checkmodel = checkmodel[0]
                #print checkmodel
                if checkmodel[9] == item['modelname'] and str(checkmodel[5]) != str(item['price']).replace(",", ""):
                    self.cursor.execute("UPDATE A_Storage SET price=%s, updated_ts=%s WHERE sid=%s",
                                        (str(item['price']).replace(",", ""), DateTime.DateTime.now(), checkmodel[0]))
            elif len(checkmodel) == 0:
                self.cursor.executemany("""INSERT INTO A_Storage (make, model, modelname, form_factor, price, neweggurl,
                                            size, type, created_ts, image, max_seq_read, max_seq_write, k_ran_read,
                                            k_ran_write, controller)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                                                                    [(item['make'],
                                                                                      item['model'],
                                                                                      item['modelname'],
                                                                                      item['form_factor'],
                                                                                      item['price'],
                                                                                      item['url'],
                                                                                      item['size'],
                                                                                      'SSD',
                                                                                      DateTime.DateTime.now(),
                                                                                      imageitem,
                                                                                      item['max_seq_read'],
                                                                                      item['max_seq_write'],
                                                                                      item['k_ran_read'],
                                                                                      item['k_ran_write'],
                                                                                      item['controller']
                                                                                      )])
            self.conn.commit()

        elif valid and spider.name == 'neweggpsu':
            self.cursor.executemany("""INSERT INTO psu (brand, type, power, price, url,
                                                              name, rate,
                                                              created_ts)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                                    [(item['brand'],
                                      item['type'],
                                      item['power'],
                                      item['price'],
                                      item['url'],
                                      item['name'],
                                      item['rating'],
                                      datetime.datetime.now(),
                                      )])
            id = self.cursor.lastrowid
            for review in item['reviews']:
                self.cursor.executemany("""INSERT INTO psu_review (board_id,cons, pros, others, rating, time)
                                          VALUES (%s,%s, %s, %s, %s, %s)""", [(int(id), review['cons'],
                                                                               review['pros'],
                                                                               review['others'],
                                                                               review['rating'],
                                                                               review['date'],
                                                                               )])
            self.conn.commit()

        return item
