import tabulate
import time

def simple_work_calc(n, a, b):
  if n == 1:
    return a * 1 - n
  else:
    return a * simple_work_calc((n // b), a, b) + n

def test_simple_work():

  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 311
  assert simple_work_calc(30, 4, 2) == 1162

  assert simple_work_calc(20, 4, 2) == 1036
  assert simple_work_calc(40, 6, 2) == 43072
  assert simple_work_calc(60, 8, 2) == 246508

def work_calc(n, a, b, f):
  if n == 1:
    return a * 1 - f(n)
  else:
    return a * work_calc((n // b), a, b, f) + f(n)

def span_calc(n, a, b, f):
  if n == 1:
    return a * 1 - f(n)
  else:
    return work_calc((n // b), a, b, f) // a + f(n)

def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 529
  assert work_calc(30, 3, 2, lambda n: n) == 381

  assert work_calc(20, 4, 2,lambda n: 1) == 853
  assert work_calc(40, 2, 2, lambda n: n*n) == 3096
  assert work_calc(60, 6, 2, lambda n: n) == 45060

### COMPARE_WORK MODIFICAION IMPLMENTED IN TEST_COMPARE_WORK ###
def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):

	result = []
	for n in sizes:
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():

  f1 = lambda n: work_calc(n, 3, 2, lambda n: 1)
  fn = lambda n: work_calc(n, 3, 2, lambda n: n)
  fnn = lambda n: work_calc(n, 3, 2, lambda n: n*n)

  print("\n W(n) where f(n)=1 is compared to f(n)=n")
  res = compare_work(f1, fn)
  print_results(res)

  print("\n W(n) where f(n)=1 is compared to f(n)=n^2")
  res = compare_work(f1, fnn)
  print_results(res)

  print("\n W(n) where f(n)=n is compared to f(n)=n^2")
  res = compare_work(fn, fnn)
  print_results(res)

def print_results_span(results):
	print(tabulate.tabulate(results,
							headers=['1', '2', '4', '8', '16'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_span():
    n_list = list()
    for n in [10, 20, 50, 100, 1000, 5000, 10000]:
        p_list = [n]
        for processor in [1, 2, 4, 8, 16]:
            s = span_calc(n, processor, 2, lambda n: n)
            p_list.append(s)
        n_list.append(p_list)
    print_results_span(n_list)
  