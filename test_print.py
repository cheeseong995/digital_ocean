# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:57:33 2023

@author: CheeSeong
"""

try:
  from function_script import add_2_numbers

  theSum = add_2_numbers(2,5)
  print(f'The sum is {theSum}')
except Exception as e:
  print(e)
