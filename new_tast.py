try:
    1/0
    print('沒出錯！')
except Exception as e:
    print('出錯了！')
    raise
