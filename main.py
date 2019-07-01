import argparse
import random
#import smtplib
#import getpass
#from bs4 import BeautifulSoup
#from selenium import webdriver
#import requests as req
#from IPython.display import Image
#from IPython.core.display import HTML
#import os
#from dotenv import load_dotenv
#load_dotenv()
#from functools import reduce
#import pandas as pd
#import statistics
#import numpy as np
#import pprint
import json
#from fpdf import FPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter


parser = argparse.ArgumentParser(description='Process some words.')
parser.add_argument('string', metavar='S', type=str, nargs='+',
                    help='a string for the API')
parser.add_argument('--sum', dest='score', action='store_const',
                    const=sum, default=max,
                    help='return the score from sentiment analysis (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

from clean import clean
print(clean('amazon_reviews.txt'))
