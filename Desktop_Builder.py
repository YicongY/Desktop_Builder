import pymysql
import DateTime
import datetime
import math
import sys
import time
import heapq as hq
import metapy
import pytoml
import json
import shutil
import os
from scrapy.conf import settings

from budget import basic_budget, gaming_budget, working_budget


class Desktop_Builder(object):

    def __init__(self,para):
        self.money = para['money']
        self.ram_size = {'basic': ['8'], 'gaming': ['16', '32'], 'working':['16', '32']}
        self.hdd_size = {'basic': ['1'], 'gaming': ['1', '2'], 'working':['1', '2']}
        if para['purpose'] == 'basic':
            self.budget = basic_budget()
        elif para['purpose'] == 'gaming':
            self.budget = gaming_budget()
        elif para['purpose'] == "working":
            self.budget = working_budget()

        #sql initialization
        self.conn = pymysql.connect(user=settings['MYSQL_USER'], passwd=settings['MYSQL_PASSWORD'],
                                    db=settings['MYSQL_DB'], host=settings['MYSQL_SERVER'],
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def tf_cal_process(self, reviews, user_query):
        #Output temporory documents for search with tf-idf
        corpus = open('tmp_corpus/tmp_corpus.dat', 'w')
        for index, review in enumerate(reviews):
            corpus.write(review + '\n')
        corpus.close()

        #tf-idf process
        idx = metapy.index.make_inverted_index('config.toml')
        doc_num = idx.num_docs()
        query = metapy.index.Document()
        ranker = metapy.index.OkapiBM25(k1=1.2,b=0.75,k3=500)
        query.content(user_query)
        tf_results = ranker.score(idx, query, doc_num)
        os.remove('tmp_corpus/tmp_corpus.dat')
        shutil.rmtree('idx')
        return tf_results

    def cal_final_core(self, alpha, tf_result, ratings, line_to_id):
        hp = []

        for tf in tf_result:
            line_index = tf[0]
            tf_score = tf[1]
            final_score = alpha * float(ratings[line_to_id[line_index]]) + (1 - alpha) * tf_score
            hq.heappush(hp, (-final_score, line_to_id[line_index]))
        ret = []
        for t in hp[0:3]:
            ret.append(t[1])
        return ret


    def recommender(self,components, user_query, option_para):
        if components == 'cpu':
            budget_money = self.money * self.budget.budget['cpu']

            min_budget_money = self.money * (self.budget.budget['cpu'] - 0.1)
            max_budget_money = self.money * (self.budget.budget['cpu'] + 0.1)

            self.cursor.execute("""SELECT id, rate, brand, url FROM cpu WHERE price between %s and %s """, [min_budget_money, max_budget_money])
            checkmodel = self.cursor.fetchall()
            reviews = []
            line_to_boardid = {}
            id_to_rating = {}
            id_to_brand = {}
            id_to_url = {}
            for i in checkmodel:
                id = i[0]
                id_to_brand[id] = i[2]
                id_to_url[id] = i[3]
                tmp = ''
                average_rating = 0
                self.cursor.execute("""SELECT others, rating FROM cpu_review WHERE board_id = %s """, [id])
                check_review = self.cursor.fetchall()

                for rev in check_review:
                    tmp += rev[0]
                    average_rating += int(rev[1])
                print(tmp)
                if len(check_review) > 0:
                    id_to_rating[id] = round(average_rating/len(check_review),2)
                else:
                    id_to_rating[id] = 0

                reviews.append(tmp)
            for index, val in enumerate(checkmodel):
                line_to_boardid[index] = val[0]

            tf_results = self.tf_cal_process(reviews, user_query)


            if len(tf_results) < 3:
                rating_tuple = []
                for key, val in id_to_rating.items():
                    rating_tuple.append((val, key))
                rating_tuple.sort(reverse= True)
                return_url = []
                return_id = []
                for t in rating_tuple:
                    return_id.append(t[1])
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)
            else:
                return_id = self.cal_final_core(0.3, tf_results, id_to_rating, line_to_boardid)
                return_url = []
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)

        elif components == 'motherboard':
            budget_money = self.money * self.budget.budget['board']

            min_budget_money = self.money * (self.budget.budget['board'] - 0.01)
            max_budget_money = self.money * (self.budget.budget['board'] + 0.01)
            board_type = option_para['board_type']

            if board_type == 'intel':
                self.cursor.execute("""SELECT id, rate, url FROM intelboard WHERE price between %s and %s and socket = %s """, [min_budget_money, max_budget_money, option_para['socket']])
            elif board_type == 'amd':
                self.cursor.execute("""SELECT id, rate, url FROM amdboard WHERE price between %s and %s and socket = %s """, [min_budget_money, max_budget_money, option_para['socket']])
            checkmodel = self.cursor.fetchall()
            reviews = []
            line_to_boardid = {}
            id_to_rating = {}
            id_to_url = {}
            for i in checkmodel:
                id = i[0]
                id_to_url[id] = i[2]
                tmp = ''
                average_rating = 0
                if board_type == 'intel':
                    self.cursor.execute("""SELECT others, rating FROM intelboard_review WHERE board_id = %s """, [id])
                elif board_type == 'amd':
                    self.cursor.execute("""SELECT others, rating FROM amdboard_review WHERE board_id = %s """, [id])
                check_review = self.cursor.fetchall()
                for rev in check_review:
                    tmp += rev[0]
                    average_rating += int(rev[1])
                if len(check_review) > 0:
                    id_to_rating[id] = round(average_rating/len(check_review),2)
                else:
                    id_to_rating[id] = 0

                reviews.append(tmp)
            for index, val in enumerate(checkmodel):
                line_to_boardid[index] = val[0]
            tf_results = self.tf_cal_process(reviews, user_query)
            print(tf_results)
            if len(tf_results) < 3:
                rating_tuple = []
                for key, val in id_to_rating.items():
                    rating_tuple.append((val, key))
                rating_tuple.sort(reverse= True)
                return_url = []
                return_id = []
                for t in rating_tuple:
                    return_id.append(t[1])
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)
            else:
                return_id = self.cal_final_core(0.3, tf_results, id_to_rating, line_to_boardid)
                return_url = []
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)

        elif components == 'gpu':
            budget_money = self.money * self.budget.budget['gpu']

            min_budget_money = self.money * (self.budget.budget['gpu'] - 0.1)
            max_budget_money = self.money * (self.budget.budget['gpu'] + 0.1)

            self.cursor.execute("""SELECT id, rate, brand, url FROM gpu WHERE price between %s and %s """, [min_budget_money, max_budget_money])
            checkmodel = self.cursor.fetchall()
            reviews = []
            line_to_boardid = {}
            id_to_rating = {}
            id_to_brand = {}
            id_to_url = {}
            for i in checkmodel:
                id = i[0]
                id_to_brand[id] = i[2]
                id_to_url[id] = i[3]
                tmp = ''
                average_rating = 0
                self.cursor.execute("""SELECT others, rating FROM gpu_review WHERE board_id = %s """, [id])
                check_review = self.cursor.fetchall()

                for rev in check_review:
                    tmp += rev[0]
                    average_rating += int(rev[1])
                if len(check_review) > 0:
                    id_to_rating[id] = round(average_rating/len(check_review),2)
                else:
                    id_to_rating[id] = 0

                reviews.append(tmp)
            for index, val in enumerate(checkmodel):
                line_to_boardid[index] = val[0]

            tf_results = self.tf_cal_process(reviews, user_query)

            if len(tf_results) < 3:
                rating_tuple = []
                for key, val in id_to_rating.items():
                    rating_tuple.append((val, key))
                rating_tuple.sort(reverse= True)
                return_url = []
                return_id = []
                for t in rating_tuple:
                    return_id.append(t[1])
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)
            else:
                return_id = self.cal_final_core(0.3, tf_results, id_to_rating, line_to_boardid)
                return_url = []
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)

        elif components == 'case':
            budget_money = self.money * self.budget.budget['case']

            min_budget_money = self.money * (self.budget.budget['case'] - 0.01)
            max_budget_money = self.money * (self.budget.budget['case'] + 0.01)
            if 'case_color' in option_para:
                case_color = option_para['case_color']
                self.cursor.execute("""SELECT id, rate, brand, url FROM desktop_case WHERE color = %s AND price between %s and %s""", [case_color, min_budget_money, max_budget_money])
            else:
                self.cursor.execute("""SELECT id, rate, brand, url FROM desktop_case WHERE price between %s and %s""", [min_budget_money, max_budget_money])
            checkmodel = self.cursor.fetchall()
            reviews = []
            line_to_boardid = {}
            id_to_rating = {}
            id_to_brand = {}
            id_to_url = {}
            for i in checkmodel:
                id = i[0]
                id_to_brand[id] = i[2]
                id_to_url[id] = i[3]
                tmp = ''
                average_rating = 0
                self.cursor.execute("""SELECT others, rating FROM case_review WHERE board_id = %s """, [id])
                check_review = self.cursor.fetchall()

                for rev in check_review:
                    tmp += rev[0]
                    average_rating += int(rev[1])
                if len(check_review) > 0:
                    id_to_rating[id] = round(average_rating/len(check_review),2)
                else:
                    id_to_rating[id] = 0

                reviews.append(tmp)
            for index, val in enumerate(checkmodel):
                line_to_boardid[index] = val[0]

            tf_results = self.tf_cal_process(reviews, user_query)


            if len(tf_results) < 3:
                rating_tuple = []
                for key, val in id_to_rating.items():
                    rating_tuple.append((val, key))
                rating_tuple.sort(reverse= True)
                return_url = []
                return_id = []
                for t in rating_tuple:
                    return_id.append(t[1])
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)
            else:
                return_id = self.cal_final_core(0.3, tf_results, id_to_rating, line_to_boardid)
                return_url = []
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)

        elif components == 'ram':
            budget_money = self.money * self.budget.budget['ram']

            min_budget_money = self.money * (self.budget.budget['ram'] - 0.05)
            max_budget_money = self.money * (self.budget.budget['ram'] + 0.05)
            if len(self.ram_size[para['purpose']]) > 1 and 'ram_rgb' in option_para:

                self.cursor.execute("""SELECT id, rate, brand, url FROM ram WHERE price between %s and %s and capacity between %s and %s and led = %s""", [min_budget_money, max_budget_money, self.ram_size[para['purpose']][0],self.ram_size[para['purpose']][1], option_para['ram_rgb']])
            elif len(self.ram_size[para['purpose']]) <= 1 and 'ram_rgb' in option_para:
                self.cursor.execute("""SELECT id, rate, brand, url FROM ram WHERE price between %s and %s and capacity = %s and led = %s""", [min_budget_money, max_budget_money, self.ram_size[para['purpose']][0], option_para['ram_rgb']])
            elif len(self.ram_size[para['purpose']]) <= 1 and 'ram_rgb' not in option_para:
                self.cursor.execute("""SELECT id, rate, brand, url FROM ram WHERE price between %s and %s and capacity = %s""", [min_budget_money, max_budget_money, self.ram_size[para['purpose']][0]])
            elif len(self.ram_size[para['purpose']]) > 1 and 'ram_rgb' not in option_para:
                self.cursor.execute("""SELECT id, rate, brand, url FROM ram WHERE price between %s and %s and capacity between %s and %s""", [min_budget_money, max_budget_money, self.ram_size[para['purpose']][0],self.ram_size[para['purpose']][1]])

            checkmodel = self.cursor.fetchall()
            reviews = []
            line_to_boardid = {}
            id_to_rating = {}
            id_to_brand = {}
            id_to_url = {}
            for i in checkmodel:
                id = i[0]
                id_to_brand[id] = i[2]
                id_to_url[id] = i[3]
                tmp = ''
                average_rating = 0
                self.cursor.execute("""SELECT others, rating FROM ram_review WHERE board_id = %s """, [id])
                check_review = self.cursor.fetchall()

                for rev in check_review:
                    tmp += rev[0]
                    average_rating += int(rev[1])
                print(tmp)
                if len(check_review) > 0:
                    id_to_rating[id] = round(average_rating/len(check_review),2)
                else:
                    id_to_rating[id] = 0

                reviews.append(tmp)
            for index, val in enumerate(checkmodel):
                line_to_boardid[index] = val[0]

            tf_results = self.tf_cal_process(reviews, user_query)


            if len(tf_results) < 3:
                rating_tuple = []
                for key, val in id_to_rating.items():
                    rating_tuple.append((val, key))
                rating_tuple.sort(reverse= True)
                return_url = []
                return_id = []
                for t in rating_tuple:
                    return_id.append(t[1])
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)
            else:
                return_id = self.cal_final_core(0.3, tf_results, id_to_rating, line_to_boardid)
                return_url = []
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)

        elif components == 'hdd':
            budget_money = self.money * self.budget.budget['hdd']

            min_budget_money = self.money * (self.budget.budget['hdd'] - 0.03)
            max_budget_money = self.money * (self.budget.budget['hdd'] + 0.03)
            if len(self.ram_size[para['purpose']]) > 1:

                self.cursor.execute("""SELECT id, rate, brand, url FROM hdd WHERE price between %s and %s and capacity between %s and %s""", [min_budget_money, max_budget_money, self.hdd_size[para['purpose']][0],self.hdd_size[para['purpose']][1]])
            elif len(self.ram_size[para['purpose']]) <= 1:
                self.cursor.execute("""SELECT id, rate, brand, url FROM hdd WHERE price between %s and %s and capacity = %s""", [min_budget_money, max_budget_money, self.hdd_size[para['purpose']][0]])

            checkmodel = self.cursor.fetchall()
            reviews = []
            line_to_boardid = {}
            id_to_rating = {}
            id_to_brand = {}
            id_to_url = {}
            for i in checkmodel:
                id = i[0]
                id_to_brand[id] = i[2]
                id_to_url[id] = i[3]
                tmp = ''
                average_rating = 0
                self.cursor.execute("""SELECT others, rating FROM hdd_review WHERE board_id = %s """, [id])
                check_review = self.cursor.fetchall()

                for rev in check_review:
                    tmp += rev[0]
                    average_rating += int(rev[1])
                if len(check_review) > 0:
                    id_to_rating[id] = round(average_rating/len(check_review),2)
                else:
                    id_to_rating[id] = 0

                reviews.append(tmp)
            for index, val in enumerate(checkmodel):
                line_to_boardid[index] = val[0]

            tf_results = self.tf_cal_process(reviews, user_query)


            if len(tf_results) < 3:
                rating_tuple = []
                for key, val in id_to_rating.items():
                    rating_tuple.append((val, key))
                rating_tuple.sort(reverse= True)
                return_url = []
                return_id = []
                for t in rating_tuple:
                    return_id.append(t[1])
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)
            else:
                return_id = self.cal_final_core(0.3, tf_results, id_to_rating, line_to_boardid)
                return_url = []
                for u in return_id:
                    return_url.append(id_to_url[u])
                print("the list you want", return_url)

if __name__ == '__main__':
    para = {}
    para['money'] = 1000
    para['purpose'] = 'basic'

    builder = Desktop_Builder(para)
    option_para = {}
    #builder.recommender('cpu', 'fast',option_para)

    option_para['board_type'] = 'intel'
    option_para['socket'] = '775'
    #builder.recommender('motherboard', 'fast',option_para)
    #builder.recommender('gpu', 'low power',option_para)
    option_para['case_color'] = 'black'
    #builder.recommender('case', 'cool',option_para)
    option_para['ram_rgb'] = 'No'
    builder.recommender('ram', 'fast',option_para)
    builder.recommender('hdd', 'large', option_para)