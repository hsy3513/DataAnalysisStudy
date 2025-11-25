'''
  넘파이(NumPy) 데이터 타입

  - 주요 타입
    * 정수형
      8비트 정수: int8 'i1'
      16비트 정수: int16 'i2'
      32비트 정수: int32 'i4'
      64비트 정수: int64 'i8'

    * 실수형
      32비트 실수: float32 'f4'
      64비트 실수: float64 'f8'

    * 복소수형
      64비트 복소수: complex64 'c8'
      128비트 복소수: complex128 'c16'

    * 논리형 : bool_ '?'

    * 문자열: str_ 'S' 'U'
      'S': 바이트 문자열(주로 ASCII)
      'U': 유니코드 문자열(한글, 다국어, ...)

  - astype(): 타입 변환
'''

import numpy as np

# --------------------------------- #
def print_info(arr):
  print(arr)

  if isinstance(arr, np.ndarray): # 자바에서 instance of 와 유사
    print(arr.dtype)
# --------------------------------- #

def dtype_int():
  data = [1, 2, 3]

  arr = np.array(data)
  print_info(arr) # int64 => 기본형

  # 배열 생성 시 타입을 지정하고자 할 경우
  #     array(data, dtype=지정할 타입)
  arr = np.array(data, dtype=int)
  print_info(arr) # 기본형으로 생성됨!(int64)

  arr = np.array(data, dtype=np.int32)
  print_info(arr)

  arr = np.array(data, dtype='i4')
  print_info(arr)

  # ---

  # arr = np.array([200, 300, 400], dtype=np.int8)
  # print_info(arr)
  # => 범위를 벗어나는 경우,
  #     실행 환경에 따라 OverflowError가 발생하거나
  #     wrap-around(순환) 될 수 있음!

# dtype_int()

def dtype_float():
  arr = np.array([1.5, 2.3, 3.6])
  print_info(arr) # 기본형 => float64

  data = [1, 2, 3, 4]
  arr = np.array(data, dtype=float)
  print_info(arr) # 기본형으로 생성됨!

  arr = np.array(data, dtype=np.float32)
  print_info(arr)

  arr = np.array(data, dtype='f4')
  print_info(arr)

# dtype_float()

def dtype_str():
  arr = np.array(['가', '나', '다'])
  print_info(arr)
  # <U1: 최대 길이가 1인 유니코드 문자열

  arr = np.array(['안농', '방가방가', 'ㅎ'])
  print_info(arr)
  # <U3: 최대길이 3
  
  arr = np.array(['a', 'b', 'c'])
  print_info(arr)
  # <U1: 일반적인 문자열은 유니코드 문자열이 기본형

  arr = np.array([b'a', b'b', b'c'])
  # 바이트 문자열 표현 시 b'---'와 같이 b 추가
  print_info(arr)
  #  |S1: 바이트 문자열, 최대길이 1

  arr = np.array(['a', 'b', 'c'], dtype='S')

# dtype_str()

def dtype_bool():
  arr = np.array([True, True, False])
  print_info(arr)

  # 숫자 데이터를 담아서, 타입을 불리언 지정
  arr = np.array([1, 0, 5], dtype=bool)
  print_info(arr)

  arr = np.array([-1, 5, 0], dtype=np.bool)
  print_info(arr)
  # 0 -> False, 양/음수 -> True

  # 문자 데이터를 담아서, 불리언 타입 지정
  arr = np.array(['abc', '', '-@#', '안농'], dtype=bool)
  print_info(arr)
  # '' -> False, 그 외에는 -> True

# dtype_bool()

def change_type():
  arr = np.array([1.3, 2.6, 6.5])
  print_info(arr)

  # astype(): 데이터 타입 변경
  #     변경할_대상_배열.astype(변경할_타입)

  # 실수 -> 정수
  arr2 = arr.astype(np.int32)
  print_info(arr2)

  # 실수 -> 정수 변환 시 소수점 이하가 버려짐(데이터 손실)
  arr2 = arr.astype('i4')
  print_info(arr2)

change_type()