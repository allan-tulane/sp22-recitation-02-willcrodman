from main import *

def test_simple_work():

  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 311
  assert simple_work_calc(30, 4, 2) == 1162

  assert simple_work_calc(20, 4, 2) == 1036
  assert simple_work_calc(40, 6, 2) == 43072
  assert simple_work_calc(60, 8, 2) == 246508

def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 529
  assert work_calc(30, 3, 2, lambda n: n) == 381

  assert work_calc(20, 4, 2,lambda n: 1) == 853
  assert work_calc(40, 2, 2, lambda n: n*n) == 3096
  assert work_calc(60, 6, 2, lambda n: n) == 45060
