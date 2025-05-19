import pandas as pd
import re

def clean_data(file_to_clean, cleaned_file = 'netflix_titles_clean.xlsx'):
    
    data_frame = pd.read_csv(file_to_clean) #carga del archivo como data frame
    
    data_frame = data_frame.drop_duplicates() #se eliminan duplicados
    
    #rellenar valores nulos
    
    data_frame['rating'] = data_frame['rating'].fillna('Unknown')
    data_frame['director'] = data_frame['director'].fillna('No Director')
    data_frame['cast'] = data_frame['cast'].fillna('Unknown')
    data_frame['country'] = data_frame['country'].fillna('Unknown')
    data_frame['date_added'] = pd.to_datetime(data_frame['date_added'], errors = 'coerce')
    data_frame['release_year'] = pd.to_numeric(data_frame['release_year'], errors = 'coerce')
    
    def clean_country(value):
        if pd.isnull(value):
            return 'Unknown'
        #quitar espacios y comas al inicio
        value = value.lstrip(' ,')
        #quitar espacios después de las comas (ej: "United States, Canada" -> "United States,Canada")
        value = ','.join([country.strip() for country in value.split(',')])
        return value

    data_frame['country'] = data_frame['country'].apply(clean_country)

    def clean_rating(value):
        if isinstance(value, str) and re.match(r'^\d+\s*min$', value.strip()):
            return 'Unknown'
        return value

    data_frame['rating'] = data_frame['rating'].apply(clean_rating)
    
    data_frame.to_excel(cleaned_file, index = False)
    
    print (f"✅ Clean dataset saved as: {cleaned_file}")
    
    return data_frame

clean_data_frame = clean_data('netflix_titles.csv')




