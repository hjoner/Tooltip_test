import json
import pydeck as pdk
import pandas as pd
from urllib.request import urlopen

token = 'your_token'

path = ('PORTO_ALEGRE_GRID_CVLI_sem0_TURNO_0_tipo0.geojson')
with open(path) as response:
        grid = json.load(response)
lat = -30.0478
lng = -51.1706

view_state = pdk.ViewState(latitude= lat,
                           longitude= lng,
                           zoom=11,
                           pitch=0) 

layer_2d = pdk.Layer( 'GeoJsonLayer',
                            grid, id='geojson',
                            opacity = 0.5,
                            stroked = True, lineWidthScale = 5,
                            filled = True,
                            extruded = False,
                            wireframe= True,pickable=True,
                            get_elevation='properties.CRIMES * 200',
                            get_fill_color = 'properties.cor' , 
                            get_line_color=[255, 0, 0, 500],
                            tooltip=True,)

tooltip = {
   "html": "<b>Nro Ocor:</b> {Nro Ocor} <br/> <b>Data Fato:</b> {Data Fato}<br/><b>Dia da Semana:</b> {Dia da Semana} <br/> <b>Hora Fato:</b> {Hora Fato} <br/> <b>Orgao Carga:</b> {Orgao Carga} <br/> <b>Tipo Fato:</b> {Tipo Fato} <br/> <b>BAIRRO:</b> {BAIRRO} <br/> <b>Ano Registro:</b> {Ano Registro} <br/> <b>Flagrante:</b> {Flagrante} <br/> <b>Endereco:</b> {Endereco} <br/> <b>Nro Interno Ocorrencia:</b> {Nro Interno Ocorrencia} <br/> <b>Nro Endereco:</b> {Nro Endereco} ",
   "style": {
        "backgroundColor": "steelblue",
        "color": "white"
   }
}

# MAPA 1 #

mapa1 = pdk.Deck(mapbox_key = token,
initial_view_state=view_state, tooltip = tooltip,
layers=[layer_2d],
)   
mapa1.to_html('teste.html')