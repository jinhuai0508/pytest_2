import os

import pytest
import yaml

from pythoncode.calaculator import Calculator

@pytest.fixture(scope='class')
def calc1():
    calc1 = Calculator()
    return calc1

yaml_file_path = os.path.dirname(__file__) + "/data.yml"
with open(yaml_file_path)as f:
    datas = yaml.safe_load(f)
    add_datas = datas["add"]
    sub_datas = datas["sub"]
    mul_datas = datas["mul"]
    divi_datas = datas["divi"]
    add_ids = datas["add_ids"]
    sub_ids = datas["sub_ids"]
    mul_ids = datas["mul_ids"]
    divi_ids = datas["divi_ids"]

@pytest.fixture(params=add_datas, ids=add_ids)
def get_add_datas(request):
    print("开始计算add")
    data = request.param
    yield data
    print("结束计算add")


@pytest.fixture(params=sub_datas, ids=sub_ids)
def get_sub_datas(request):
    print("开始计算sub")
    data = request.param
    yield data
    print("开始计算sub")

@pytest.fixture(params=mul_datas, ids=mul_ids)
def get_mul_datas(request):
    print("开始计算mul")
    data = request.param
    yield data
    print("开始计算mul")


@pytest.fixture(params=divi_datas, ids=divi_ids)
def get_divi_datas(request):
    print("开始计算divi")
    data = request.param
    yield data
    print("开始计算divi")
