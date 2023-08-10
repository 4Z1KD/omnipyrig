# omnipyrig

A package that allows the deveplopment of amateur radio applications using the amazing Omni-Rig library

# prerequisite
1. OmniRig (http://dxatlas.com/omnirig/)
2. python (https://www.python.org/downloads/)

# Installation
PyPi:<br>
https://pypi.org/project/omnipyrig/<br>
pip install omnipyrig


# usage
```

import omnipyrig

#create an instance
client = omnipyrig.OmniRigWrapper()

#print the current state
client.showParams()

#set the frequency of vfo A
client.setFrequency('A', 14230000)

```

# how it works? 
the package uses win32com to dispatch omnirig object<br/>
it then wrap it's properties and methods<br/>

# constants & methods

## constants:</br>
***mode enumeration***
- MODE_SSB_L
- MODE_SSB_U
- MODE_CW_U
- MODE_FM
- MODE_AM
- MODE_RTTY_L
- MODE_CW_L
- MODE_DATA_L
- MODE_RTTY_U
- MODE_DATA_FM
- MODE_FM_N
- MODE_DATA_U
- MODE_AM_N
- MODE_PSK
- MODE_DATA_FM_N

***rit/xit***
- RIT_ON
- RIT_OFF
- XIT_ON
- XIT_OFF

***split***
- SPLIT_ON
- SPLIT_OFF

***vfo***
- VFO_AA
- VFO_AB
- VFO_BB
- VFO_BA

## methods:
- client.showParams()
- client.setFrequency(vfo_selector, frequency)
- client.setMode(mode)
- client.setRit(state)
- client.setXit(state)
- client.setRitOffset(offset)
- client.setSplit(state)
- client.setPitch(pitch)
- client.setVfoA()
- client.setVfoB()
- client.setVfoAB()
- client.setVfoBA()


73,<br/>
Gil 4Z1KD
