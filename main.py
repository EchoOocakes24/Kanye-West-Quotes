from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    quote = data["quote"]

    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()

# import requests
# import datetime as dt
#
# MY_LAT = 51.507351
# MY_LONG = -0.127758
#
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0
# }
#
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
#
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
#
# print(sunrise)
# print(sunset)
#
# time_now = dt.datetime.now()
#
# print(time_now.hour)

# import requests
# from datetime import datetime
# import smtplib
# import time
#
# MY_LAT = 51.507351  # Your latitude
# MY_LONG = -0.127758  # Your longitude
#
# # If the ISS is close to my current position
# def is_iss_overhead():
#     response = requests.get(url="http://api.open-notify.org/iss-now.json")
#     response.raise_for_status()
#     data = response.json()
#
#     iss_latitude = float(data["iss_position"]["latitude"])
#     iss_longitude = float(data["iss_position"]["longitude"])
#
#
#     # Your position is within +5 or -5 degrees of the ISS position.
#     if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
#         return True
#
# # and it is currently dark
# def is_night():
#     parameters = {
#             "lat": MY_LAT,
#             "lng": MY_LONG,
#             "formatted": 0,
#         }
#
#     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#     response.raise_for_status()
#     data = response.json()
#     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#
#     time_now = datetime.now().hour
#
#     if time_now >= sunset or time_now >= sunrise:
#         return True
#
#
# # Then send me an email to tell me to look up.
# my_email = "echodeguzman007@gmail.com"
# password = "wdyj jhhk cgsf emnr"
#
# # BONUS: run the code every 60 seconds.
# while True:
#     time.sleep(60)
#     if is_iss_overhead() and is_night():
#         with smtplib.SMTP("smtp.gmail.com") as connection:
#             connection.starttls()
#             connection.login(user=my_email, password=password)
#             connection.sendmail(from_addr=my_email, to_addrs="saysonjomer@gmail.com", msg="Subject: Night Sky \n\n"
#                                                                                           "Please Look Up and Loot at the mesmerizing Night Sky.")
#
