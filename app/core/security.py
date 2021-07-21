from typing import Union, Any
from datetime import timedelta, datetime
from app.core.settings import settings
from authlib.jose import jwt
def read_file(filename):
  fh = open(filename, "r")
  try:
      return fh.read()
  finally:
      fh.close()

