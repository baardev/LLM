#!/bin/env python
from pprint import pprint
import math

def tryit(kwargs, arg, default):
    try:
        rs = kwargs[arg]
    except:
        rs = default
    return rs
def cev(**kwargs,):
    v = tryit(kwargs,'v',False)
    i = tryit(kwargs,'i',False)
    r = tryit(kwargs,'r',False)
    p = tryit(kwargs,'p',False)

    # print(v,i,r,p)
    # exit()

    if v:
        if i: # vi [rp] !r
            if not r: r = v / i
            if not p: p = i * v
        if r: # vr [ip] !r
            if not i: i = v / r
            if not p: p = i * v
        if p: # vp [ir] !r
            if not i: i = p / v
            if not r: r = v / i
    if i:
        if v: # iv [rp] !r
            if not r: r = v / i
            if not p: p = i * v
        if r: # ir [vp] !r
            if not r: v = i * r
            if not p: p = i * v
        if p: # ip [vr] !r
            if not v: v = p / i
            if not r: r = v / i
    if r:
        if v: # rv [ip] !r
            if not i: i = v / r
            if not p: p = i * v
        if i: # ri [vp] !r
            if not v: v = i * r
            if not p: p = i * v
        if p: # rp [vi] !r
            if not v: v = math.sqrt(p * r)
            if not i: i = v / r
    if p:
        if v: # pv [ir] !r
            if not r: r = v / i
            if not i: i = v / r
        if i: # pi [vp] !r
            if not r: v = i * r
            if not p: p = i * v
        if r: # pr [vi] !r
            if not r: v = i * r
            if not i: i = v / r

    #
    # p = i * v
    # v = i * r
    # i = v / r
    # r = v / i
    return {
        '( 6) Volts': v,
        '( 3) Amps': i,
        '( 2) Ohms': r,
        '(18) Watts': p
    }

def show(v,r,i,p):
    if v == 0: v= False
    if r == 0: r= False
    if i == 0: i= False
    if p == 0: p= False

    vals = cev(v=v,r=r,i=i,p=p)

    for key in (vals):
        print(f"{key}: {vals[key]}")

    v = vals['( 6) Volts']
    i = vals['( 3) Amps']
    r = vals['( 2) Ohms']
    p = vals['(18) Watts']


    fstr = f"""
V	=	√PR     {v:06.3f} = √({p:06.3f}*{r:06.3f} 
V	=	P/I     {v:06.3f} =   {p:06.3f}/{i:06.3f}
V	=	IR      {v:06.3f} =   {i:06.3f}*{r:06.3f}

R	=	V/I     {r:06.3f} =   {v:06.3f}/{i:06.3f}
R	=	V2/P    {r:06.3f} =   {v**2:06.3f}/{p:06.3f}
R	=	P/I2    {r:06.3f} =   {p:06.3f}/{i**2:06.3f}

p	=	V2/R    {p:06.3f} =   {v**2:06.3f}/{r:06.3f}
P	=	I2R     {p:06.3f} =   {i**2:06.3f}*{r:06.3f}
P	=	VI      {p:06.3f} =   {v:06.3f}*{i:06.3f}

I	=	V/R     {i:06.3f} =   {v:06.3f}/{r:06.3f}
I	=	P/V     {i:06.3f} =   {p:06.3f}/{v:06.3f}
I	=	√P/R    {i:06.3f} = √({p:06.3f}/{r:06.3f})

"""

    print(fstr)
    #
    #
    # print(f"{p:06.3f} x {i:06.3f} = {v:06.3f}")
    # print(f"{p:06.3f} / {i:06.3f} = {r:06.3f}")
    # print(f"{p:06.3f} / {r:06.3f} = {i:06.3f}")
    # print(f"{p:06.3f} x {i:06.3f} = {p:06.3f}")
    # print("------------------------------")

# show(6,0,0,18)
show(
    0,
    0,
    math.sqrt(3),
    18
)
# show(6,0,0,18)

