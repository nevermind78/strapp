import streamlit as st
def lanR(n=800,m=800):
    html_code = """
    <html>
    <head>
    <meta charset="utf-8" />
    <title>DataCamp Light | Standalone example</title>
    <link rel='shortcut icon' type='image/x-icon' href='https://www.datacamp.com/assets/favicon.ico'/>
    <style>
    .exercise {
      margin: 00px;
    }
    </style>
    <script async src="https://cdn.datacamp.com/dcl-react.js.gz"></script>
    </head>
    <body>
    <div class="exercise">
    <div class="title">
      <h2 style="color: white;">This is an R script</h2>
    </div>
     <div data-datacamp-exercise data-lang="r" style="height: 100%;>
      <code data-type="pre-exercise-code"># no pec</code>
      <code data-type="sample-code">
        # Assign the value 5 to the variable my_apples


        # Print out the value of the variable my_apples
      </code>
      <code data-type="solution">
        # Assign the value 5 to the variable my_apples
        my_apples &lt;- 5

        # Print out the value of the variable my_apples
        my_apples
      </code>
      <code data-type="sct">
        test_object(&quot;my_apples&quot;,
        undefined_msg = &quot;Please make sure to define a variable `my_apples`.&quot;,
        incorrect_msg = &quot;Make sure that you assign the correct value to `my_apples`.&quot;)
        test_output_contains(&quot;my_apples&quot;, incorrect_msg = &quot;Have you
        explicitly
        told R to print out the `my_apples` variable to the console?&quot;)
        success_msg(&quot;Great! Continue to the next exercise!&quot;)
      </code>
      <div data-type="hint">
        <p>Remember that if you want to assign a number or an object to a variable in R, you
          can
          make use of the assignment operator
          <code>&lt;-</code>. Alternatively, you can use
          <code>=</code>, but
          <code>&lt;-</code> is widely preferred in the R community.
        </p>
      </div>
    </div>
    </body>
    </html>"""
    st.components.v1.html(html_code, height=n,  width=m)


def lanRVide(n=800,m=800):
    html_code = """
    <html>
    <head>
    <meta charset="utf-8" />
    <title>DataCamp Light | Standalone example</title>
    <link rel='shortcut icon' type='image/x-icon' href='https://www.datacamp.com/assets/favicon.ico'/>
    <style>
    .exercise {
      margin: 00px;
    }
    </style>
    <script async src="https://cdn.datacamp.com/dcl-react.js.gz"></script>
    </head>
    <body>
    <div class="exercise">
    <div class="title">
      <h2 style="color: white;">R editor </h2>
    </div>
     <div data-datacamp-exercise data-lang="r" style="height: 100%;>
      <code data-type="pre-exercise-code"># no pec</code>
      <code data-type="sample-code">
        # Write Your Code here 

      </code>
      <code data-type="sct"></code>
      <div data-type="hint">
        <p> Run The script </p>
      </div>
    </div>
    </body>
    </html>"""
    st.components.v1.html(html_code, height=n,  width=m)