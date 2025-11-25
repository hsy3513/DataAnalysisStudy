'''
  벡터화 연산(Vectorization)

  - 반복문(for) 없이 배열 전체에 연산을 적용하는 기술
  - 속도 향상, 코드가 간결해짐!
'''
import numpy as np
import time

def basic():
  arr1 = np.arange(1, 4)
  arr2 = np.arange(4, 7)
  
  # arr1 + arr2 결과
  print(f'arr1 + arr2: {arr1 + arr2}')

  # arr1 * arr2 결과
  print(f'arr1 * arr2: {arr1 * arr2}')

  result = arr1 > 2
  print(result)

basic()

def time_check():
  # 100만 개의 요소 생성
  arr = np.random.rand(1_000_000)

  # 벡터화 연산
  start1 = time.time()    # 유닉스 시간(Unix Time)형식 숫자
  result1 = arr * 2 + 5
  end1 = time.time()

  vec_time = end1 - start1

  # 반복문 연산
  start2 = time.time()    # 유닉스 시간(Unix Time)형식 숫자
  result2 = []
  for e in arr:
    result2.append(e * 2 + 5)
  end2 = time.time()

  loop_time = end2 - start2

  print(f'데이터 개수: {arr.size}')
  print(f'벡터화 연산 수행 시간: {vec_time:.6f}s')
  print(f'반복문 연산 수행 시간: {loop_time:.6f}s')
  print(f'{loop_time / vec_time:.1f}배 차이!')

# time_check()
