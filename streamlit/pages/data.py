import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64
from support.apiConnection import breeding_preguin 

def data_page():
    st.title("Data from Palmer Archipelago (Antarctica)")

    data = breeding_preguin()
    data_years = [int(row['year']) for row in data]
    data_average_born = [row['average_born_by_species']  for row in data]

    gento_y = []
    chinstrap_y = []
    adelie_y = []

    for value in data_average_born:
        gento_y.append(value['gentoo'])
        chinstrap_y.append(value['chinstrap'])
        adelie_y.append(value['adelie'])

    lst = [data_years, gento_y, chinstrap_y, adelie_y]
    df = pd.DataFrame(lst).T
    df = df.rename(columns={0: 'year', 1: 'Gento', 2: 'Chinstrap', 3: 'Adelie'})
    df = df.set_index('year')
    st.write(df)
    st.download_button(
        label="Download CSV of Breeding Pairs Signy Island",
        data = df.to_csv().encode('utf-8'),
        file_name='Breeding Pairs.csv',
        mime='text/csv')



    #report_text = st.text_input("Report Text")
    html = """
    <H1 align="center">html2fpdf</H1>
    <h2>Basic usage</h2>
    <p>You can now easily print text mixing different
    styles : <B>bold</B>, <I>italic</I>, <U>underlined</U>, or
    <B><I><U>all at once</U></I></B>!<BR>You can also insert links
    on text, such as <A HREF="http://www.fpdf.org">www.fpdf.org</A>,
    or on an image: click on the logo.<br>
    <center>
    <A HREF="http://www.fpdf.org"><img src="tutorial/logo.png" width="104" height="71"></A>
    </center>
    <h3>Sample List</h3>
    <ul><li>option 1</li>
    <ol><li>option 2</li></ol>
    <li>option 3</li></ul>

    <table border="0" align="center" width="50%">
    <thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
    <tbody>
    <tr><td>cell 1</td><td>cell 2</td></tr>
    <tr><td>cell 2</td><td>cell 3</td></tr>
    </tbody>
    </table>
    """
    export_as_pdf = st.button("Export Report")

    def create_download_link(val, filename):
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

    if export_as_pdf:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40, 10, html)
        html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")
        st.markdown(html, unsafe_allow_html=True)


