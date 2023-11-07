import os, sys
try:
    __import__("bczr").main()
except Exception as e:
    exit(str(e))
