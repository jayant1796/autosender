import schedule
import time
import pywhatkit as kit
import datetime

def send_whatsapp_message(phone_number, message, hour, minute):
    try:
       
        current_time = datetime.datetime.now().time()
        current_hour = current_time.hour
        current_minute = current_time.minute
        
        wait_time_seconds = ((hour - current_hour) * 3600) + ((minute - current_minute) * 60)
        
        
        if wait_time_seconds < 0:
            wait_time_seconds += 24 * 3600
        
       
        kit.sendwhatmsg(phone_number, message, hour, minute, wait_time=wait_time_seconds)
        
        print(f"Message sent to {phone_number} at {hour}:{minute}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def schedule_message():
    number = ''#enter number you mant to message
    message = ' '#enter message
    hour = ' '# enter hour
    minute =' ' #enter minute
    send_whatsapp_message(number, message, hour, minute)

schedule.every().day.at(" #").do(schedule_message) # instead of'#' enter hour and minute

while True:
    schedule.run_pending()
    time.sleep(1)
