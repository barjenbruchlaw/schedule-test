import schedule
import time

def delayed_funct():
    print("The time is now 21:47")

schedule.every().day.at("21:47").do(delayed_funct)

while True:
    schedule.run_pending()
    time.sleep(1)
