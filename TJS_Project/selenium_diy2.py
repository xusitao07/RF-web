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
Sql = "SELECT id FROM n_product WHERE NAME = 'autotesting'"
Sql1 = "SELECT id FROM n_product WHERE NAME = '城建系列1'"
Sql2 = "SELECT id FROM n_product WHERE NAME = '城建系列2'"
Sql3 = "SELECT id FROM n_product WHERE NAME = '城建系列3'"
pc = Do()
prodictId = pc.do_dql(Sql)
ReviewedPostDate = {
    "product_id": prodictId,
    "verifyed": "Y",
    "remark": "12"
}

pc1 = Do()
prodictId1 = 0
prodictId1 = pc1.do_dql(Sql1)
ReviewedPostDate1 = {
    "product_id": prodictId1,
    "verifyed": "Y",
    "remark": "12"
}
pc2 = Do()
prodictId2 = 0
prodictId2 = pc2.do_dql(Sql2)
ReviewedPostDate2 = {
    "product_id": prodictId2,
    "verifyed": "Y",
    "remark": "12"
}

pc3 = Do()
prodictId3 = 0
prodictId3 = pc3.do_dql(Sql3)
ReviewedPostDate3 = {
    "product_id": prodictId3,
    "verifyed": "Y",
    "remark": "12"
}
# establishUrl = {
#     "establishUrl":"http://admin.tjs.com/server/product/establish.html"
# }
# Sql2 = "SELECT id FROM n_product WHERE NAME = 'autotesting'"
# establisID = pc.do_dql(Sql2)
# print establisID
# establishPostDate = {
#     "id": establisID,
#     "raise_flag": "Y",
# }