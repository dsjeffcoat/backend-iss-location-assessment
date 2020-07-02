#!/usr/bin/env python

__author__ = 'Diarte Jeffcoat w/help from Kyle Negley & Randy Charity'

import turtle
import requests


def get_iss_people():
    link = requests.get('http://api.open-notify.org/astros.json').json()
    print(
        f'Number of Occupants: {link["number"]}')
    for x in link["people"]:
        print(x["craft"], x["name"])


def get_iss_location():
    current_loc = []
    location = requests.get('http://api.open-notify.org/iss-now.json').json()
    latitude = location["iss_position"]["latitude"]
    longitude = location["iss_position"]["longitude"]
    timestamp = location["timestamp"]
    print(
        f'Current Position: {latitude}, {longitude}\nCurrent Time: {timestamp}')
    current_loc.extend(location["iss_position"].values())
    return current_loc


def get_iss_position():
    lat, lng = get_iss_location()
    iss_map = turtle.Screen()
    iss_map.bgpic("map.gif")
    iss_map.setup(800, 600)
    iss_map.setworldcoordinates(-180, -90, 180, 90)
    iss_map.addshape("iss.gif")
    cursor = turtle.Turtle()
    cursor.shape("iss.gif")
    cursor.goto(float(lng), float(lat))
    iss_map.exitonclick()


def get_iss_passover():
    pass


def main():
    get_iss_people()
    get_iss_location()
    get_iss_position()
    get_iss_passover()


if __name__ == '__main__':
    main()
