# coding=utf-8
import imp
Http2=imp.load_source('Http_self','D:/RF/TJS_Project/mylibaryes/tool/Httpself.py')
key = {

    "url":"http://www.tjs.com/",
    "browser":"ff",
    "username":"18770053344",
    
    "username1":"1877002757888",
    "username2":"1877002757",
    "username3":"1",
    "username4":"",
       
    "password":"aa111111",
    
    "password1":"aa11111",
    "password2":"a",
    "password3":"",
    "password4":"aa111111111",
    
    "element1":"name=abtn",
    "element2":"xpath=html/body/div[1]/div[1]/div/div[2]/a[1]",
    "expected":u"187****3344"


}
create_product_args = {

    "CreatrUrl":"http://admin.tjs.com/server/product/edit.html",
    
        
        }

CreatePostDate = {

    "product_model": "3",
    "category_id": "11",
    "type": "1",
    "name": "autotesting",
    "user_id": "60c74e91-8995-477f-a4d1-b57829cbc720",
    "custodian_id": "",
    "trustee_id": "4b7591c9-013f-4609-82a0-393f3aeedf3f",
    "rate":"9",
    "total_amount": "500000",
    "buy_min_amount": "100",
    "step_amount": "100",
    "interest_start_time": "2018-09-03",
    "interest_end_time": "2019-09-03",
    "loan_day": "365",
    "interest_advance_time": "2019-09-03",
    "loan_day_advance": "0",
    "buy_user_limit": "10",
    "transfer_allow": "Y",
    "transfer_lock_day": "0",
    "interest_way": "1",
    "repayment": "E3",
    "contract_tpl_ids": "15",
    "raise_proof_id": "15",
    "endpoint_status": "all",
    "channel_flag": "financial",
    "display_order": "10000",
    "inherit_flag": "Y",
    "use_gift": "Y",
    "interest_discount": "N",
    "bottom_amount": "100",
    "buy_max_times": "0",
    "buy_max_day_total": "0",
    "buy_max_total": "0",
    "buy_max_amount": "0",
    "record_service_fee": "0",
    "register_service_fee": "0",
    "trusteeship_service_fee": "0",
    "transfer_service_fee": "0",
    "cashing_service_fee": "0",
    "other_service_fee": "0",
    "buy_start_time": "2018-09-03 00:00",
    "buy_end_time": "2018-12-05 00:00",
    "raise_full_stop": "Y",
    "raising_flag": "Y",
    "raise_min_amount": "0"
    }

CreatePostDate2 = {             #尾包测试数据

    "product_model": "3",
    "category_id": "11",
    "type": "1",
    "name": "autotesting",
    "user_id": "60c74e91-8995-477f-a4d1-b57829cbc720",
    "custodian_id": "",
    "trustee_id": "4b7591c9-013f-4609-82a0-393f3aeedf3f",
    "rate":"9",
    "total_amount": "560000",
    "buy_min_amount": "100000",
    "step_amount": "10000",
    "interest_start_time": "2018-09-03",
    "interest_end_time": "2019-09-03",
    "loan_day": "365",
    "interest_advance_time": "2019-09-03",
    "loan_day_advance": "0",
    "buy_user_limit": "10",
    "transfer_allow": "Y",
    "transfer_lock_day": "0",
    "interest_way": "1",
    "repayment": "E3",
    "contract_tpl_ids": "15",
    "raise_proof_id": "15",
    "endpoint_status": "all",
    "channel_flag": "financial",
    "display_order": "10000",
    "inherit_flag": "Y",
    "use_gift": "Y",
    "interest_discount": "N",
    "bottom_amount": "100",
    "buy_max_times": "0",
    "buy_max_day_total": "0",
    "buy_max_total": "0",
    "buy_max_amount": "0",
    "record_service_fee": "0",
    "register_service_fee": "0",
    "trusteeship_service_fee": "0",
    "transfer_service_fee": "0",
    "cashing_service_fee": "0",
    "other_service_fee": "0",
    "buy_start_time": "2018-09-03 00:00",
    "buy_end_time": "2018-12-05 00:00",
    "raise_full_stop": "Y",
    "raising_flag": "Y",
    "raise_min_amount": "0"

}

CreatePostDate3 = {

    "product_model": "3",
    "category_id": "11",
    "type": "1",
    "name": "城建系列1",
    "user_id": "60c74e91-8995-477f-a4d1-b57829cbc720",
    "custodian_id": "",
    "trustee_id": "4b7591c9-013f-4609-82a0-393f3aeedf3f",
    "rate":"9",
    "total_amount": "500000",
    "buy_min_amount": "100",
    "step_amount": "100000",
    "interest_start_time": "2018-09-03",
    "interest_end_time": "2019-09-03",
    "loan_day": "365",
    "interest_advance_time": "2019-09-03",
    "loan_day_advance": "0",
    "buy_user_limit": "10",
    "transfer_allow": "Y",
    "transfer_lock_day": "0",
    "interest_way": "1",
    "repayment": "E3",
    "contract_tpl_ids": "15",
    "raise_proof_id": "15",
    "endpoint_status": "all",
    "channel_flag": "financial",
    "display_order": "10000",
    "inherit_flag": "Y",
    "use_gift": "Y",
    "interest_discount": "N",
    "bottom_amount": "100",
    "buy_max_times": "0",
    "buy_max_day_total": "0",
    "buy_max_total": "0",
    "buy_max_amount": "0",
    "record_service_fee": "0",
    "register_service_fee": "0",
    "trusteeship_service_fee": "0",
    "transfer_service_fee": "0",
    "cashing_service_fee": "0",
    "other_service_fee": "0",
    "buy_start_time": "2018-09-03 00:00",
    "buy_end_time": "2018-12-05 00:00",
    "raise_full_stop": "Y",
    "raising_flag": "Y",
    "raise_min_amount": "0"
    }

CreatePostDate4 = {

    "product_model": "3",
    "category_id": "12",
    "type": "1",
    "name": "城建系列2",
    "user_id": "60c74e91-8995-477f-a4d1-b57829cbc720",
    "custodian_id": "",
    "trustee_id": "4b7591c9-013f-4609-82a0-393f3aeedf3f",
    "rate":"9",
    "total_amount": "500000",
    "buy_min_amount": "100",
    "step_amount": "100000",
    "interest_start_time": "2018-09-03",
    "interest_end_time": "2019-09-03",
    "loan_day": "365",
    "interest_advance_time": "2019-09-03",
    "loan_day_advance": "0",
    "buy_user_limit": "10",
    "transfer_allow": "Y",
    "transfer_lock_day": "0",
    "interest_way": "1",
    "repayment": "E3",
    "contract_tpl_ids": "15",
    "raise_proof_id": "15",
    "endpoint_status": "all",
    "channel_flag": "financial",
    "display_order": "10000",
    "inherit_flag": "Y",
    "use_gift": "Y",
    "interest_discount": "N",
    "bottom_amount": "100",
    "buy_max_times": "0",
    "buy_max_day_total": "0",
    "buy_max_total": "0",
    "buy_max_amount": "0",
    "record_service_fee": "0",
    "register_service_fee": "0",
    "trusteeship_service_fee": "0",
    "transfer_service_fee": "0",
    "cashing_service_fee": "0",
    "other_service_fee": "0",
    "buy_start_time": "2018-09-03 00:00",
    "buy_end_time": "2018-12-05 00:00",
    "raise_full_stop": "Y",
    "raising_flag": "Y",
    "raise_min_amount": "0"
    }

CreatePostDate5 = {

    "product_model": "3",
    "category_id": "11",
    "type": "1",
    "name": "城建系列3",
    "user_id": "60c74e91-8995-477f-a4d1-b57829cbc720",
    "custodian_id": "",
    "trustee_id": "4b7591c9-013f-4609-82a0-393f3aeedf3f",
    "rate":"9",
    "total_amount": "500000",
    "buy_min_amount": "100",
    "step_amount": "100000",
    "interest_start_time": "2018-09-03",
    "interest_end_time": "2019-09-03",
    "loan_day": "365",
    "interest_advance_time": "2019-09-03",
    "loan_day_advance": "0",
    "buy_user_limit": "10",
    "transfer_allow": "Y",
    "transfer_lock_day": "0",
    "interest_way": "1",
    "repayment": "E3",
    "contract_tpl_ids": "15",
    "raise_proof_id": "15",
    "endpoint_status": "all",
    "channel_flag": "financial",
    "display_order": "10000",
    "inherit_flag": "Y",
    "use_gift": "Y",
    "interest_discount": "N",
    "bottom_amount": "100",
    "buy_max_times": "0",
    "buy_max_day_total": "0",
    "buy_max_total": "0",
    "buy_max_amount": "0",
    "record_service_fee": "0",
    "register_service_fee": "0",
    "trusteeship_service_fee": "0",
    "transfer_service_fee": "0",
    "cashing_service_fee": "0",
    "other_service_fee": "0",
    "buy_start_time": "2018-09-03 00:00",
    "buy_end_time": "2018-12-05 00:00",
    "raise_full_stop": "Y",
    "raising_flag": "Y",
    "raise_min_amount": "0"
    }

TiXianArg = {
    "passward1":"aa11111111",
    "passward2":"aa11",
    "passward3":"",
    "passward4":"aa111111"
}

SelectSql = {
    "Sql":"select code from  n_valid ORDER BY add_time  DESC  limit  1",
    "Passward":"aa111111",
    "username":u"自动",
    "idcard":"440513198108264567",
    "pre_mobile":"18922319914",
    "bank_card":"6214835893152205",


}


