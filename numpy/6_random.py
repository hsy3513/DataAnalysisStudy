'''
  난수(랜덤값), 분포 생성

  - np.random.seed        : 난수 시드 설정
  - np.random.randint     : 정수 난수 생성
  - np.random.normal      : 실수 난수 생성
  - np.random.rand/randn  : 0 ~ 1 사이 난수 생성
'''
import numpy as np

def set_seed():
  '''
    시드 설정: 시들르 고정하면 이후에 코드를 실행해도 동일한 난수가 생성됨
    => 재현성 확보를 위함
  '''
  np.random.seed(42)

# set_seed()

def random_int():
  '''
    균일 분포(Uniform Distribution)
      : 모든 값이 동일한 확률로 무작위하게 나옴 (주사위)
      : np.random.randint(최소값, 최대값, size=개수)
  '''

  # 0 이상 10 미만의 정수 난수 5개 생성
  random = np.random.randint(0, 10, size=5)
  print(random)

  # 2차원 배열 생성
  random_2d = np.random.randint(-10, 10, size=(2, 4))
  print(random_2d)

  # 3차원 배열 생성
  random_3d = np.random.randint(1, 101, size=(3, 2, 2))
  print(random_3d)
  
# random_int()

def normal_dist():
  '''
    정규 분포(Normal Distribution)
    : 자연 현상(키, 몸무게, 시험 점수)에서 가장 흔하게 나타나는 분포
    : 평균을 중심으로 데이터가 모이고, 양 끝으로 갈 수록 희박해지는 모양의 그래프를 띔

    표준 편차(Standard Deviation)
    : 데이터가 평균으로부터 얼마나 떨어져 있는 지(퍼져있는 지)를 나타내는 값
    : 표준 편차가 작을 수록 데이터는 평균 주변에 좁게 모여 있음

    np.random.normal(loc=평균, scale=표준편차, size=개수)
  '''

  # 평균이 173, 표준편차 5, 데이터 10개 생성
  data = np.random.normal(loc=173, scale=5, size=10)
  print(data)

  # 생성된 데이터의 평균
  print(f'- 평균: {data.mean():.2f}')

  # 생성된 데이터의 표준편차
  print(f'- 표준편차: {data.std():.2f}')


# normal_dist()

def uniform_and_std_normal():
  # np.random.rand(개수): 0.0 이상 1.0 미만의 균일 분포 난수(개수만큼)
  
  # 난수를 10개 생성
  arr = np.random.rand(10)
  print(arr)

  # * 표준 편차 분포 : 정규 분포의 특별한 형태로 항상 평균=0, 표준편차=1인 경우
  arr = np.random.randn(5)
  print(arr)
  print(f'평균: {arr.mean()}')
  print(f'표준편차: {arr.std()}')

uniform_and_std_normal()