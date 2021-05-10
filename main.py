import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image #画像用
import time

st.title("streamlit 入門")
# st.write("DataFrame")
# st.write("Display Image") #画像表示
st.write("プレグレスバー表示")
"start"
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f"Iteration {i+1}")
  bar.progress(i+1)
  time.sleep(0.01)

left_column,right_column = st.beta_columns(2) #左右の２カラムに割れる
button = left_column.button("右カラムに文字表示")
if button:
  # right_column.write("ここは右")
  expander1 = st.beta_expander("問い合わせ1")
  expander1.write("書く1")
  expander2 = st.beta_expander("問い合わせ2")
  expander2.write("書く2")


text = st.text_input("あなたの趣味を教えて")
"あなたの趣味",text
condition = st.slider("あなたの今の調子",0,100,50)
"コンディション",condition

#セレクトボックス インタラクティブ
# option = st.selectbox(
#   "あなたが好きな数字を教えて",
#   list(range(1,11))
# )
# "あなたの好きな数字は",option,"です"

#if チェックされていれば画像表示。インタラクティブな動作
#相互動作とか動的とかそういう意味
# if st.checkbox("Show Image"): 
#   img = Image.open("innu.jpeg")
#   st.image(img,caption="innu",use_column_width=True)

# df = pd.DataFrame(
  # "１列目":[1,2,3,4],
  # "２列目":[10,20,30,40]

  # np.random.rand(20,3),
  # columns=["a","b","c"]

  # np.random.rand(100,2)/[50,50]+[35.69,139.70], #座標打ち込み
  # columns=["lat","lon"]
# )

# st.line_chart(df) #チャート表示
# st.area_chart(df)

# st.map(df) #座標をもとにマップ表示

# st.write(df)
# st.dataframe(df,width=200,height=400) #表の縦横を設定できる
# st.dataframe(df.style.highlight_max(axis=0)) #ハイライトをつける
# st.table(df.style.highlight_max(axis=0)) #tableはstatic(静的)なテーブル

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import pandas as pd
# import numpy as np
# ```
# """

