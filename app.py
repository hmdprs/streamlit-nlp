import streamlit as st
import nlpiffy as nl
import classiffy as cl


def main():
    st.title("Streamlit Sample")

    catagory = st.sidebar.selectbox("Which Catagory?", ("NLP", "Classification"))
    if catagory == "NLP":
        nl.main()
    elif catagory == "Classification":
        cl.main()


if __name__ == "__main__":
    main()
