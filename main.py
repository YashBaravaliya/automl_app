import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import io
import seaborn as sns
import warnings
from streamlit_option_menu import option_menu
from config import *


# warnings.simplefilter("ignore", UserWarning)


# if 'cleaned_data' not in st.session_state:
#     st.session_state['cleaned_data'] = None
# initialize_data()

def main():

    st.set_option('deprecation.showPyplotGlobalUse', False)

    selected = option_menu(
        menu_title = "AutoMll: Instant Machine Learning",
        options = ['Explore_Data','Feature_Enginerring','Regression','Classification','Clustering'],
        orientation="horizontal",
        icons=['cloud-upload-fill','clipboard-data-fill','bar-chart-line-fill','collection-fill','vr'],
        menu_icon='pie-chart-fill',
    )

    

    # upload_file_ = st.file_uploader("Upload a CSV file 📂", type=["csv"])

    # if upload_file_ is not None:
    #     data = pd.read_csv(upload_file_)
    #     cleaned_data = data.copy()

    #     # Save the cleaned data in session state
    #     update_data(data,cleaned_data)
        # data = shared_data[data]
        # cleaned_data = shared_data[cleaned_data]
        # st.session_state["cleaned_data"] = cleaned_data
        # st.session_state["data"] = data
        # st.session_state["file_name"] = upload_file_.name
    # Function to perform some exploratory data analysis


    if selected == 'Explore_Data':
        upload()

    elif selected == 'Feature_Enginerring':
        fe()

    elif selected == 'Regression':
        regression()

    elif selected == 'Classification':
        classification()

    elif selected == 'Clustering':
        clustering()

if __name__ == "__main__": 
    main()
