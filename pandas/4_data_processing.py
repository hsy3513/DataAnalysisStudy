import pandas as pd
import numpy as np

# * products.csv 파일 데이터 읽어오기
df = pd.read_csv('products.csv', index_col='id')

# 상위 5개 데이터 출력하기 => head()
# 하위 5개 => tail()
# print(df.head())

# print(f'index: {df.index}')
print(f'columns: {df.columns}')

# * 행/열 선택(인덱싱) 및 범위 선택(슬라이싱): loc iloc
#     loc(Label Location): 라벨 기반 선택
#       loc[행_선택, 열_선택]
#       - 행 선택: 인덱스 라벨(문자열, 숫자, 지정한 이름..)
#       - 열 선택: 컬럼 라벨(열 이름, 문자열, ...)
#       => 슬라이싱 시 끝 라벨을 포함!

#     iloc(Integer Location): 정수(위치) 기반 선택
#       iloc[행_선택, 열_선택]
#       - 행 선택: 0부터 시작하는 순서(위치)
#       - 열 선택: 0부터 시작하는 순서(위치)
#       => 위치 기반으로 기존 슬라이싱과 동일. 끝 위치(인덱스) 미포함(제외)

def practice_loc():
  print('* ==== 상품명만 조회(출력) ==== *')
  print(df['상품명'])   # 데이터 프레임에 []로 인덱싱 할 때는 컬럼을 기준으로 선택. 행x

  print('* ==== 113번 행의 데이터 조회 ==== *')
  print(df.loc[113])    # 행 인덱스로 접근하고자 할 경우 loc, iloc 사용
  
  print('* ==== 113번 행의 상품명 조회 ==== *')
  print(df.loc[113, '상품명'])

  print('* ==== 113번 행의 상품명, 가격 조회 ==== *')
  # print(df.loc[113, ['상품명', '가격']])  # 여러 개의 열을 리스트 형태로 전달
  print(df.loc[113, '상품명':'가격'])       # 슬라이싱 적용

  print('* ==== 110번 행의 상품명, 재고 조회 ==== *')
  # 리스트 방식
  print(df.loc[110, ['상품명', '재고']])

  # 슬라이싱 방식
  print(df.loc[110, '상품명'::2])

# practice_loc()

def practice_iloc():
  print('* ==== 첫번째 행의 전체 컬럼 조회 ==== *')
  print(df.iloc[0])
  # print(df.iloc[0, :])

  print("* ==== 첫번째 행의 마지막 컬럼 조회 ==== *")
  print(df.iloc[0, -1])   # => Scalar
  print(df.iloc[0, -1:])  # => Series

  print('* ==== 3 ~ 5번째 행의 모든 컬럼 조회 ==== *')
  print(df.iloc[2:5, :])

  print('* ==== 3 ~ 5번째 행의 두번째 컬럼 조회 ==== *')
  print(df.iloc[2:5, 1:2])

# practice_iloc()

'''
  데이터프레임(DataFrame)의 인덱스는 반드시 숫자가 아닐 수 있음.
  문자나 날짜 등 다양한 값이 라벨이 될 수 있음
  따라서, 위치(index)로 선택하는 것인지, 라벨(label)로 선택하는 것인지 모호해질 수 있음.

  이러한 혼란을 방지하고 의도를 명확하게 하기 위해
  판다스(Pandas)에서는 라벨 기반 선택은 loc, 위치 기반 선택은 iloc로 구분하여 기능 제공.
'''

# =============================================================

# * 새로운 컬럼 생성
#   df[추가할_컬럼명] = 저장할_데이터
def add_column_test():
  df_test = df.copy()
  
  df_test['TEST'] = '테스트 데이터'
  print(df_test.head(1))

  # 컬럼 삭제 => drop(columns=[삭제할컬럼])
  df_test = df_test.drop(columns=['TEST'])
  print(df_test.head(1))

# add_column_test()

def add_total_price():
  print('* ==== 총 금액 컬럼 추가 === *')
  # 총 금액 = 가격 * 재고
  df['총 금액'] = df['가격'] * df['재고']

  print(df.head())

  print('* ==== 재고 수량에 따른 상태 컬럼 추가 ==== *')
  # 재고 상태 => 재고가 130 미만이면 '부족', 그렇지 않으면 '충분'
  df['재고 상태'] = np.where(df['재고'] < 130, '부족', '충분')

  print(df.head())

  print('* ==== 재고 상태별 데이터 개수 조회 ==== *')
  print(df['재고 상태'].value_counts())

# add_total_price()

# =============================================================

# * 문자열 처리
def str_processing():
  # * 상품명 정보 조회
  print(df['상품명'])

  # 괄호가 포함된 상품의 정보 분리 ============

  # 1) 괄호를 기준으로 분리

  # df.str: 시리즈(컬럼) 내의 데이터가 문자열이거나 문자열 리스트일떄,
  #         문자열 자체에 접근 가능한 방법(특별한 통로)
  #         => 전체 데이터를 대상으로 문자열 처리 가능

  # str.split(구분자, n=분리횟수, expand=컬럼확장여부)
  #     * n: 구분자에 해당하는 부분이 여러개일 때 몇번 분리할 것인지
  #     * expand: False - 리스트 시리즈 형태로 반환(하나만 빠르게 추출할 때)
  #               True - 데이터프레임 형태로 반환(하나의 컬럼을 여러개의 독립된 컬럼으로 나눌 때. 일반적인 방식)

  # 구분자, 분리횟수 설정하여 분리
  #   '('
  split_df = df['상품명'].str.split('(', n=1)
  print(split_df)

  print(split_df.str[0])  # 첫번째 요소(메인 이름)만 추출

  print('-' * 30)

  # 구분자, 분리횟수, 컬럼확장 설정 분리
  split_df = df['상품명'].str.split('(', n=1, expand=True)
  # print(split_df)
  # print(split_df.columns)
  # print(split_df[0])  # 메인 이름
  # print(split_df[1])   # 용량/부가 정보. 없는 데이터 None

  # '메인 이름' 컬럼을 추가, 구분한 첫번째 데이터를 저장(공백 제거)
  # '용량' 컬럼을 추가, 구분한 두번째 데이터를 저장 (')'를 제거)
  df['메인 이름'] = split_df[0].str.strip()
  df['용량'] = split_df[1].str.replace(')', '')

  print('* ==== 메인이름, 용량 컬럼 추가 ==== *')
  print(df.head())

  print('* ==== 용량 데이터만 조회 ==== *')
  print(df['용량'])

  # 결측치 확인: isnull()
  #   -> 결측치: 유효하지 않은 값(수집x, ...)
  #       * NaN   : Not a Number. 수치형 데이터에서 주로 다룸
  #       * None  : Python 객쳬에서 "값이 없음"을 명시
  #       * Nat   : Not a Time. 날짜/ㅅ;간 데이터에서 사용

  # print(df['용량'].isnull())
  # 유효한 값을 확인 => isnull()의 결과를 부정
  #                     부정 연산자(~) 사용
  # print(~df['용량'].isnull())

  print(df[~df['용량'].isnull()])

  # * 유효한 값이 있는 지 확인: notna()
  #   - 유효한 값(결측치 x) : True
  #   - 결측치(NaN, Null)   : False
  print('* ==== notna() ==== *')
  print(df['용량'].notna())

  print(df[df['용량'].notna()])
  
str_processing()