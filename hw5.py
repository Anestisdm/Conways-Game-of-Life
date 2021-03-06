from clock import *

#-------------------- Askisi 1 ----------------------------
class RomanCascadeCounter(CascadeCounter):
    """Metritis CascadeCounter me endei3eis me rwmaikous ari8mous."""
    def __str__(self):
        tens = self.value // 10
        units = self.value % 10
        tens_s = 'L' if tens == 5 else tens*'X'
        if units < 5:
            units_s = units*'I'
        else:
            units_s = 'V' + (units-5)*'I'

        sz = len(tens_s + units_s)
        return '-'*(9-sz) + tens_s + units_s


class RomanClock(Clock):
    """Roloi me endei3eis me rwmaika noumera.

    >>> c = RomanClock(23, 59, 58)
    >>> str(c)
    '----XXIII:---LVIIII:----LVIII'
    >>> c.advance()
    >>> print(c)
    ----XXIII:---LVIIII:---LVIIII
    >>> c.advance()
    >>> print(c)
    ---------:---------:---------
    >>> c.advance()
    >>> print(c)
    ---------:---------:--------I
    >>> c.advance()
    >>> print(c)
    ---------:---------:-------II
    """
    def __init__(self, h, m, s):
        self._h = RomanCascadeCounter(None, 24, h)
        self._m = RomanCascadeCounter(self._h, 60, m)
        self._s = RomanCascadeCounter(self._m, 60, s)
    

#-------------------- Askisi 2 ----------------------------
class DayCounter(CyclicCounter):
    """Metritis hmeras.

    Paradeigmata:
    >>> d = DayCounter()
    >>> str(d)
    'Sunday'
    >>> d.advance()
    >>> print(d)
    Monday
    >>> d2 = DayCounter('Saturday')
    >>> str(d2)
    'Saturday'
    >>> d2.advance()
    >>> str(d2)
    'Sunday'
    >>> d2.advance()
    >>> str(d2)
    'Monday'
    """
    _days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',\
            'Thursday', 'Friday', 'Saturday']
    def __init__(self, day = 'Sunday'):
        CyclicCounter.__init__(self, 7, DayCounter._days.index(day)+1)

    def __str__(self):
        return DayCounter._days[self.value-1]


#-------------------- Askisi 3 ----------------------------
class DayClock(Clock):
    """Roloi me endei3h hmeras.

    >>> c = DayClock(23, 59, 58, 'Sunday')
    >>> str(c)
    '23:59:58 Sunday'
    >>> c.advance()
    >>> str(c)
    '23:59:59 Sunday'
    >>> c.advance()
    >>> str(c)
    '00:00:00 Monday'
    >>> c.advance()
    >>> str(c)
    '00:00:01 Monday'

    An paralhf8ei to onoma imeras (teleytaio orisma ston kataskeyasti)
    tote pairnei timi 'Sunday', px.:
    >>> c = DayClock(6, 35, 0)
    >>> print(c)
    06:35:00 Sunday
    """
    def __init__(self, h = 0, m = 0, s = 0, day = 'Sunday'):
        self._d = DayCounter(day)
        self._h = CascadeCounter(self._d, 24, h)
        self._m = CascadeCounter(self._h, 60, m)
        self._s = CascadeCounter(self._m, 60, s)

    def __str__(self):
        return '{0}:{1}:{2} {3}'.format(self._h, self._m, self._s, self._d)



#-------------------- Askisi 4 ----------------------------
class Timer(Counter):
    """Antistrofos xronometritis.

    >>> c = Timer(0, 0, 2)
    >>> str(c)
    '00:00:02'
    >>> c.advance()
    >>> str(c)
    '00:00:01'
    >>> c.advance()
    >>> str(c)
    '00:00:00'
    >>> c.advance()
    >>> str(c)
    'TI DI DI DI'
    >>> c.advance()
    >>> str(c)
    'TI DI DI DI'
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    def __init__(self, h, m, s):
        self._h = CascadeCounter1(None, 24, 'h', h)
        self._m = CascadeCounter1(self._h, 60, 'm', m)
        self._s = CascadeCounter1(self._m, 60, 's', s)
       
    def advance(self):
        self._s.advance()
        
    def __str__(self):
        if self._h.value>=0 or self._m.value>=0 or self._s.value>=0:
            return '{0}:{1}:{2}'.format(self._h, self._m, self._s)
        else:
            return 'TI DI DI DI'
            
            
class CyclicCounter1(Counter):
    def __init__(self,period,start = 0):
        
        self.period = period
        Counter.__init__(self,start)
    
    def advance(self):
        self.value = (self.value - 1) % self.period
        
    def __str__(self):
        s = Counter.__str__(self)
        return (len(str(self.period-1))-len(s))*'0' + s
        
        
class CascadeCounter1(CyclicCounter1):
    def __init__(self, next, period, t, start = 0):
    
        CyclicCounter1.__init__(self,period,start)
        self.next = next
        self.t = t
        
    def advance(self):
        if self.t == 's':
            if self.next.next.value>0 or self.next.value>0 or self.value>0:
                CyclicCounter1.advance(self)
            else:
                self.next.next.value=-1
                self.next.value=-1
                self.value=-1
        else:
            CyclicCounter1.advance(self)
        if self.next and self.value == 59:
            self.next.advance()