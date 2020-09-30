import pandas as pd
import datetime as dt
import matplotlib as plt
from sqlalchemy import create_engine

path="Resources/googletrends.csv"

data = pd.read_csv(path) 

data.columns=['date','cerb','mask','bike','zoom', 'patio']
data=data.drop(data.index[[0,1]])
data=data.reset_index()

trend_df=data.drop('index', axis=1)


trend_df['cerb'] = trend_df['cerb'].replace(
    {'<1': '0'})

trend_df['cerb']=trend_df['cerb'].astype('str', copy=True).astype('float', copy=True)
trend_df['mask']=trend_df['mask'].astype('str', copy=True).astype('float', copy=True)
trend_df['bike']=trend_df['bike'].astype('str', copy=True).astype('float', copy=True)
trend_df['zoom']=trend_df['zoom'].astype('str', copy=True).astype('float', copy=True)
trend_df['patio']=trend_df['patio'].astype('str', copy=True).astype('float', copy=True)

print(trend_df.head())

n_path="Resources/covid19.csv"

cdata = pd.read_csv(n_path) 

cdata['prname']=cdata['prname'].astype('str', copy=True)

candata=cdata[[ 'date','prname','numconf','numdeaths','numtoday','numdeathstoday','numtested','numtestedtoday','numrecover', 
     'numrecoveredtoday','numactive'
     ]]


candata["numtoday"] = candata["numtoday"].fillna(0).copy()
candata["numdeaths"] = candata["numdeaths"].fillna(0).copy()
candata["numdeathstoday"] = candata["numdeathstoday"].fillna(0).copy()
candata["numtested"] = candata["numtested"].fillna(0).copy()
candata["numtestedtoday"] = candata["numtestedtoday"].fillna(0).copy()
candata["numrecover"] = candata["numrecover"].fillna(0).copy()
candata["numrecoveredtoday"] = candata["numrecoveredtoday"].fillna(0).copy()
candata["numactive"] = candata["numactive"].fillna(0).copy()

provinces_url = "https://www.latlong.net/category/provinces-40-60.html"
territories_url = "https://www.latlong.net/category/territories-40-61.html"
popullation_url ="https://worldpopulationreview.com/canadian-provinces"

provinces_tables = pd.read_html(provinces_url)
territories_tables = pd.read_html(territories_url)
population_tables = pd.read_html(popullation_url)

prov_lat_long_df = provinces_tables[0]
terr_lat_long_df = territories_tables[0]
population_df = population_tables[0]


population_2019_df=population_df.drop(['2016 Population', '2011 Population'], axis=1)
population_2019_df = population_2019_df.sort_values(by='Name', ascending=True)
population_2019_df.reset_index(drop = True, inplace=True)


coordinates_df = pd.concat([prov_lat_long_df, terr_lat_long_df])
clean_coordinates_df = coordinates_df.reset_index(drop = True).drop(8)
canada_coordinates_df = clean_coordinates_df.reset_index(drop = True)
canada_coordinates_df.loc['12'] = ['Northwest Territories', '64.8255', '-124.8457']
canada_coordinates_df = canada_coordinates_df.sort_values(by='Place Name', ascending=True)
canada_coordinates_df.reset_index(drop = True, inplace=True)

territories = pd.concat([population_2019_df, canada_coordinates_df], axis=1, join='inner')
territories_df = territories.drop(['Place Name'], axis=1)
territories_df.rename(columns={'2019 Population': 'population', 'Latitude': 'latitude', 'Longitude': 'longitude'}, inplace=True)
territories_df.rename(columns={'Name': 'prname'}, inplace=True)
territories_df['prname'] = territories_df['prname'].replace(['Newfoundland'],'Newfoundland and Labrador')
territories_df['prname'] = territories_df['prname'].replace(['Northwest Territory'],'Northwest Territories')

canada_covid_df = candata.merge(territories_df, on='prname', how='outer')

canada_df=canada_covid_df.loc[canada_covid_df["prname"]=="Canada"]

canada_df=canada_df[["date", "numconf","numtestedtoday","numtoday","numdeathstoday", "numactive"]]

print(canada_df.head())


covid_trends_df=canada_df.merge(trend_df, on='date', how='inner')

print(covid_trends_df.head())



connection_string = "sqlite:///Covid_Vision.sqlite"
engine = create_engine(f'{connection_string}')

covid_trends_df.to_sql(name = "covid_trends", con=engine, if_exists = 'replace', index = True)
canada_covid_df.to_sql(name = "canada_covid", con=engine, if_exists = 'replace', index = True)

