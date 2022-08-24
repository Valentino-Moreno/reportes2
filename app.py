from jinja2 import Environment, FileSystemLoader

import pdfkit

env=Environment(loader=FileSystemLoader("templates"))

template= env.get_template("boleta.html")

datos={
    'nombre':'Diego Armando Maradona',
    'legajo':1234,
    'fecha-d':'30-10-2022',
    'fecha-h': '5-12-2022'
}

html=template.render(datos)

f=open('nuevo_html.html','w')
f.write(html)
f.close()

pdfkit.from_file('nuevo_html.html','nuevooopdf.pdf')