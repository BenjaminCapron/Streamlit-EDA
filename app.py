#Framework
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid import GridUpdateMode, DataReturnMode
from streamlit_pandas_profiling import st_profile_report

#Data analysis
import pandas as pd
import pandas_profiling
import openpyxl

#Navbar
import hydralit_components as hc

#Global Config
st.set_page_config(
    page_title="Arcane Analytics",
    page_icon="\U0001F300",
    layout="wide",
    initial_sidebar_state="expanded",
)

#Anti-Streamlit trademark
hide_streamlit_style = """
	<style>
	#MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
	</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#st.sidebar
with st.sidebar:
    st.title("DATA INPUT")
    uploaded_file = st.file_uploader(
        "Upload a .csv/.xlsx/.xls file below",
        key="1",
    )

    if uploaded_file is not None:
        if uploaded_file.name[-4:]==".csv":
            shows = pd.read_csv(uploaded_file, sep=None)
            file_format='csv'
        elif (uploaded_file.name[-4:]=="xlsx" or uploaded_file.name[-4:]==".xls" or uploaded_file.name[-4:]=="xlsm" or uploaded_file.name[-4:]=="xlsb"):
            shows = pd.read_excel(uploaded_file)
            file_format='excel'
        else:
            st.error("Uploaded file format is wrong.")
            file_format=None
    else:
        st.info(
            f"""
                👆 Sample to try : [train.csv](https://storage.googleapis.com/tf-datasets/titanic/train.csv)
                """
        )

    
#Navbar Content
menu_data = [
    {'label':"\U0001F300 Arcane Analytics"},
    {'label':"\U0001F4CA Data Analysis"},
    {'label':"\U0001F5A5 AI Prediction"},
    {'label':"\U0001F310 Data Enrichment"},
]

over_theme = {'txc_active': '#a61234'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)

#TAB 1 : Arcane Analytics
if menu_id=="\U0001F300 Arcane Analytics":
    st.title("\U0001F300 Arcane Analytics")
    st.markdown("**Author :** Benjamin CAPRON  |  **Email :** mailto:arcane.analytics.contact@gmail.com | **Version :** 1.0.0")
    st.markdown("**Arcane Analytics** provides automatic **Data Analysis**, **AI Prediction** (with machine learning) and **Data Enrichment** (with scraping/API). Access those features with the top navigation bar.")
    if (uploaded_file is not None and file_format!=None):
        st.success("File successfully uploaded. See below the data it contains.")
        if file_format=='csv':
            gb = GridOptionsBuilder.from_dataframe(shows)
            gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
            #gb.configure_selection(selection_mode="multiple", use_checkbox=True)
            gb.configure_side_bar()
            gridOptions = gb.build()

            response = AgGrid(
                shows,
                gridOptions=gridOptions,
                enable_enterprise_modules=True,
                update_mode=GridUpdateMode.MODEL_CHANGED,
                data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
                fit_columns_on_grid_load=False,
            )
        if file_format=='excel':
            st.table(shows)
    else:
        st.warning(
        f"""
            Upload a .csv/.xlsx/.xls file in the sidebar to analyse the data it contains ! You can also try it out with the sample provided.
            """
        )

#TAB 2 : Data Analysis
if menu_id=="\U0001F4CA Data Analysis":
    st.title("\U0001F4CA Data Analysis")
    if (uploaded_file is not None and file_format!=None):
        st.success(f"Dataset provided : **{uploaded_file.name}**, click on the button below to generate a complete analysis of your data")
        generate_report = st.button("Generate Report")
        if generate_report:
            pr = shows.profile_report()
            st_profile_report(pr)
    else:
        st.warning("You need to provide data before starting its analysis. You can upload a .csv/.xlsx/.xls file in the sidebar.")
        
#TAB 3 : Data Analysis
if menu_id=="\U0001F5A5 AI Prediction":
    st.title("\U0001F5A5 AI Prediction")
    if (uploaded_file is not None and file_format!=None):
        st.success(f"Dataset provided : **{uploaded_file.name}**, click on the button below to generate an AI Prediction based on your data")
        generate_report = st.button("Generate AI Prediction")
        if generate_report:
            pass
            #DO SOME
    else:
        st.warning("You need to provide data before applying AI Prediction. You can upload a .csv/.xlsx/.xls file in the sidebar.")
      
