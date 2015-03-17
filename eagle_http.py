#!/usr/bin/env python 
from lxml import etree
from lxml import objectify
import requests, copy 
from api_classes import *
import datetime


class eagle_http():
    host_local = 'https://192.168.100.169'
    host = 'https://rainforestcloud.com'
    port = 9445
    rurl = '/cgi-bin/post_manager'
    history = []
    #XML Fragment constructs
    command_root= etree.Element('Command')
    command_name= etree.Element('Name')
    mac_id = etree.Element('DeviceMacId')
    msg_id = etree.Element('Id')
    format_ = etree.Element('Format')
    history_start_time = etree.Element('StartTime')
    history_end_time = etree.Element('EndTime')
    history_frequency = etree.Element('Frequency')
    schedule_event = etree.Element('Event')
    schedule_frequency = etree.Element('Frequency')
    schedule_enabled = etree.Element('Enabled')
    target = etree.Element('Target')
    #command list
    cmd_get_network_info ="get_network_info"
    cmd_get_network_status = "get_network_status"
    cmd_get_instantaneous_demand = "get_instantaneous_demand"
    cmd_get_price = "get_price"
    cmd_get_message = "get_message"
    cmd_confirm_message = "confirm_message"
    cmd_get_current_summation = "get_current_summation"
    cmd_get_history_data = "get_history_data"
    cmd_set_schedule = "set_schedule"
    cmd_get_schedule = "get_schedule"
    noisy = True
    json = False
    
    def __init__(self, uname, password, cloud_id):
        self.user_name = uname
        self.user_password = password
        self.cloud_id = cloud_id
        self.construct_headers(self.cloud_id, self.user_name, self.user_password)
    def construct_headers(self,cloud_id, user_name, password_):
        self.headers = {
            'Cloud-ID': str(cloud_id),
            'User':str(user_name),
            'Password':str(password_)
        }
        return self.headers
    def send(self,send_data,request_headers):
        requests.packages.urllib3.disable_warnings()
        self.final_url =self.host+":"+str(self.port)+self.rurl
        try:
            self.req = requests.post(self.final_url, data = send_data, headers = request_headers, verify =False)
            if self.noisy:
                print self.final_url
                print send_data
                print self.req.text
            if self.json:
                returned_object =self.parse_json_response(self.req.text)
            else:
                returned_object =self.parse_xml_response(self.req.text)
            self.write_history(send_data,self.req.text,returned_object)
        except Exception as e:
            print "Exception raised: "+str(e)
    def parse_xml_response(self, text):
        try:
            self.xmlTree =objectify.fromstring(text)
            module = __import__('api_classes')
            #print self.xmlTree.tag
            class_ = getattr(module, self.xmlTree.tag)
            instance = class_(self.json,self.xmlTree, text)
            setattr(self, self.xmlTree.tag, instance)
            return instance
        except:
            raise
    def parse_json_response(self, text):
        module = __import__('api_classes')
        json_obj = json.loads(text)
        class_ = ""
        for key in json_obj:
            class_ = getattr(module, key)
            instance = class_(self.json,json_obj, text)
            print instance
            setattr(self, key, instance)
            return instance
    def write_history(self,sent, received, return_obj):
        history_obj = {
            'time':str(datetime.datetime.now()),
            'command':self.command_name.text,
            'sent':sent,
            'received':received,
            'object':return_obj
        }
        self.history.append(history_obj)
    def readback(self, readback_count =100):
        i = 0
        for item in reversed(self.history):
            print "Item Number: "+str(i)
            print "Datetime: "+str(item['time'])
            print "Command Sent: "+str(item['command'])
            print "SENT  --------------------------"
            print str(item['sent'])
            print "RECEIVED -----------------------"
            print str(item['received'])
            if i > readback_count:
                break
            i= i+1
    def compose_root(self, command, mac_id):
        command_base = copy.copy(self.command_root)
        self.command_name.text = command
        command_base.append(self.command_name)
        if mac_id is not None:
            self.mac_id.text = mac_id
            command_base.append(self.mac_id)
        if self.json == True:
            print "json"
            self.format_.text = 'JSON'
            command_base.append(self.format_)
        return command_base
    def get_network_info(self, mac_id= None):
        self.command = self.compose_root(self.cmd_get_network_info, mac_id)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers)
    def get_network_status(self,mac_id =None):
        self.command = self.compose_root(self.cmd_get_network_status, mac_id)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers)
    def get_instantaneous_demand(self, mac_id = None):
        self.command = self.compose_root(self.cmd_get_instantaneous_demand, mac_id)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers)
    def get_price(self,mac_id = None):
        self.command = self.compose_root(self.cmd_get_price, mac_id)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers)
    def get_message(self, mac_id = None):
        self.command = self.compose_root(self.cmd_get_message, mac_id)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers)
    def confirm_message(self, message_id, mac_id =None):
        self.command = self.compose_root(self.cmd_confirm_message, mac_id)
        self.msg_id.text = message_id
        self.command.append(self.msg_id)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers)
    def get_current_summation(self, mac_id = None):
        self.command = self.compose_root(self.cmd_get_current_summation, mac_id)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers)
    def get_history_data(self,start_time, end_time=None,frequency =None,mac_id= None):
        self.command = self.compose_root(self.cmd_get_history_data, mac_id)
        self.command.append(self.history_start_time)
        self.history_start_time.text = start_time
        if end_time is not None:
            self.history_end_time.text = end_time
            self.command.append(self.history_end_time)
        if frequency is not None:
            self.history_frequency.text = frequency
            self.command.append(self.history_frequency)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers)
    def set_schedule(self,event,frequency, enabled, mac_id =None):
        #event could be demand, summation,message,scheduled_prices, price, billing_period,block_period,profile_data
        self.command = self.compose_root(self.cmd_set_schedule, mac_id)
        self.command.append(self.history_start_time)
        self.schedule_event.text = event
        self.schedule_frequency.text= frequency
        self.schedule_enabled.text = enabled
        self.command.append(self.schedule_event)
        self.command.append(self.schedule_frequency)
        self.command.append(self.schedule_enabled)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers)
    def get_schedule(self, event, mac_id = None):
        self.command = self.compose_root(self.cmd_get_schedule, mac_id)
        self.schedule_event.text = event
        self.command.append(self.schedule_event)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers) 
    def reboot(self, target, mac_id=None):
        self.command = self.compose_root(self.cmd_get_network_info, mac_id)
        self.target.text = target
        self.command.append(self.target)
        self.xml_fragment =etree.tostring(self.command, pretty_print=True)
        self.send(self.xml_fragment, self.headers)
        
        
        
if __name__ == '__main__':
    instance = eagle_http('user_email', 'password', 'cloud_id')
    instance.get_network_info()
    instance.get_network_status()
    instance.get_instantaneous_demand()
    instance.get_price()
    instance.get_message()
    instance.confirm_message('0xFF')
    instance.get_history_data('0x1c91d800','0x1c91d87d')
    instance.set_schedule('demand', '0x000a', 'Y')
    instance.get_schedule('demand')
    instance.json = True
    instance.get_network_info()
    instance.get_network_status()
    instance.get_instantaneous_demand()
    instance.get_price()
    instance.get_message()
    instance.confirm_message('0xFF')
    instance.get_history_data('0x1c91d800','0x1c91d87d')
    instance.set_schedule('demand', '0x000a', 'Y')
    instance.get_schedule('demand')
    instance.readback(100)
    print instance.NetworkInfo
    print instance.NetworkInfo.DeviceMacId
    print instance.history[0]['command']
