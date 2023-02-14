import gspread



def append_data(username, user_id, hash_text, amount, date_time):
    
    gc = gspread.service_account(filename="C:\\Users\\zeros\\PycharmProjects\\Bots\\cryptoBot\\usdt-info-300ee474608b.json")

    worksheet = gc.open_by_key(key="1dm3GkYbFdbL-ya4PFmFTjKSxiMxnrrQoSGeynbU9Wto")

    current_sheet = worksheet.worksheet("first_list")
    
    current_sheet.append_row([f"{username}", f"{user_id}", f"{hash_text}", f"{amount}", f"{date_time}"])

    return True