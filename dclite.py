import streamlit as st
def Py(n=800,m=800):
    html_code = f"""
            <html>
            <head>
            <meta charset="utf-8" />
            <title>DataCamp Light | Standalone example</title>
            <link rel='shortcut icon' type='image/x-icon' href='https://www.datacamp.com/assets/favicon.ico'/> 
            <script async src="https://cdn.datacamp.com/dcl-react.js.gz"></script>
            </head>
            <body>
            <div class="exercise">
                <div class="title">
                <h2 style="color: white;">This is a python script with a plot</h2>
                </div>     
                <div data-datacamp-exercise data-lang="python" style="height: 100%;">
                <code data-type="pre-exercise-code"></code>
                <code data-type="sample-code">
                    # sample code 
                    import numpy as np
                    import matplotlib.pyplot as plt
                    x = np.arange(0, 5, 0.1);
                    y = np.sin(x)
                    plt.plot(x, y)
                    plt.show()
                </code>
                <code data-type="solution"></code>
                <code data-type="sct"></code>
                <div data-type="hint">Just press 'Run'.</div>
                </div>
            </div>
            </body>
            </html>
            """
    st.components.v1.html(html_code, height=n,  width=m)
