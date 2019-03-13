# coding=utf-8

import pymysql

class Do:
    def do_dql(self, sql):
        global id
        connection = pymysql.connect(host='192.168.111.243', port=3306, user='zjmax', password='zjmax.com',db='num_pro', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        sql = sql
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        print results
        for row in results:
            id = row["id"]
        connection.close()
        return id


Reviewed = {
    "ReviewedUrl":"http://admin.tjs.com/server/product/update_status.html"
}
Sql1 = "SELECT id FROM n_product WHERE NAME = '城建系列1'"


pc1 = Do()
prodictId1 = 0
prodictId1 = pc1.do_dql(Sql1)
ReviewedPostDate1 = {
    "product_id": prodictId1,
    "verifyed": "Y",
    "remark": "12"
}
