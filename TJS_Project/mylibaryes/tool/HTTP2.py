# -*- coding: utf-8 -*
# import requests
# from PIL import Image
# from io import BytesIO
# def down_image():
#     img_src = "http://192.168.111.113:8090/safety/show/"
#     response = requests.get(img_src)
#     image = Image.open(BytesIO(response.content))
#     image.save('D:/test_image/yzm.png')
#
#
# def _get_dynamic_binary_image(filedir, img_name):
#     filename =   './out_img/' + img_name.split('.')[0] + '-binary.jpg'
#     img_name = filedir + '/' + img_name
#     print('.....' + img_name)
#     im = cv2.imread(img_name)
#     im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #灰值化
#     # 二值化
#     th1 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
#     cv2.imwrite(filename,th1)
#     return th1


def should_be_in(self, actualValue_list, *expectValue_list):  # 成标方法
    try:
        if actualValue_list in expectValue_list:
            return True
        else:
            return False

    except:

        raise IndexError()



arg = ['{"home_product": [{"loan_day": "365", "buy_min_amount": "100.00", "rate": "9.00", "tag": [], "interest_start_time": "1532448000", "id": "3465", "min_amount_desc": "起投金额", "term_desc": "计划期限", "remain_amount": "900.00", "current_time": "2018-10-15 09:33:49", "loan_type": "天", "loan_name": "365", "progress": {"disabled": 1, "value": 100, "desc": "募集结束"}, "rate_desc": "预期年化收益率", "status": "5", "status_desc": "募集结束", "interest_end_time": "1563984000", "buy_max_amount": "0.00", "total_amount": "1000.00", "name": "起投100，total1000", "url": "http://wap.tjs.com/tjs/webview/product_detail/3465?app=1", "step_amount": "10.00", "add_rate": "0", "buy_start_time": "2018-07-16 00:00:00"}, {"loan_day": "365", "buy_min_amount": "100.00", "rate": "9.00", "tag": [], "interest_start_time": "1535904000", "id": "3615", "min_amount_desc": "起投金额", "term_desc": "计划期限", "remain_amount": "397500.00", "current_time": "2018-10-15 09:33:49", "loan_type": "天", "loan_name": "365", "progress": {"disabled": 0, "value": 20.5, "desc": "募集中"}, "rate_desc": "预期年化收益率", "status": "2", "status_desc": "立即认购", "interest_end_time": "1567440000", "buy_max_amount": "0.00", "total_amount": "500000.00", "name": "autotesting99999", "url": "http://wap.tjs.com/tjs/webview/product_detail/3615?app=1", "step_amount": "100.00", "add_rate": "0", "buy_start_time": "2018-09-03 00:00:00"}, {"loan_day": "365", "buy_min_amount": "1000000.00", "rate": "6.88", "tag": [], "interest_start_time": "1531152000", "id": "3365", "min_amount_desc": "起投金额", "term_desc": "计划期限", "remain_amount": "44000000.00", "current_time": "2018-10-15 09:33:49", "loan_type": "天", "loan_name": "365", "progress": {"disabled": 1, "value": 100, "desc": "已截止"}, "rate_desc": "预期年化收益率", "status": "5", "status_desc": "已截止", "interest_end_time": "1562688000", "buy_max_amount": "0.00", "total_amount": "50000000.00", "name": "城建系列0711", "url": "http://wap.tjs.com/tjs/webview/product_detail/3365?app=1", "step_amount": "10000.00", "add_rate": "0", "buy_start_time": "2018-07-10 00:00:00"}], "tag_name": "推荐产品", "footer_url": "http://wap.tjs.com/tjs/webview/app_index?app=1", "news": {"more_url": "http://wap.tjs.com/tjs/webview/news_list?app=1", "list": [{"url": "http://wap.tjs.com/tjs/webview/news_view/44/2968?app=1", "title": "测试图片"}]}}']
arg2 = ['{"home_product": [{"loan_day": "365", "buy_min_amount": "100.00", "rate": "9.00", "tag": [], "interest_start_time": "1532448000", "id": "3465", "min_amount_desc": "起投金额", "term_desc": "计划期限", "remain_amount": "900.00", "current_time": "2018-10-15 09:33:49", "loan_type": "天", "loan_name": "365", "progress": {"disabled": 1, "value": 100, "desc": "募集结束"}, "rate_desc": "预期年化收益率", "status": "5", "status_desc": "募集结束", "interest_end_time": "1563984000", "buy_max_amount": "0.00", "total_amount": "1000.00", "name": "起投100，total1000", "url": "http://wap.tjs.com/tjs/webview/product_detail/3465?app=1", "step_amount": "10.00", "add_rate": "0", "buy_start_time": "2018-07-16 00:00:00"}, {"loan_day": "365", "buy_min_amount": "100.00", "rate": "9.00", "tag": [], "interest_start_time": "1535904000", "id": "3615", "min_amount_desc": "起投金额", "term_desc": "计划期限", "remain_amount": "397500.00", "current_time": "2018-10-15 09:33:49", "loan_type": "天", "loan_name": "365", "progress": {"disabled": 0, "value": 20.5, "desc": "募集中"}, "rate_desc": "预期年化收益率", "status": "2", "status_desc": "立即认购", "interest_end_time": "1567440000", "buy_max_amount": "0.00", "total_amount": "500000.00", "name": "autotesting99999", "url": "http://wap.tjs.com/tjs/webview/product_detail/3615?app=1", "step_amount": "100.00", "add_rate": "0", "buy_start_time": "2018-09-03 00:00:00"}, {"loan_day": "365", "buy_min_amount": "1000000.00", "rate": "6.88", "tag": [], "interest_start_time": "1531152000", "id": "3365", "min_amount_desc": "起投金额", "term_desc": "计划期限", "remain_amount": "44000000.00", "current_time": "2018-10-15 09:33:49", "loan_type": "天", "loan_name": "365", "progress": {"disabled": 1, "value": 100, "desc": "已截止"}, "rate_desc": "预期年化收益率", "status": "5", "status_desc": "已截止", "interest_end_time": "1562688000", "buy_max_amount": "0.00", "total_amount": "50000000.00", "name": "城建系列0711", "url": "http://wap.tjs.com/tjs/webview/product_detail/3365?app=1", "step_amount": "10000.00", "add_rate": "0", "buy_start_time": "2018-07-10 00:00:00"}], "tag_name": "推荐产品", "footer_url": "http://wap.tjs.com/tjs/webview/app_index?app=1", "news": {"more_url": "http://wap.tjs.com/tjs/webview/news_list?app=1", "list": [{"url": "http://wap.tjs.com/tjs/webview/news_view/44/2968?app=1", "title": "测试图片"}]}}']
print should_be_in(arg,arg2)
