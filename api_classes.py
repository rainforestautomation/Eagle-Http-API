from lxml import etree
from lxml import objectify



class MessageCluster():
    def __init__(self, xml_tree,block_string):
        self.block_string = block_string
        for element in xml_tree.iterchildren():
            setattr(self, element.tag, element.text)
    def __repr__(self):
        return  self.xml_tree
        
        
class TimeCluster():
    def __init__(self, xml_tree,block_string):
        self.block_string = block_string
        for element in xml_tree.iterchildren():
            setattr(self, element.tag, element.text)
    def __repr__(self):
        return self.block_string
    
class InstantaneousDemand():
    def __init__(self, xml_tree,block_string):
        self.block_string = block_string
        for element in xml_tree.iterchildren():
            setattr(self, element.tag, element.text)
    
class NetworkInfo():
    def __init__(self, xml_tree,block_string):
        self.block_string = block_string
        self.xml_tree = xml_tree
        for element in xml_tree.iterchildren():
            setattr(self, element.tag, element.text)
    def __repr__(self):
        return self.block_string
    
class PriceCluster():
    def __init__(self, xml_tree,block_string):
        self.block_string = block_string
        for element in xml_tree.iterchildren():
            setattr(self, element.tag, element.text)
    def __repr__(self):
        return self.block_string
    
class DeviceInfo():
    def __init__(self, xml_tree,block_string):
        self.block_string = block_string
        for element in xml_tree.iterchildren():
            setattr(self, element.tag, element.text)
    def __repr__(self):
        return self.block_string
    
class CurrentSummationDelivered():
    def __init__(self, xml_tree,block_string):
        self.block_string = block_string
        for element in xml_tree.iterchildren():
            setattr(self, element.tag, element.text)
    def __repr__(self):
        return self.block_string
    
class ScheduleInfo():
    def __init__(self, xml_tree,block_string):
        self.block_string = block_string
        for element in xml_tree.iterchildren():
            setattr(self, element.tag, element.text)
    def __repr__(self):
        return self.block_string
    
class BlockPriceDetail():
    def __init__(self, xml_tree,block_string):
        self.block_string = block_string
        for element in xml_tree.iterchildren():
            setattr(self, element.tag, element.text)
    def __repr__(self):
        return self.block_string
class HistoryData():
    def __init__(self, xml_tree,block_string):
        self.block_string = block_string
        for element in xml_tree.iterchildren():
            setattr(self, element.tag, element.text)
    def __repr__(self):
        return self.block_string
        