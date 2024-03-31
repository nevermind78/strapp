import streamlit as st 
from streamlit_option_menu import option_menu
from pathlib import Path
from dclite import Py
from R import lanR, lanRVide
#import streamlit as st
#from PIL import Image
#import app
from app import show

st.set_page_config(layout="wide")
st.sidebar.title("My Streamlit App")
with st.sidebar:
    selected = option_menu( 
        menu_title= "Menu",
        options = ["Home", "About" ,"Contact"],
        icons = ["house-fill", 'person-circle','envelope-heart-fill'],
        menu_icon =["'chat-text-fill'"],
        default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "gray"},
        "nav-link-selected": {"background-color": "#02ab21"},}
    )
       
match selected:
    case "Home":           
            st.markdown(f'<h2 style="margin-left:180px;">Data Analysis with Python and R</h1> ', unsafe_allow_html=True)
            st.markdown("""
            <ul style="text-align: left; margin-left: 240px;">
            <li>You can use python and r script</li>
            <li>Edit the script below or add your own script</li>
            <li>Note that DataCamp Lite uses Python version == 3.6</li>
            </ul>
            """, unsafe_allow_html=True)
            _,col1,col2,col3,col4,col5 = st.columns(6)
            with col1:
                st.write(
                """
                
                """
                )
                Py(400,1000)
                lanR(400,1000)
            
            # Code R à afficher
            code_r = """
            require(stats) # for lowess, rpois, rnorm
            plot(cars)
            lines(lowess(cars))

            plot(sin, -pi, 2*pi) # see ?plot.function

            ## Discrete Distribution Plot:
            plot(table(rpois(100, 5)), type = "h", col = "red", lwd = 10,
                main = "rpois(100, lambda = 5)")

            ## Simple quantiles/ECDF, see ecdf() {library(stats)} for a better one:
            plot(x <- sort(rnorm(47)), type = "s", main = "plot(x, type = \\"s\\")")
            points(x, cex = .5, col = "dark red")
            """
            col1,col2,col3= st.columns([0.15,0.6,0.1])
            # Affichage du code R dans Streamlit
            with col2:
                 st.write("Vous pouvez utiliser ce code dans l'éditeur de R pour le tester:")
                 st.code(code_r, language='r')

    case "About":
        st.markdown(f'<h1 style="margin-left: 10px;">Welcome to the {selected}</h1>', unsafe_allow_html=True)
        show()
    case "Contact":
        st.title(f"Welcome to the {selected} page")