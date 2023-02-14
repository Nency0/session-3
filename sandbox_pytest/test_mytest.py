#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mytest import square

import pytest
@pytest.fixture

def input_value():
    return 4

def test_square_correct_value(input_value):
    subject=square(input_value)
    assert subject==16


# In[ ]:




