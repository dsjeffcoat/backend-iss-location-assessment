#!/usr/bin/env python

__author__ = 'Diarte Jeffcoat w/help from Kyle Negley, Randy Charity Jr, and RaspberryPi.org("https://projects.raspberrypi.org/en/projects/where-is-the-space-station/5")'

import turtle
import requests
import time


def get_iss_people():
    link = requests.get('http://api.open-notify.org/astros.json').json()
    print(
        f'Number of Occupants: {link["number"]}')
    for x in link["people"]:
        print(f"{x['name']} is on board the {x['craft']}")


def get_iss_location():
    current_loc = []
    location = requests.get(
        'http://api.open-notify.org/iss-now.json').json()
    latitude = location["iss_position"]["latitude"]
    longitude = location["iss_position"]["longitude"]
    timestamp = location["timestamp"]
    print(
        f'Current Position: {latitude}, {longitude}\nCurrent Time: {timestamp}')
    current_loc.extend(location["iss_position"].values())
    return current_loc


def get_iss_position():
    lat, lon = get_iss_location()
    m = turtle.Screen()
    m.setup(720, 360)
    m.setworldcoordinates(-180, -90, 180, 90)
    m.bgpic("map.gif")

    m.addshape("iss.gif")
    t = turtle.Turtle()
    t.shape("iss.gif")
    t.setheading(90)

    t.penup()
    t.goto(float(lon), float(lat))

    # Indianapolis, Indiana
    lat = 39.7684
    lon = -86.1581

    indy = turtle.Turtle()
    indy.penup()
    indy.color('yellow')
    indy.goto(lon, lat)
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
    get_iss_location()
    get_iss_position()


if __name__ == '__main__':
    main()
