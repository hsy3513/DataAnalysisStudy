'''
  넘파이 배열 검색, 정렬
  
  - where: 조건에 맞는 요소의 인덱스 반환 / 값 치환
  - argmax / argmin: 최대값/최소값이 있는 인덱스를 반환
  - sort : 배열을 정렬
'''
import numpy as np

def search_and_replace():
  arr = np.array([10, 5, 22, 15, 8, 30])
  print(arr)

  # 15보다 큰 요소 찾기
  idx_info = np.where(arr > 15)
  print(idx_info)
  print(arr[idx_info])
  # np.where(조건) => 조건에 해당하는 인덱스 반환

  # 10보다 큰 요소는 99로 변경
  # 아닌 요소는 0으로 변경(치환)
  rpc_arr = np.where(arr > 10, 99, 0)
  print(rpc_arr)
  # np.where(조건, 조건O 시 치환 값, 조건X 시 치환 값)
  # => 조건에 따라 변경된 값으로 구성된 배열 반환

# search_and_replace()

def max_min_index():
  arr = np.array([[10, 20, 5], [33, 15, 40]])
  print(arr)

  # argmax(): 최대값의 인덱스 반환
  # argmin(): 최소값의 인덱스 반환
  print(f'최대값 인덱스: {np.argmax(arr)}')
  print(f'최소값 인덱스: {np.argmin(arr)}')

  print(arr.flatten())
  # => 1차원 배열로 평탄화된 기준으로 인덱스를 반환

  # 축(axis) 기준으로 조회
  # - 열 기준으로 최대값 인덱스: axis=0
  print(f'열 기준 최대 인덱스: {np.argmax(arr, axis=0)}') # => 행의 인덱스 반환
  print(f'행 기준 최대 인덱스: {np.argmax(arr, axis=1)}') # => 열의 인덱스 반환

# max_min_index()

def array_sortig():
  arr = np.array([4, 1, 2, 5, 3])

  # np.sort(): 원본 배열을 변경하지 않고, 정렬된 새로운 배열을 반환
  sorted_arr = np.sort(arr)
  print(f'정렬된 배열: {sorted_arr}') # => 오름차순
  print(f'기존 배열: {arr}')

  # 내림차순 정렬
  # 1) 오름차순 정렬 후 역순으로 배치(슬라이싱)
  desc_arr = sorted_arr[::-1]
  print(f'역정렬된 배열: {desc_arr}') # => 오름차순

  # 원본 배열을 정렬하고자 할 때: 배열.sort()
  arr.sort()
  print(f'정렬된 기존 배열: {arr}')

array_sortig()