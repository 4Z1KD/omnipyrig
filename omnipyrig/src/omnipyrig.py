import win32com.client
import time

class OmniRigWrapper():
    #properties
    is_debug = False
    _omnirig = None
    _rig = None
    _rig1 = None
    _rig2 = None
    _timeout = 0.5

    #on/off enumeration
    OFF = 0
    ON = 1

    #mode enumeration
    MODE_SSB_L = 1
    MODE_SSB_U = 2
    MODE_CW_U = 3
    MODE_FM = 4
    MODE_AM = 5
    MODE_RTTY_L = 6
    MODE_CW_L = 7
    MODE_DATA_L = 8
    MODE_RTTY_U = 9
    MODE_DATA_FM = 10
    MODE_FM_N = 11
    MODE_DATA_U = 12
    MODE_AM_N = 13
    MODE_PSK = 14
    MODE_DATA_FM_N = 15
    
    #mode values
    SSB_L = 0x04000000
    SSB_U = 0x02000000
    CW_U = 0x00800000
    FM = 0x40000000
    AM = 0x20000000
    CW_L = 0x01000000
    DATA_L = 0x10000000
    DATA_U = 0x08000000

    #rit/xit
    RIT_ON = 0x00020000
    RIT_OFF = 0x00040000
    XIT_ON = 0x00080000
    XIT_OFF = 0x00100000

    #split
    SPLIT_ON = 0x00008000
    SPLIT_OFF = 0x00010000

    #vfo
    VFO_AA = 128
    VFO_AB = 256
    VFO_BB = 512
    VFO_BA = 1024
    

    #c'tor
    def __init__(self):
        # create an instance of the service
        #self._omnirig = win32com.client.gencache.EnsureDispatch("Omnirig.OmnirigX")
        self._omnirig = win32com.client.Dispatch("Omnirig.OmnirigX")

        #set default Rig
        self._rig = self._rig1 = self._omnirig.Rig1
        self._rig2 = self._omnirig.Rig2

        #set a delay
        time.sleep(self._timeout)

############################### setters #########################        
        
    def setFrequency(self, vfo_selector, frequency):
        time.sleep(self._timeout)
        if (frequency):
            if vfo_selector.upper() == 'A':
                self._rig.FreqA = frequency
            elif vfo_selector.upper() == 'B':
                self._rig.FreqB = frequency
    
    def setMode(self, mode):
        time.sleep(self._timeout)
        mode = self.safe_int(mode)
        if (mode):
            if mode == self.MODE_CW_L:
                self._rig.Mode = self.CW_L
            elif mode == self.MODE_CW_U:
                self._rig.Mode = self.CW_U
            elif mode == self.MODE_SSB_L:
                self._rig.Mode = self.SSB_L
            elif mode == self.MODE_SSB_U:
                self._rig.Mode = self.SSB_U
            elif mode == self.MODE_DATA_L:
                self._rig.Mode = self.DATA_L
            elif mode == self.MODE_DATA_U:
                self._rig.Mode = self.DATA_U
            elif mode == self.MODE_FM:
                self._rig.Mode = self.FM
            elif mode == self.MODE_AM:
                self._rig.Mode = self.AM
                
    def setRit(self,state):
        time.sleep(self._timeout)
        state = self.safe_int(state)
        if (state):
            if state == self.ON:
                self._rig.Rit = self.RIT_ON
            if state == self.OFF:
                self._rig.Rit = self.RIT_OFF

    def setXit(self,state):
        time.sleep(self._timeout)
        state = self.safe_int(state)
        if (state):
            if state == self.ON:
                self._rig.Xit = self.XIT_ON
            if state == self.OFF:
                self._rig.Xit = self.XIT_OFF

    def setRitOffset(self, offset):
        time.sleep(self._timeout)
        offset = self.safe_int(offset)
        if (offset):
            self._rig.ClearRit()
            self._rig.RitOffset = offset
    
    def setSplit(self,state):
        time.sleep(self._timeout)
        state = self.safe_int(state)
        if (state):
            if state == self.ON:
                #self._rig.SetSplitMode()
                self._rig.Split = self.SPLIT_ON
            if state == self.OFF:
                #self._rig.SetSimplexMode()
                self._rig.Split = self.SPLIT_OFF

    def setPitch(self, pitch):
        time.sleep(self._timeout)
        pitch = self.safe_int(pitch)
        if (pitch):
            pitch = int(pitch/10)
            pitch = int(pitch*10)
            self._rig.Pitch = pitch

    def setVfoA(self):
        time.sleep(self._timeout)
        self._rig.Vfo = self.VFO_AA
    
    def setVfoB(self):
        time.sleep(self._timeout)
        self._rig.Vfo = self.VFO_BB
    
    def setVfoAB(self):
        time.sleep(self._timeout)
        self._rig.Vfo = self.VFO_AB
    
    def setVfoBA(self):
        time.sleep(self._timeout)
        self._rig.Vfo = self.VFO_BA

    def setActiveRig(self, index):
        time.sleep(self._timeout)
        index = self.safe_int(index)
        if (index):
            if index == 1:
                self._rig = self._rig1
            elif index == 2:
                self._rig = self._rig2
    
############################ helpers ##############################
    def parseCommand(self, command_string):
        cmd, val = self.split_string(command_string)
        if cmd and val:
            cmd = cmd.upper()
            if cmd == 'FA':
                self.setFrequency('A', val)
            elif cmd == 'FB':
                self.setFrequency('B', val)
            elif cmd == 'MD':
                self.setMode(val)
            elif cmd == 'RT':
                self.setRit(val)
            elif cmd == 'XT':
                self.setXit(val)
            elif cmd == 'RU':
                self.setRitOffset(val)
            elif cmd == 'KP':
                self.setPitch(val)
            elif cmd == 'AA':
                self.setVfoA()
            elif cmd == 'BB':
                self.setVfoB()
            elif cmd == 'AB':
                self.setVfoAB()
            elif cmd == 'BA':
                self.setVfoBA()
            else:
                return #raise ValueError("Invalid operator")
    
    def split_string(self, s):
        s = s.strip()
        if len(s) >= 2:
            first_two_letters = s[:2]
            rest_of_string = s[2:]
            return first_two_letters, rest_of_string
        else:
            return s, ""
    
    def showParams(self):
        print(dir(self._rig))
        time.sleep(self._timeout)

    def getParam(self, param):
        time.sleep(self._timeout)
        if param =='Freq': return self._rig.Freq
        elif param =='FreqA': return self._rig.FreqA
        elif param =='FreqB': return self._rig.FreqB
        elif param =='FrequencyOfTone': return self._rig.FrequencyOfTone(0)
        elif param =='GetRxFrequency': return self._rig.GetRxFrequency()
        elif param =='GetTxFrequency': return self._rig.GetTxFrequency()
        elif param =='Mode': return hex(self._rig.Mode)
        elif param =='Pitch': return self._rig.Pitch
        elif param =='PortBits': return self._rig.PortBits.Cts, self._rig.PortBits.Dsr,self._rig.PortBits.Dtr,self._rig.PortBits.Rts
        elif param =='ReadableParams': return self._rig.ReadableParams
        elif param =='RigType': return self._rig.RigType
        elif param =='Rit': return self._rig.Rit
        elif param =='RitOffset': return self._rig.RitOffset
        elif param =='Split': return self._rig.Split
        elif param =='Status': return self._rig.Status
        elif param =='StatusStr': return self._rig.StatusStr
        elif param =='Tx': return self._rig.Tx
        elif param =='Vfo': return self._rig.Vfo
        elif param =='WriteableParams': return self._rig.WriteableParams
        elif param =='Xit': return self._rig.Xit
        time.sleep(self._timeout)

    def safe_int(self, input_data):
        if isinstance(input_data, str):
            try:
                return int(input_data.replace(".", ""))  # Remove decimal point
            except ValueError:
                return None  # Return None if the string cannot be converted
        elif isinstance(input_data, (int, float)):
            if isinstance(input_data, float):
                input_data = str(input_data).replace(".", "")  # Remove decimal point
            return int(input_data)
        else:
            return None  # Return None for other types
        
############################ main #######################################
if __name__ == "__main__":
    client = OmniRigWrapper()
    
    client.setActiveRig(2)
    client.setFrequency("A",14255000)

    StatusStr = client.getParam("StatusStr")
    print(StatusStr)
    ClearRit = client.getParam("ClearRit")
    print(ClearRit)
    Freq = client.getParam("Freq")
    print(Freq)
    FreqA = client.getParam("FreqA")
    print(FreqA)
    FreqB = client.getParam("FreqB")
    print(FreqB)
    FrequencyOfTone = client.getParam("FrequencyOfTone")
    print(FrequencyOfTone)
    GetRxFrequency = client.getParam("GetRxFrequency")
    print(GetRxFrequency)
    GetTxFrequency = client.getParam("GetTxFrequency")
    print(GetTxFrequency)
    IsParamReadable = client.getParam("IsParamReadable")
    print(IsParamReadable)
    Mode = client.getParam("Mode")
    print(Mode)
    Pitch = client.getParam("Pitch")
    print(Pitch)
    cts,dsr,dtr,rts = client.getParam("PortBits")
    print(f'{cts},{dsr},{dtr},{rts}')
    ReadableParams = client.getParam("ReadableParams")
    print(ReadableParams)
    RigType = client.getParam("RigType")
    print(RigType)
    Rit = client.getParam("Rit")
    print(Rit)
    RitOffset = client.getParam("RitOffset")
    print(RitOffset)
    Split = client.getParam("Split")
    print(Split)
    Status = client.getParam("Status")
    print(Status)
    Tx = client.getParam("Tx")
    print(Tx)
    Vfo = client.getParam("Vfo")
    print(Vfo)
    WriteableParams = client.getParam("WriteableParams")
    print(WriteableParams)
    Xit = client.getParam("Xit")
    print(Xit)