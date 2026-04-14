def clean_data(data):
    clean_data_list = []

    for flt in data [1:]:
        cleaned_val = float(flt.strip())
        clean_data_list.append(cleaned_val)

   
    return clean_data_list