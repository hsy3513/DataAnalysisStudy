import numpy as np

def practice_1d():
  # 1차원 배열 생성 -> [10, 20, 30, 40, 50, 60]
  arr = np.arange(10, 61, 10)

  print('---- 1D ----')
  print(arr)

  print()

  print('* indexing *')
  print('세번째 요소: ' + str(arr[2]))
  print('마지막 요소: ' + str(arr[-1]))

  print()

  print('* slicing *')
  print('2번째 요소부터 4번째 요소까지 추출: ' + str(arr[1:4]))
  print('앞의 3개 요소 추출: ' + str(arr[:3]))
  print('짝수번째 요소 추출: ' + str(arr[1::2]))
  print('역순으로 추출: ' + str(arr[::-1]))

# practice_1d()

def practice_2d():
  # 3행 4열 형태로 1 ~ 12까지 데이터를 담아 생성
  arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
  ])
  print(arr)

  # print('** arange.reshape 사용 **')
  # arr = np.arange(1, 13).reshape(3, 4)
  # print(arr)
  print()

  print('** indexing **')
  # print('배열에서 7을 출력: ' + str(arr[1][2]))
  print('배열에서 7을 출력: ' + str(arr[1, 2]))

  print()

  print('** slicing') # => [행 슬라이스, 열 슬라이스]
  print('배열에서 3, 4, 7, 8을 추출')
  print(arr[:2, 2:])  # 행: 첫번째부터 1번 인덱스까지 / 열: 2번부터 끝 인덱스까지
  print()
  print('배열에서 1, 2, 3, 4를 추출: ')
  print(arr[:1])
  print()
  print('배열에서 2, 6, 10을 추출: ')
  print(arr[:, 1:2])

# practice_2d()

def practice_3d():
  # 1 ~ 12 데이터를 저장하는 3차원 배열 (2x3 배열이 2개)
  arr = np.arange(1, 13).reshape(2, 2, 3)
  print(arr)

  print('** indexing **')
  print('데이터 중 6을 출력: ')
  print(arr[0, 1, 2])
  print()
  print('** slicing **')
  print(' 7 ~ 12 값을 추출: ')
  print(arr[1:,: ,:])
  # print(arr[1])
  print()
  print(' 1, 2, 3, 7, 8, 9 를 추출:')
  print(arr[:, :1, :])

# practice_3d()

def practice_boolean_indexing():
  # 1차원 배열 추출
  arr = np.array([10, 21, 30, 43, 50, 8])
  print(arr)

  # 30보다 큰 요소만 추출
  print(arr > 30)       # [False False False  True  True False]
  print(arr[arr > 30])  # 조건에 해당하는 요소로만 다시 배열 생성!

  # 2차원 배열 생성
  # * 10 ~ 90까지 총 9개의 데이터를 저장(3x3), 간격: 10
  arr = np.arange(10, 91, 10).reshape(3, 3)
  print(arr)
  print()
  # * 50 < x < 80 데이터만 추출
  print('50보다 큰 값만 추출::')
  print(arr[arr > 50])
  print()
  print('80보다 작은 값만 추출::')
  print(arr[arr < 80])
  print()
  print('50보다 크고 80보다 작은 값만 추출::')
  print(arr[(arr > 50) & (arr < 80)])

  # 최대값 추출: max()
  print(arr.max())
  print(arr[arr == arr.max()])


practice_boolean_indexing()
