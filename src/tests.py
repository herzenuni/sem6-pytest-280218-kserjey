import pytest
from hypothesis import given
import hypothesis.strategies as st
from main import create_dict

def test_default():
    keys = ['nick', 'goss']
    values = ['python', 'nodejs']
    expected = { 'nick': 'python', 'goss': 'nodejs' }

    assert create_dict(keys, values) == expected

def test_fill_none():
    keys = ['nick', 'goss', 'pasha']
    values = ['python', 'nodejs']
    expected = { 'nick': 'python', 'goss': 'nodejs', 'pasha': None }

    assert create_dict(keys, values) == expected

@given(st.lists(st.text()))
def test_skip_values(extra_values):
    keys = ['nick', 'goss']
    values = ['python', 'nodejs'] + extra_values
    expected = { 'nick': 'python', 'goss': 'nodejs' }

    assert create_dict(keys, values) == expected

@pytest.mark.parametrize('keys, values', [
    (['sergey'], 'react'),
    ('sergey', ['react'])
])
def test_check_types(keys, values):
    with pytest.raises(TypeError):
        create_dict(keys, values)
