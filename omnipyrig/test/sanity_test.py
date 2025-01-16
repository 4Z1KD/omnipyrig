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

#There are 3 ways to send set commands
#1. using the explicit methods
#2. using the semi-generic set method, passing a 2-Letter identifier and a value
#3. using the generic setCustomCommand method, passing the command string

#set the frequency of VFO A to 14.255MHz using the explicit setFrequency(...) method
OmniClient.setFrequency("A",14255000)

#set the mode to USB using the explicit setMode(...) method
OmniClient.setMode(OmniClient.MODE_SSB_U)

#set frequency of VFO B to 7.130MHz using the semi-generic set method
OmniClient.set("FB07130000")

#set frequency of VFO A to 18.110MHz using the generic set method
OmniClient.setCustomCommand("FA018110000;", 0, 0)

#here is the full list of explicit set methods:
'''
setFrequency(vfo_selector, frequency)
setMode(mode)
setRit(state)
setXit(state)
setRitOffset(offset)
setSplit(state)
setPitch(pitch)
setVfoA()
setVfoB()
setVfoAB()
setVfoBA()
setActiveRig(index)
'''

#here is the full list of 2-Letters command identifiers for the generic set command:
'''
'FA########' - sets frequency to VFO A (# is the frequency in Hz)
'FB########' - sets frequency to VFO B (# is the frequency in Hz)
'MD##' - sets the mode (# is value of the mode identifier [not to confuse with the mode enum])
'RT##' - sets the Rit (# is value of the rit enum)
'XT##' - sets the Xit (# is value of the xit enum)
'RU####' - set the Rit Offset (# is frequency offset in Hz)
'KP####' - set the Pitch (# is frequency offset in Hz)
'AA' - set the VFO to A
'BB' - set the VFO to B
'AB' - set the Reciever to VFOA and transmitter to VFOB
'BA' - set the Reciever to VFOB and transmitter to VFOA
'''

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