import pandas as pd
import numpy as np

df1 = pd.read_csv('Tratados_internacionales_de_Colombia.csv')

###

df1['Fecha de Adopcion'] =  pd.to_datetime(df1['Fecha de Adopcion'], format='%d/%M/%Y')
df1['Fecha de Adopcion'] = df1['Fecha de Adopcion'].dt.strftime('%Y-%m-%d')
df1['Fecha de Adopcion'] = pd.to_datetime(df1['Fecha de Adopcion'])

###

data = []
for Temas in df1['Temas']:
    if Temas == '(NO REGISTRA)':
        Temas = pd.NA
    else:
        Temas = Temas
    data.append(Temas)
df1 = df1.assign(Temas=data)

###

data = []
for Bilateral in df1['Bilateral']:
    if Bilateral == 'SI':
        Bilateral = True
    else:
        Bilateral = False
    data.append(Bilateral)
df1 = df1.assign(Bilateral=data)

###

data = []
for Depositario in df1['Depositario']:
    if Depositario == '(NO REGISTRA)':
        Depositario = pd.NA
    else:
        Depositario = Depositario
    data.append(Depositario)
df1 = df1.assign(Depositario=data)

###

data = []
for Suscribio_Por_Colombia in df1['Suscribio Por Colombia']:
    if Suscribio_Por_Colombia == '(NO REGISTRA)':
        Suscribio_Por_Colombia = pd.NA
    else:
        Suscribio_Por_Colombia = Suscribio_Por_Colombia
    data.append(Suscribio_Por_Colombia)
df1 = df1.assign(Suscribio_Por_Colombia=data)

###

data = []
for Vigente in df1['Vigente']:
    if Vigente == 'SI':
        Vigente = True
    else:
        Vigente = False
    data.append(Vigente)
df1 = df1.assign(Vigente=data)

###

data = []
for Fecha_Ley_Aprobatoria in df1['Fecha Ley Aprobatoria']:
    if Fecha_Ley_Aprobatoria == '(NO REGISTRA)':
        Fecha_Ley_Aprobatoria = pd.NA
    else:
        Fecha_Ley_Aprobatoria = pd.to_datetime(Fecha_Ley_Aprobatoria, format='%d/%M/%Y')
        Fecha_Ley_Aprobatoria = Fecha_Ley_Aprobatoria.strftime('%Y-%m-%d')
    data.append(Fecha_Ley_Aprobatoria)
df1 = df1.assign(Fecha_Ley_Aprobatoria=data)

###

data = []
for Numero_Ley_Aprobatoria in df1['Numero Ley Aprobatoria']:
    if Numero_Ley_Aprobatoria == '(NO REGISTRA)':
        Numero_Ley_Aprobatoria = pd.NA
    else:
        Numero_Ley_Aprobatoria = Numero_Ley_Aprobatoria
    data.append(Numero_Ley_Aprobatoria)
df1 = df1.assign(Numero_Ley_Aprobatoria=data)

###

data = []
for Sentencia_Fecha_Ley in df1['Sentencia Fecha Ley']:
    if Sentencia_Fecha_Ley == '(NO REGISTRA)':
        Sentencia_Fecha_Ley = pd.NA
    else:
        Sentencia_Fecha_Ley = pd.to_datetime(Sentencia_Fecha_Ley, format='%d/%M/%Y')
        Sentencia_Fecha_Ley = Sentencia_Fecha_Ley.strftime('%Y-%m-%d')
    data.append(Sentencia_Fecha_Ley)
df1 = df1.assign(Sentencia_Fecha_Ley=data)

###

data = []
for Sentencia_Numero in df1['Sentencia Numero']:
    if Sentencia_Numero == '(NO REGISTRA)':
        Sentencia_Numero = pd.NA
    else:
        Sentencia_Numero = Sentencia_Numero
    data.append(Sentencia_Numero)
df1 = df1.assign(Sentencia_Numero=data)

###

data = []
for Decreto_Fecha_Diario_Oficial in df1['Decreto Fecha Diario Oficial']:
    if Decreto_Fecha_Diario_Oficial == '(NO REGISTRA)':
        Decreto_Fecha_Diario_Oficial = pd.NA
    else:
        Decreto_Fecha_Diario_Oficial = pd.to_datetime(Decreto_Fecha_Diario_Oficial, format='%d/%M/%Y')
        Decreto_Fecha_Diario_Oficial = Decreto_Fecha_Diario_Oficial.strftime('%Y-%m-%d')
    data.append(Decreto_Fecha_Diario_Oficial)
df1 = df1.assign(Decreto_Fecha_Diario_Oficial=data)

###

data = []
for Decreto_Numero_Diario_Oficial in df1['Decreto Numero Diario Oficial']:
    if Decreto_Numero_Diario_Oficial == '(NO REGISTRA)':
        Decreto_Numero_Diario_Oficial = pd.NA
    else:
        Decreto_Numero_Diario_Oficial = Decreto_Numero_Diario_Oficial
    data.append(Decreto_Numero_Diario_Oficial)
df1 = df1.assign(Decreto_Numero_Diario_Oficial=data)

###

df1['Fecha_Ley_Aprobatoria'] = pd.to_datetime(df1['Fecha_Ley_Aprobatoria'])
df1['Sentencia_Fecha_Ley'] = pd.to_datetime(df1['Sentencia_Fecha_Ley'])
df1['Decreto_Fecha_Diario_Oficial'] = pd.to_datetime(df1['Decreto_Fecha_Diario_Oficial'])

###

df1 = df1[['Nombre del Tratado','Bilateral','Lugar de Adopcion','Fecha de Adopcion','Estados-Organismos','Temas','Naturaleza del Tratado','Depositario','Suscribio_Por_Colombia','Vigente','Fecha_Ley_Aprobatoria','Numero_Ley_Aprobatoria','Sentencia_Fecha_Ley','Sentencia_Numero','Decreto_Fecha_Diario_Oficial','Decreto_Numero_Diario_Oficial']]

############# segundo archivo #################

ruta_api = 'https://restcountries.com/v3.1/all'
df2 = pd.read_json(ruta_api)

###########

data = []
for name_spa in df2['translations']:
    name_spa = name_spa['spa']['common']
    data.append(name_spa)
df2 = df2.assign(pais_del_tratado=data)
df2['pais_del_tratado'] = df2['pais_del_tratado'].str.upper()

###########

data = []
for cod in df2['idd']:
    if cod != {}:
        cod = cod['root'] + cod['suffixes'][0]
    else:
        cod = ''
    data.append(cod)
df2 = df2.assign(codigo_de_llamadas=data)

###########

data = []
for zonah in df2['timezones']:
    zonah = zonah[0]
    data.append(zonah)
df2 = df2.assign(zona_horaria=data)

###########

data = []
for cap in df2['capital']:
    if cap is np.nan:
        cap = cap
    else:
        cap = cap[0]
    data.append(cap)
df2 = df2.assign(capital=data)

###########

data = []
for fronteras in df2['borders']:
    if fronteras is np.nan:
        fronteras = 0
    else:
        fronteras = len(fronteras)
    data.append(fronteras)
df2 = df2.assign(fronteras=data)

###########

data = []
for idiomas in df2['languages']:
    if idiomas is np.nan:
        idiomas = 0
    else:
        idiomas = list(idiomas.values())
    data.append(idiomas)
df2 = df2.assign(idiomas=data)

###########

df2['monedas'] = df2['currencies'].astype(str).str[2:5]
df2['borders'] = df2['borders'].astype(str).str[1:-1]
df2 = df2.rename(columns={'population':'poblacion'})
df2['idiomas'] = df2['idiomas'].astype(str).str[1:-1]

###########

data = []
for dif_horaria in df2['zona_horaria']:
    if '+00:00' in dif_horaria:
        dif_horaria = +5.0
    elif '-01:00' in dif_horaria:
        dif_horaria = +4.0
    elif '-02:00' in dif_horaria:
        dif_horaria = +3.0
    elif '-03:00' in dif_horaria:
        dif_horaria = +2.0
    elif '-04:00' in dif_horaria:
        dif_horaria = +1.0
    elif '-05:00' in dif_horaria:
        dif_horaria = 0.0
    elif '-06:00' in dif_horaria:
        dif_horaria = -1.0
    elif '-07:00' in dif_horaria:
        dif_horaria = -2.0
    elif '-08:00' in dif_horaria:
        dif_horaria = -3.0
    elif '-09:00' in dif_horaria:
        dif_horaria = -4.0
    elif '-10:00' in dif_horaria:
        dif_horaria = -5.0
    elif '-11:00' in dif_horaria:
        dif_horaria = -6.0
    elif '-12:00' in dif_horaria:
        dif_horaria = -7.0
    elif '-13:00' in dif_horaria:
        dif_horaria = -8.0
    elif '+01:00' in dif_horaria:
        dif_horaria = +6.0
    elif '+02:00' in dif_horaria:
        dif_horaria = +7.0
    elif '+03:00' in dif_horaria:
        dif_horaria = +8.0
    elif '+04:00' in dif_horaria:
        dif_horaria = +9.0
    elif '+05:00' in dif_horaria:
        dif_horaria = +10.0
    elif '+06:00' in dif_horaria:
        dif_horaria = +11.0
    elif '+07:00' in dif_horaria:
        dif_horaria = +12.0
    elif '+08:00' in dif_horaria:
        dif_horaria = +13.0
    elif '+09:00' in dif_horaria:
        dif_horaria = +14.0
    elif '+10:00' in dif_horaria:
        dif_horaria = +15.0
    elif '+11:00' in dif_horaria:
        dif_horaria = +16.0
    elif '+12:00' in dif_horaria:
        dif_horaria = +17.0
    elif '+13:00' in dif_horaria:
        dif_horaria = +18.0
    else:
        dif_horaria = +5.0
    data.append(dif_horaria)
df2 = df2.assign(dif_horaria=data)

###########

df2 = df2[['pais_del_tratado','codigo_de_llamadas','capital','region','subregion','poblacion','area','zona_horaria','monedas','idiomas','fronteras','dif_horaria']]

df_all = pd.merge(df1,df2,left_on='Estados-Organismos',right_on='pais_del_tratado',how='left')

df_all = df_all[['Nombre del Tratado','Bilateral','Lugar de Adopcion','Fecha de Adopcion','Estados-Organismos','Temas','Naturaleza del Tratado','Depositario','Suscribio_Por_Colombia','Vigente','Fecha_Ley_Aprobatoria','Numero_Ley_Aprobatoria','Sentencia_Fecha_Ley','Sentencia_Numero','Decreto_Fecha_Diario_Oficial','Decreto_Numero_Diario_Oficial','pais_del_tratado','codigo_de_llamadas','capital','region','subregion','poblacion','area','zona_horaria','monedas','idiomas','fronteras','dif_horaria']]

df_all.to_parquet('df_all.parquet.gzip',compression='gzip')

