# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:57:33 2023

@author: CheeSeong
"""

import requests

def send_telegram_message(group_id , send_url , text_type , error_message = ""):
    
    date_value = datetime.now() - timedelta(days = 1)
    date = date_value.strftime("%Y-%m-%d")
    
    if text_type == 'failed':
        text = f"Showroom data tried to update for {date} but failed. Error message: {error_message}"
    else:
        text = f"Showroom data have been updated successfully for {date}."

    group_id = group_id
    send_url = send_url

    requests.post(send_url , json = {'chat_id' : group_id, 'text': text})
    
send_telegram_message(-1001763318295 , "https://api.telegram.org/bot5564798304:AAHyN_uuboKonRVhVvVSB9sBe9gfhiViJXk/sendMessage" , "failed" , error_message = "Testing")
