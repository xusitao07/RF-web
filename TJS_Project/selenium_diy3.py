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

establishUrl = {
    "establishUrl":"http://admin.tjs.com/server/product/establish.html"
}
Sql2 = "SELECT id FROM n_product WHERE NAME = 'autotesting'"
pc = Do()
establisID = pc.do_dql(Sql2)
print establisID
establishPostDate = {
    "id": establisID,
    "raise_flag": "Y",
}
