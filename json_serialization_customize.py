#!/usr/bin/python
# coding: utf-8

import time
import json

# 序列化
def to_json(python_object):
    # 处理time对象
    if isinstance(python_object, time.struct_time):
        return {
            "__class__": "time.asctime",
            "__value__": time.asctime(python_object)
        }
    # 处理bytes对象
    if isinstance(python_object, bytes):
        return {
            "__class__": "bytes",
            "__value__": python_object.decode()
        }
    # 默认返回值
    raise TypeError("{} is not JSON serializable.".format(repr(python_object)))

# json.dump(entry, ifs, default=to_json)

# 反序列化
def from_json(json_object):
    # 与to_json中的设置相应
    if "__class__" in json_object:
        # time对象
        if json_object['__class__'] == "time.asctime":
            return time.strptime(json_object['__value__'])
        # bytes对象
        if json_object['__class__'] == "bytes":
            return bytes(json_object['__value__'], encoding='utf-8')
    return json_object

# entry = json.load(ifs, object_hook=from_json)

if __name__ == '__main__':
    entry = {
        "title": "测试对象",
        "content": b"Guess what this program is capabable of?",
        "date": time.localtime()
    }

    print("Serializtion:\n")
    entry2 = json.dumps(entry, default=to_json)
    print(entry2)
    print("\n" * 2)
    print("Deserialization:\n")
    print(json.loads(entry2, object_hook=from_json))
    