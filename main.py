import streamlit as st
import pandas as pd

with st.echo():
    st.title("Getting Start streamlit")
    st.write("My first web introduction to streamlit")
    st.markdown("*Streamlit* is **really** ***cool***.")

    code = '''
        def hello():
        print("Hello, Streamlit!")
        '''

    run_btn = st.button("Run!")
    if run_btn:
        st.markdown("Button was has already clicked")
    show_btn = st.button("Show Code")
    if show_btn:
        st.code(code, language="python")

    cols = st.columns(2)
    with cols[0]:
        age_inp = st.number_input("Input you age")
        st.markdown(f"You age is {age_inp}")

    #st.markdown("# NLP Task")
    with cols[1]:
        text_inp = st.text_input("Input yupr text")
        word_tokenize = "|".join(text_inp.split())
        st.markdown(f"{word_tokenize}")

    df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
    )

    st.dataframe(df, use_container_width=True)


    df = pd.DataFrame({
            "first column": [1,2,3,4,5,6],
            "second column": [10,20,60,90,200,100]
    })

    st.dataframe(df)
    show_plot_btn = st.button("Show Chart")
    if show_plot_btn:
        st.line_chart(df,x='first column',y='second column')