class poker():
    def __init__(self,name:str):
        self.flower = name[0]
        self.number = name[1]
        
    def __gt__(self,other):
        # Spad,Heart,Diamond,Club,先比花色再比数字
        sort_order = {'s':3,'h':2,'d':1,'c':0}
        if sort_order[self.flower] > sort_order[other.flower]:
            return 1
        elif self.flower == other.flower:
            return self.number > other.number
        else:
            return 0
