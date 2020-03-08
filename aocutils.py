import sys
import argparse

def getargs():
   parser = argparse.ArgumentParser()
   parser.add_argument("filename")
   args = parser.parse_args()
   return args

def getdata( args ):
   filename = args.filename
   data = open(filename,"r")
   l = []
   for line in data:
       l.append( int(line) )
   return l