# pip install finance-datareader streamlit
import FinanceDataReader as fdr
import streamlit as st
import datetime

st.title("스타벅스 주식 차트 및 데이터 조회")

date = st.date_input("조회 시작일 선택", datetime.datetime(2024, 1, 1))

code = st.text_input('종목코드', value='SBUX', placeholder='예: SBUX (Starbucks)')

if code and date:
    try:
        df = fdr.DataReader(code, date)
        data = df.sort_index(ascending=True).loc[:, 'Close']
        
        tab1, tab2 = st.tabs(['차트', '데이터'])

        with tab1:
            st.line_chart(data)

        with tab2:
            st.dataframe(df.sort_index(ascending=False))

        with st.expander('컬럼 설명'):
            st.markdown('''
            - Open : 시가  
            - High : 고가  
            - Low  : 저가  
            - Close : 종가  
            - Adj Close : 수정 종가  
            - Volume : 거래량  
            ''')
    except Exception as e:
        st.error(f"데이터 불러오기 실패: {e}")