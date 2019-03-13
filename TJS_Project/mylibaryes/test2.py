import requests,json

session = requests.Session()
host = "http://admin.tjs.com"

login_url = "http://admin.tjs.com/login.html"
login_post_data = {
    "phone": "18770027573",
    "password":"aa111111"
}
res = session.post(login_url, login_post_data)


# head_date = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate",
#         "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#         "Connection": "keep-alive",
#         "Content-Length": "635",
#         "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#         "Host": "admin.tjs.com",
#         "Origin": "http://admin.tjs.com",
#         "Referer": "http://admin.tjs.com/product/add.html",
#         "X-Requested-With": "XMLHttpRequest"
# }
# for item in head_date:
#     session.headers.setdefault(item, head_date[item])
creatr_url = "http://admin.tjs.com/server/product/edit.html"

create_post_date = {
    "product_model":"3",
    "category_id":"11",
    "type": "1",
    "name": "autotesting656",
    "user_id": "60c74e91-8995-477f-a4d1-b57829cbc720",
    "custodian_id": "60c74e91-8995-477f-a4d1-b57829cbc720",
    "trustee_id": "60c74e91-8995-477f-a4d1-b57829cbc720",
    "rate": "10",
    "total_amount": "100",
    "buy_min_amount": "100",
    "step_amount": "100",
    "interest_start_time": "2018-06-16",
    "interest_end_time": "2019-06-16",


    "interest_advance_time": "2019-06-16",
    "loan_day_advance": "365",
    "raise_proof_id": "15",
    "endpoint_status": "all",
    "channel_flag": "financial",
    "display_order": "1000",
    "record_service_fee": "2",
    "register_service_fee": "2",
    "trusteeship_service_fee": "2",
    "transfer_service_fee": "2",
    "cashing_service_fee": "2",
    "other_service_fee": "2",


    "loan_day": "365",
    "buy_user_limit": "10",
    "transfer_allow": "Y",
    "transfer_lock_day": "0",
    "interest_way": "1",
    "repayment": "E3",
    "contract_tpl_ids": "15",
    "buy_start_time": "2018-06-14 00:00",
    "buy_end_time": "2018-06-16 00:00",
    "raise_full_stop": "Y",
    "raising_flag": "Y",
    "raise_min_amount": "0"
}
ress = session.post(creatr_url, create_post_date)
print(ress.content.decode('UTF-8'))
