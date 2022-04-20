import os
import sys
import pyjoycon
from pyjoycon import JoyCon, get_L_id

ids = get_L_id()
joycon = JoyCon(*ids)
