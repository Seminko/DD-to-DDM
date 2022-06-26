def convert_gps_coords_DD_to_DMM(lat, lon):
    lat_degrees = int(lat)
    lat_minutes = round((lat - lat_degrees) * 60, 3)
    lat_minutes_int = int(lat_minutes)
    lat_minutes_dec = round(lat_minutes - lat_minutes_int, 3)
    
    lat_degrees_str = str(lat_degrees)
    lat_minutes_str = str(lat_minutes_int)
    lat_minutes_dec_str = str(lat_minutes_dec)[2:]
    
    lat_str = "N " + ((2-len(lat_degrees_str)) * "0") + lat_degrees_str + "° " + ((2-len(lat_minutes_str)) * "0") + \
                lat_minutes_str + "." + ((2-len(lat_minutes_dec_str)) * "0") + lat_minutes_dec_str
    
    lon_degrees = int(lon)
    lon_minutes = round((lon - lon_degrees) * 60, 3)
    lon_minutes_int = int(lon_minutes)
    lon_minutes_dec = round(lon_minutes - lon_minutes_int, 3)
    
    lon_degrees_str = str(lon_degrees)
    lon_minutes_str = str(lon_minutes_int)
    lon_minutes_dec_str = str(lon_minutes_dec)[2:]
    
    lon_str = "E " + ((3-len(lon_degrees_str)) * "0") + lon_degrees_str + "° " + ((2-len(lon_minutes_str)) * "0") + \
        lon_minutes_str + "." + ((2-len(lon_minutes_dec_str)) * "0") + lon_minutes_dec_str
    
    final_str_coords = lat_str + " " + lon_str
    
    return final_str_coords
