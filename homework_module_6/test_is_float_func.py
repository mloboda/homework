import pytest
import sys

sys.path.append('D:\ma_python\homework\homework_module_6\my\module')
from funcs import is_float

values_1 = [100, 0, -1, +10.333, -10.333, '0', 10.]
values_2 = ['python', 'PYTHON', '!@#$']
values_3 = [(TypeError, [1]), (TypeError, (1,)), (TypeError, ()), (TypeError, {1}), (TypeError, {'1': 1})]


@pytest.mark.parametrize('test_value', values_1)
def test_is_float_true(test_value):
    assert is_float(test_value)


@pytest.mark.parametrize('test_value', values_2)
def test_is_float_false(test_value):
    assert not is_float(test_value)


@pytest.mark.parametrize('excepted_exception, test_value', values_3)
def test_type_error(excepted_exception, test_value):
    with pytest.raises(excepted_exception):
        is_float(test_value)
