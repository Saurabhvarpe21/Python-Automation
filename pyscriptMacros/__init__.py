import pandas as pd
def convert_to_upper_case(lname):
    df = pd.read_excel(lname)
    pd.set_option('colheader_justify', 'center')  # FOR TABLE <th>
    table = df.to_html(classes='mystyle')
    html_string = f'''
       <html>
         <head><title>HTML Pandas Dataframe with CSS</title></head>
         <link rel="stylesheet" type="text/css" href="df_style.css"/>
         <body>
           {table}
         </body>
       </html>'''
    # html_string.format(table=df.to_html(classes='mystyle'))
    # html = df.to_html()
    return html_string