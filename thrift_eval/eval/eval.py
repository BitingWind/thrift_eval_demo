# encoding: utf-8

import json
import re
import thriftpy2
from typing import List

# Get the Object define
demo_thrift = thriftpy2.load("../idl/demo.thrift", module_name="demo_thrift")
ARequest = demo_thrift.ARequest

base_thrift = thriftpy2.load("../idl/base.thrift", module_name="base_thrift")
Base = base_thrift.Base

def load_file_to_request() -> List[ARequest] :
    with open("../log/elk_log.json", "r") as es_json_res:
        load_rst = json.load(es_json_res)
        log_msg_list = [hit["_source"]["log_msg"] for hit in load_rst["hits"]["hits"]]
        request_list = []
        for log_msg in log_msg_list:
            try:
                a_request = re.findall("params: \((.+?),\)$", log_msg)[0]
                # eval the str to object
                req = eval(a_request)
                request_list.append(req)
            except Exception:
                continue
        return request_list

if __name__ == "__main__":
    a_list = load_file_to_request()
    a = a_list[0]
    print(a.a1)



