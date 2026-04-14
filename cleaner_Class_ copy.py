def clean_data(data):
    clean_data_list = []

    for row in data:
        if row != "minutes\n":
            clean_data.append(float(row.strip()))
   
    return clean_data