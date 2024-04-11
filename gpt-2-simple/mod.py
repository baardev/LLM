#!/bin/env python
import shutil as sh
import sys
import getopt
from colorama import Fore
from pprint import pprint
import json
from strip_ansi import strip_ansi

# [] brackets !r
def replace_w_brackets(old, new, text):
    idx = 0
    while idx < len(text):
        # index_l = text.lower().find(old.lower(), idx)
        index_l = text.find(old, idx)
        if index_l == -1:
            return text
        text = text[:index_l] + "["+new+"]" + text[index_l + len(old):]
        idx = index_l + len(new)
    return text

# markdown !r

def replace_w_md(old, new, text):
    idx = 0
    while idx < len(text):
        # index_l = text.lower().find(old.lower(), idx)
        index_l = text.find(old, idx)
        if index_l == -1:
            return text
        text = text[:index_l] + "**"+new+"**" + text[index_l + len(old):]
        idx = index_l + len(new)
    return text

# no [] brackets !r
def replace_w_plain(old, new, text):
    idx = 0
    while idx < len(text):
        # index_l = text.lower().find(old.lower(), idx)
        index_l = text.find(old, idx)
        if index_l == -1:
            return text
        text = text[:index_l] + new + text[index_l + len(old):]
        idx = index_l + len(new)
    return text


def showhelp():
    str = f"""
        -h, --help      this test
        -f, --file      <path to text file>
"""
    print(str,flush=True)
    exit()

def showidx(reps, idx, lines):
    rep = reps[idx]
    
    # print(Fore.LIGHTWHITE_EX+f"**┌───────────────────────────────────────────────**"+Fore.RESET)
    # print(Fore.LIGHTWHITE_EX+f"**│ DEFINITIONS FOR {idx} ARE AS FOLLOWS**"+Fore.RESET)
    # print(Fore.LIGHTWHITE_EX+f"**└───────────────────────────────────────────────**"+Fore.RESET)

    # for key in rep:
    #     if f"{key}" != strip_ansi(rep[key]):
    #         print(f"**{key}** is defined as **{rep[key]}**")
    # print("")
    # for key in rep:
    #     if f"{key}" == strip_ansi(rep[key]):
    #     # if 1==1:
    #         print(f"**{key}** remains as **{rep[key]}**")
    # 

    newlines = lines
    newlines = replace_w_md("TITLE",idx,newlines)
    for key in rep:
        # newlines = replace_w_md(key,rep[key],newlines)
        newlines = replace_w_plain(key,rep[key],newlines)
    # need to run through twice !r
    for key in rep:
        # newlines = replace_w_md(key,rep[key],newlines)
        newlines = replace_w_plain(key,rep[key],newlines)
        # add special notes for light, numbers !r
        if idx in ["Light"]:
            newlines = replace_w_plain("(condition_1)","(Not Possible for contexts with constants)",newlines)
        else:
            newlines = replace_w_plain("(condition_1)","",newlines)

    print(newlines,flush=True)
    print("",flush=True)
    print('\x0c',end='')

# for color
def c(str,idxval):
    fc = [
        Fore.LIGHTRED_EX,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTMAGENTA_EX,
        Fore.YELLOW,
    ]
    # idxval = idxval + 1
    return fc[idxval]+str+Fore.RESET



def re_MOMENTUM(k): # 3 !r
    # Momentum is a measure of the amount of motion in an object. MOMENTUM = (MASS x VELOCITY) !c
    if k == "Newton Org":       return "MOMENTUM"   # MOMENTUM !r
    if k == "Numbers":          return "3"   # MOMENTUM !r
    if k == "Cause Effect":     return "RATE-OF-CHANGE"   # MOMENTUM !r
    if k == "Electricity":      return "AMPERAGE"   # MOMENTUM !r
    if k == "Light":            return "DEFINED-MOTION"   # MOMENTUM !r
    if k == "E=mc²":            return "MEASURE-OF-MOTION"   # MOMENTUM !r
    if k == "Society":          return "LEVEL-OF-ACTIVITY"   # MOMENTUM !r
    if k == "Economics":        return "MARKETCAP" # MOMENTUM !r
    if k == "Intelligence":     return "INTERACTION-POTENTIAL" # MOMENTUM !r
    if k == "Awareness":        return "MEASURE~3-momentum~" # MOMENTUM !r

    if k == "Tholons P1":       return "AMOUNT-OF-MOTION"   # MOMENTUM !r
    if k == "Tholons P2":       return "AMOUNT-OF-MOTION"   # MOMENTUM !r
    # if k == "Alternative Definitions":         return "MAGNITUDE-OF-MOTION-OF-MASS"   # MOMENTUM 
    # if k == "Mental Physical Emotional": return "AMOUNT-OF-EMOCION"   # MOMENTUM 
    # if k == "Tholons":          return "AMOUNT-OF-MOTION"   # MOMENTUM 

def re_MASS(k):# 2 !g
    # MASS is a measure of INSTANCE, a property of BODY !c
    if k == "Newton Org":       return "MASS"   # MASS !g
    if k == "Numbers":          return "2"   # MASS !g
    if k == "Cause Effect":     return "INSTANCE"   # MASS !g
    if k == "Electricity":      return "RESISTANCE"   # MASS !g
    if k == "Light":            return "TIME"    # MASS !g#  (as frequency)" !r
    if k == "E=mc²":            return "m"   # MASS !g
    if k == "Society":          return "PROPERTY-AND-INFRASTRUCTURE"   # MASS !g
    if k == "Economics":          return "PRODUCTION & OVERHEAD" # MASS !g
    if k == "Intelligence":          return "INSTANCE" # MASS !g
    if k == "Awareness":        return "DUALITY~2~" # MASS !g

    if k == "Tholons P1":       return "DEFINITION"    # MASS !g
    if k == "Tholons P2":       return "LIMITATION"    # MASS !g
    # if k == "Alternative Definitions":         return "SCOPED-INSTANCE-IN-MATERIAL-CONTEXT"   # MASS 
    # if k == "Mental Physical Emotional": return "PHYSICAL-LIFEFORM"   # MASS 
    # if k == "Tholons":          return "DEFINITION/LIMITATION"   # MASS 

def re_MOTION(k):# 3 !r
    # MOTION is a state of movement !c
    if k == "Newton Org":       return "MOTION"   # MOTION !r
    if k == "Numbers":          return "3"  # MOTION !r
    if k == "Cause Effect":     return "CHANGE-IN-LOCATION"  # MOTION !r
    if k == "Electricity":      return "CURRENT"  # MOTION !r
    if k == "Light":            return "SPACE"  # MOTION !r
    if k == "E=mc²":            return "c"  # MOTION !r
    if k == "Society":          return "PEOPLE"  # MOTION !r
    if k == "Economics":        return "CHANGES" # MOTION !r
    if k == "Intelligence":     return "INTELLIGENCE" # MOTION !r
    if k == "Awareness":        return "MOVEMENT~3-motion~" # MOTION !r

    if k == "Tholons P1":       return "CONTRIBUTION"   # MOTION !r
    if k == "Tholons P2":       return "INTEGRATION"   # MOTION !r
    # if k == "Alternative Definitions":         return "CHANGES-IN-SPACE-TIME-POSITION"  # MOTION 
    # if k == "Mental Physical Emotional": return "EMOCION"  # MOTION 
    # if k == "Tholons":          return "CONTRIBUTION/INTEGRATION"  # MOTION 

def re_VELOCITY(k):# 3 !r
    # VELOCITY is the change in displacement over time in a direction !c
    if k == "Newton Org":       return "VELOCITY"  # VELOCITY !r
    if k == "Numbers":          return "3~v~"  # VELOCITY !r
    if k == "Cause Effect":     return "SPEED-AND-DIRECTION-OF-DISPLACEMENT"  # VELOCITY !r
    if k == "Electricity":      return "CURRENT~v~"   # VELOCITY !r
    if k == "Light":            return "SPACE~v~" #   # VELOCITY !r (as wavelength)" !r
    if k == "E=mc²":            return "c~v~"
    if k == "Society":          return "PEOPLE~v~"  # VELOCITY !r
    if k == "Economics":        return "SERVICE PRODUCT"  # VELOCITY !r
    if k == "Intelligence":     return "APPLIED-INTELLIGENCE~v~"# VELOCITY !r
    if k == "Awareness":        return "INTENTION~3-velocity~" # VELOCITY !r

    if k == "Tholons P1":       return "CONTRIBUTION~v~"  # VELOCITY !r
    if k == "Tholons P2":       return "INTEGRATION~v~"  # VELOCITY !r
    # if k == "Alternative Definitions":         return "RATE-AND-DIRECTION-BODY-IS-MOVING"  # VELOCITY
    # if k == "Mental Physical Emotional": return "INTENTION"  # VELOCITY
    # if k == "Tholons":          return "CONTRIBUTION/INTEGRATION~v~"  # VELOCITY

def re_ACCELERATION(k):# 3 !r
    # Acceleration is the rate of change of velocity !c
    # if k == "Alternative Definitions":         return "increase of change of position in space over time" 
    if k == "Newton Org":       return "ACCELERATION"  # ACCELERATION !r
    if k == "Numbers":          return "3~a~"  # ACCELERATION !r
    if k == "Cause Effect":     return "INCREASED-IMBALANCE"  # ACCELERATION !r
    if k == "Electricity":      return "CURRENT~a~"  # ACCELERATION !r
    if k == "Light":            return "SPACE~a~"   # ACCELERATION !r#! (as wavelength)" !r
    if k == "E=mc²":            return "c~a~"  # ACCELERATION !r
    if k == "Society":          return "GATHERINGS-OF-PEOPLE~a~"  # ACCELERATION !r
    if k == "Economics":        return "GROWTH"# ACCELERATION !r
    if k == "Intelligence":     return "NOVELTY~a~"# ACCELERATION !r
    if k == "Awareness":        return "CREATION~3-acceleration~" # ACCELERATION !r

    if k == "Tholons P1":       return "CONTRIBUTION~a~"  # ACCELERATION !r
    if k == "Tholons P2":       return "INTEGRATION~a~"  # ACCELERATION !r
    # if k == "Alternative Definitions":         return "INCREASE-IN-MOTION"  # ACCELERATION 
    # if k == "Mental Physical Emotional": return "INCREASED EMOCION"  # ACCELERATION 
    # if k == "Tholons":          return "CONTRIBUTION/INTEGRATION~a~"  # ACCELERATION 

def re_FORCE(k): # 6 !b
    # Force is the interaction between bodies that result in pushing or pulling. !c
    if k == "Newton Org":       return "FORCE"  # FORCE !b
    if k == "Numbers":          return "6"  # FORCE !b
    if k == "Cause Effect":     return "IMPULSE"  # FORCE !b
    if k == "Electricity":      return "VOLTS"  # FORCE !b
    if k == "Light":            return "c"  # FORCE !b
    if k == "E=mc²":            return "J"  # FORCE !b
    if k == "Society":          return "HUMAN-ASPIRATIONS"  # FORCE !b
    if k == "Economics":          return "CONSUMER_DEMAND"  # FORCE !b
    if k == "Intelligence":          return "INTERACTION"#____!R   #FORCE !b
    if k == "Awareness":        return "A&I~6~" # FORCE !b

    if k == "Tholons P1":       return "NEGOTIATION"   # FORCE !b
    if k == "Tholons P2":       return "BALANCE"  # FORCE !b
    # if k == "Alternative Definitions":         return "PUSHING"  # FORCE 
    # if k == "Mental Physical Emotional": return "INSPIRATION"  # FORCE 
    # if k == "Tholons":          return "NEGOTIATION/BALANCE"  # FORCE 

def re_BODY(k): # concept name 
    # BODY is a collections of concepts that is treated as a single object !c
    if k == "Newton Org":       return "BODY"  # BODY 
    if k == "Numbers":          return "2x3=6"  # BODY 
    if k == "Cause Effect":     return "POINT-OF-EXCHANGE"  # BODY 
    if k == "Electricity":      return "CIRCUIT"  # BODY 
    if k == "Light":            return "PHOTON"  # BODY 
    if k == "E=mc²":            return "E=mc^2^"  # BODY 
    if k == "Society":          return "SOCIETY"  # BODY 
    if k == "Economics":        return "ECONOMICS"  # BODY
    if k == "Intelligence":     return "INTELLIGENCE"# # BODY
    if k == "Awareness":        return "INSTANCE~2x3=6~"# # BODY

    if k == "Tholons P1":       return "THOLON"   # BODY 
    if k == "Tholons P2":       return "THOLON"   # BODY 
    # if k == "Alternative Definitions":         return "INSTANCE"  # BODY 
    # if k == "Mental Physical Emotional": return "PERSON"  # BODY 
    # if k == "Tholons":          return "THOLON"  # BODY 
def re_POWER(k): # 18 !m
    # is the amount of energy transfered in a CONTEXTUAL INSTANCE during an interaction, the result of CAUSE and EFFECT  !c
    if k == "Newton Org":       return "POWER"  # POWER !m
    if k == "Alternative Definitions":         return "WORK_OR_ENERGY_TRANSFER"  # POWER !m
    if k == "Numbers":          return "18"  # POWER !m
    if k == "Electricity":      return "WATTS"  # POWER !m
    if k == "Light":            return "JOULES"  # POWER !m
    if k == "E=mc²":            return "E"  # POWER !m
    if k == "Society":          return "A-THRIVING-COMMUNITY"  # POWER !m
    if k == "Economics":          return "PROFIT_MARGIN"  # POWER !m
    if k == "Intelligence":          return "KNOWLEDGE"#   # POWER !m
    if k == "Awareness":        return "CONSCIOUSNESS~18~" # POWER !m

    if k == "Tholons P1":       return "ABILITY-TO-GENERATE"  # POWER !m
    if k == "Tholons P2":       return "ABILITY-TO-GENERATE"  # POWER !m
    # if k == "Cause Effect":     return "CHANGE-IN-LOCATION-PER-TIME"  # POWER 
    # if k == "Mental Physical Emotional": return "CREATION"  # POWER 
    # if k == "Tholons":          return "ABILITY-TO-GENERATE"  # POWER 

def re_CONTEXT(k): #
    # the conext of instantiation !c
    if k == "Newton Org":       return "3D spacetime"  # CONTEXT 
    if k == "Numbers":          return "MATH"  # CONTEXT 
    if k == "Cause Effect":     return "ENTANGLEMENT"  # CONTEXT 
    if k == "Electricity":      return "ELECTROMAGNETISM (spacetime)"  # CONTEXT 
    if k == "Light":            return "ENERGY (spacetime)"  # CONTEXT 
    if k == "E=mc²":            return "RELATIVITY (spacetime)"  # CONTEXT 
    if k == "Society":          return "Morphic/tholonic field?"  # CONTEXT 
    if k == "Economics":          return "ECONOMICS"   # CONTEXT 
    if k == "Intelligence":          return "INTELLIGENCE"# CONTEXT
    if k == "Awareness":        return "A&I" # CONTEXT

    if k == "Tholons P1":       return "THOLOGRAM"  # CONTEXT
    if k == "Tholons P2":       return "THOLOGRAM"  # CONTEXT 
    # if k == "Alternative Definitions":   return "3D spacetime"  # CONTEXT 
    # if k == "Mental Physical Emotional": return "INDIVIDUAL CONSCIOUSNESS?"  # CONTEXT 
    # if k == "Tholons":          return "THOLOGRAM"  # CONTEXT 

def re_SCOPE(k): #
    # the scope of the instatiated instance !c
    if k == "Newton Org":       return "SI Unit"  # SCOPE 
    if k == "Numbers":          return "NUMBERS"  # SCOPE 
    if k == "Cause Effect":     return "NORMALIZATION"  # SCOPE 
    if k == "Electricity":      return "SI Units"  # SCOPE 
    if k == "Light":            return "SI Units"  # SCOPE 
    if k == "E=mc²":            return "SI Units"  # SCOPE 
    if k == "Society":          return "?TBD (economics?, health?, growth?)"  # SCOPE 
    if k == "Economics":        return "BUDGET"  # SCOPE
    if k == "Intelligence":     return "???"# SCOPE
    if k == "Awareness":        return "???" # SCOPE

    if k == "Tholons P1":       return "THOLONICS (TBD)"  # SCOPE 
    if k == "Tholons P2":       return "THOLONICS (TBD)"  # SCOPE 
    # if k == "Alternative Definitions":         return "SI Units"  # SCOPE 
    # if k == "Mental Physical Emotional": return "?TBD (states of mental?, physcial?, emotional?)"  # SCOPE 
    # if k == "Tholons":          return "THOLONICS (TBD)"  # SCOPE 


# ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────── !Y


file = "n2l_RELATIONSHIPS.md"
with open(file,"r") as f:
    rlines = f.read()

allkeys = [
    'Newton Org',
    # 'Alternative Definitions',
    'Numbers',
    # 'Cause Effect',
    # 'Electricity',
    # 'Light',
    # 'E=mc²',
    # 'Society',
    # 'Economics',
    # 'Intelligence',
    # 'Awareness',
    # 'Mental Physical Emotional',
    # 'Tholons',
    # 'Tholons P1',
    # 'Tholons P2',
]

cdx = 0
reps = {}
# Create word replacement pairs for each concept group !g
for rkey in allkeys:
    file = "n2l_"+rkey.replace(" ","_")+".md"
    print(f"Opening: [{file}]")
    with open(file,"r") as f:
        lines = f.read()
    lines = lines + rlines
    # print(f"Building: {rkey}")
    cdx = (cdx + 1) % 5
    reps[rkey] = {
        # "Newtons 2nd Law":  c("[Newtons 2nd Law as a Tholonic rule]",cdx),
        "MASS":             c(re_MASS(rkey), cdx), # 2 !r
        "MOTION":           c(re_MOTION(rkey), cdx), # 3 !c
        "VELOCITY":         c(re_VELOCITY(rkey), cdx), # 3 !c
        "ACCELERATION":     c(re_ACCELERATION(rkey),cdx), # 3 !c
        "FORCE":            c(re_FORCE(rkey),cdx), # 6 !m
        "MOMENTUM":         c(re_MOMENTUM(rkey),cdx), # 3 !c
        "BODY":             c(re_BODY(rkey),cdx), # 18 !y
        "POWER":            c(re_POWER(rkey),cdx), # 18 !y
        "CONTEXT":          c(re_CONTEXT(rkey),cdx),
        "SKOPE":            c(re_SCOPE(rkey),cdx),
    }
    showidx(reps,rkey,lines)
# print(json.dumps(reps,indent=4))
# exit()

# showidx(reps,'Newton Org',lines)
# showidx(reps,'Alternative Definitions',lines)
#
# showidx(reps,'Numbers',lines)
# showidx(reps,'Cause Effect',lines)
#
# showidx(reps,'Electricity',lines)
# showidx(reps,'Light',lines)
# showidx(reps,'E=mc²',lines)
#
# showidx(reps,'Society',lines)
# showidx(reps,'Economics',lines)
# showidx(reps,'Mental Physical Emotional',lines)
#
# showidx(reps,'Tholons',lines)
# showidx(reps,'Tholons P1',lines)
# showidx(reps,'Tholons P2',lines)

