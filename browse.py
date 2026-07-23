import streamlit as st
import sqlite3
import pandas as pd

def main():
    st.title("Graphically Music")
    st.header("Browse")
    items = cache_data()
    all_items, brands, filter_list = st.tabs(["All", "Brands", "Filter"])

    with all_items:
        display_all_items(items)




def display_all_items(items):

@st.cache_resource
def db_connection():
    try:
        with sqlite3.connect("file:Audio.db?mode=ro", uri=True, check_same_thread=False) as connection:
            st.toast()
            return connection
    except sqlite3.OperationalError:




@st.cache_data
def load_iem_data(query, _conn):
    return pd.read_sql_query(query, _conn)

if __name__ == "__main__":
    main()