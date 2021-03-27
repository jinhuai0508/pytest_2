import os
import pytest
import yaml

from pythoncode.calaculator import Calculator


class TestCalc:

    @pytest.mark.run(order=1)
    def test_add(self, calc1, get_add_datas):
        result = calc1.add(get_add_datas[0], get_add_datas[1])
        assert result == get_add_datas[2]

    @pytest.mark.run(order=4)
    def test_div(self, calc1, get_divi_datas):
        result = calc1.div(get_divi_datas[0], get_divi_datas[1])
        assert result == get_divi_datas[2]

    @pytest.mark.run(order=2)
    def test_sub(self, calc1, get_sub_datas):
        result = calc1.sub(get_sub_datas[0], get_sub_datas[1])
        assert result == get_sub_datas[2]

    @pytest.mark.run(order=3)
    def test_mul(self, calc1, get_mul_datas):
        result = calc1.mul(get_mul_datas[0], get_mul_datas[1])
        assert result == get_mul_datas[2]
