# omnipyrig

A package that allows the deveplopment of amateur radio applications using the amazing Omni-Rig library

# prerequisite
1. OmniRig (http://dxatlas.com/omnirig/)
2. python (https://www.python.org/downloads/)

# installation
PyPi:<br>
https://pypi.org/project/omnipyrig/<br>
pip install omnipyrig<br>
<br>
if you need to update:<br>
pip install omnipyrig -U<br>

# usage
```python
import omnipyrig

#create a new instance
OmniClient = omnipyrig.OmniRigWrapper()

#set the active rig to 1 (as defined in OmniRig GUI)
OmniClient.setActiveRig(1)
RigType = OmniClient.getParam("RigType")
print(f'Rig 1: {RigType}')

#set the active rig to 2 (as defined in OmniRig GUI)
OmniClient.setActiveRig(2)
RigType = OmniClient.getParam("RigType")
print(f'Rig 2: {RigType}')

#There are 2 ways to send set commands
#1. using the explicit methods
#2. using the generic set method, passing a 2-Letter identifier and a value

#set the frequency of VFO A to 14.255MHz using the explicit setFrequency(...) method
OmniClient.setFrequency("A",14255000)

#set the mode to USB using the explicit setMode(...) method
OmniClient.setMode(OmniClient.MODE_SSB_U)

#set frequency of VFO B to 7.130MHz using the generic set method
OmniClient.set("FB07130000")

#here is the full list of methods:

#setFrequency(vfo_selector, frequency)
#setMode(mode)
#setRit(state)
#setXit(state)
#setRitOffset(offset)
#setSplit(state)
#setPitch(pitch)
#setVfoA()
#setVfoB()
#setVfoAB()
#setVfoBA()
#setActiveRig(index)

#get and print some parameters from the radio
StatusStr = OmniClient.getParam("StatusStr")
print(StatusStr)
ClearRit = OmniClient.getParam("ClearRit")
print(ClearRit)
Freq = OmniClient.getParam("Freq")
print(Freq)
FreqA = OmniClient.getParam("FreqA")
print(FreqA)
FreqB = OmniClient.getParam("FreqB")
print(FreqB)
FrequencyOfTone = OmniClient.getParam("FrequencyOfTone")
print(FrequencyOfTone)
GetRxFrequency = OmniClient.getParam("GetRxFrequency")
print(GetRxFrequency)
GetTxFrequency = OmniClient.getParam("GetTxFrequency")
print(GetTxFrequency)
IsParamReadable = OmniClient.getParam("IsParamReadable")
print(IsParamReadable)
Mode = OmniClient.getParam("Mode")
print(Mode)
Pitch = OmniClient.getParam("Pitch")
print(Pitch)
cts,dsr,dtr,rts = OmniClient.getParam("PortBits")
print(f'{cts},{dsr},{dtr},{rts}')
ReadableParams = OmniClient.getParam("ReadableParams")
print(ReadableParams)
RigType = OmniClient.getParam("RigType")
print(RigType)
Rit = OmniClient.getParam("Rit")
print(Rit)
RitOffset = OmniClient.getParam("RitOffset")
print(RitOffset)
Split = OmniClient.getParam("Split")
print(Split)
Status = OmniClient.getParam("Status")
print(Status)
Tx = OmniClient.getParam("Tx")
print(Tx)
Vfo = OmniClient.getParam("Vfo")
print(Vfo)
WriteableParams = OmniClient.getParam("WriteableParams")
print(WriteableParams)
Xit = OmniClient.getParam("Xit")
print(Xit)
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
- showParams()
- setFrequency(vfo_selector, frequency)
- setMode(mode)
- setRit(state)
- setXit(state)
- setRitOffset(offset)
- setSplit(state)
- setPitch(pitch)
- setVfoA()
- setVfoB()
- setVfoAB()
- setVfoBA()


73,<br/>
Gil 4Z1KD
