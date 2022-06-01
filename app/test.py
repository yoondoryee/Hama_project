import RPi.GPIO as GPIO
import sys
import time
import adafruit_dht
import pymysql
import board

sensor = adafruit_dht.DHT11(board.D18)
