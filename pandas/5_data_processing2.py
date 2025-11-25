import pandas as pd
import numpy as np

# * json 파일에서 데이터 읽어오기: pd.read_json(파일명)

# * 고객 정보 데이터(users.json)를 읽어서 df_users 변수에 저장
df_users = pd.read_json('users.json')
# print(df_users.head(1))

# * 주문 정보 데이터(orders.json)를 읽어서 df_orders 변수에 저장
df_orders = pd.read_json('orders.json')
# print(df_orders.head(1))

# * 병합 * -----------------------------
# merge() : SQL의 JOIN과 동일하게 동작.
#           두 데이터 프레임을 특정 컬럼 기준으로 병합

# merge(Left_DataFrame, Right_DataFrame, Left_기준컬럼, Right_기준컬럼, 병합방식)
# - 병합 방식: inner, left, right, outer

def inner_join():
  df_merge = pd.merge(
    df_users, 
    df_orders, 
    left_on='user_id', 
    right_on='customer_id', 
    how='inner'
  )

  print('* ==== inner join ==== *')
  # print(df_merge)
  # => 양쪽 데이터프레임에 모두 존재하는 데이터만 병합
  #     - 104 고객은 주문 정보가 없어 제외
  #     - A-005 주문은 고객 정보가 없어 제외

  # * 고객번호, 이름, 주소, 주문번호, 제품명, 가격만 출력 =====*
  print(df_merge[['user_id', 'name', 'addr', 'order_id', 'item', 'amount']])

# inner_join()

def left_join():
  # 고객 정보와 주문 정보를 병합 -> 모든 고객 정보를 조회
  df_merge = pd.merge(
    df_users, 
    df_orders, 
    left_on='user_id', 
    right_on='customer_id', 
    how='left'
  )

  print('* === left join ==== *')
  print(df_merge)
  # => 주문 정보가 없는 고객의 주문 컬럼들은 모두 NaN으로 표시됨

  # np.nan 데이터 타입 조회
  print(type(np.nan))
  # => 병합 시 결측값(NaN) 발생하면서 데이터 타입이 변경됨(정수 -> 실수)

  # * 기존 데이터 타입을 유지하면서 결측값을 처리하고자 할 경우: convert_dtypes()
  df_convert = df_merge.convert_dtypes()
  print(df_convert)
  # => <NA> (Not Avaliable): Nullable 자료형.

  # * 컬럼들의 데이터 타입 조회
  print(df_convert.dtypes)


left_join()