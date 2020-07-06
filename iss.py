#!/usr/bin/env python

__author__ = 'Diarte Jeffcoat w/help from Kyle Negley, Randy Charity Jr, and RaspberryPi.org("https://projects.raspberrypi.org/en/projects/where-is-the-space-station/5")'

import turtle
import requests
import time


def iss_decorator(func):
    def iss_wrapper():
        print("*" * 40)
        func()
        print("*" * 40)
    return iss_wrapper


@iss_decorator
def get_iss_people():
    link = requests.get('http://api.open-notify.org/astros.json').json()
    print(
        f'Number of Occupants: {link["number"]}')
    for x in link["people"]:
        print(f"{x['name']} is on board the {x['craft']}")


response = requests.get('http://api.open-notify.org/iss-now.json').json()
location = response["iss_position"]
# print(response)
lat = location["latitude"]
lon = location["longitude"]
stamp = time.ctime(response["timestamp"])
print(
    f'Current Latitude: {lat}\nCurrent Longitude: {lon}\nCurrent Time: {stamp}')


def get_iss_position():
    lat = float(location["latitude"])
    lon = float(location["longitude"])

    # print(lat, lon)
    m = turtle.Screen()
    m.setup(720, 360)
    m.setworldcoordinates(-180, -90, 180, 90)
    m.bgpic("map.gif")

    m.addshape("iss.gif")
    t = turtle.Turtle()
    t.shape("iss.gif")
    t.setheading(45)

    t.penup()

    t.goto(lon, lat)

    # Indianapolis, Indiana
    ilat = 39.7684
    ilon = -86.1581

    indy = turtle.Turtle()
    indy.penup()
    indy.color('yellow')
    indy.goto(ilon, ilat)
    indy.dot(5)
    indy.hideturtle()

    url = "http://api.open-notify.org/iss-pass.json"
    url = url + "?lat=" + str(lat) + "&lon=" + str(lon)
    req = requests.get(url).json()
    # print(req)

    passtime = req['response'][1]['risetime']
    # print(passtime)

    style = ('Arial', 10, 'bold')
    indy.write(time.ctime(passtime), font=style)
    m.exitonclick()


def main():
    get_iss_people()
    get_iss_position()


if __name__ == '__main__':
    main()
