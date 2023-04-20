import argparse
from math import gcd

def generate_sig(q,p,a,x,ke,show_steps):
    r = pow(a,ke,p)
    s = ((x-q*r))