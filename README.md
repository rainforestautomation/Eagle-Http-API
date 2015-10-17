2015-04-20  Chrome Browser Extension Released!

![alt tag](https://lh3.googleusercontent.com/-BGEkB6ghmKoZfKBUjj_i0jpYQEoeYy_ApB4Yoweeg5hbkTGdC0ZxznTYkgiMCyse4Bd8cLOow=s640-h400-e365)

A new chrome extension has been released which allows you to view your energy usage by simply looking at an icon in your browser. To tryi it out, go here:

https://chrome.google.com/webstore/detail/rainforest-automation-eag/jogodcnmpmgfihdjebbnbmpcmolipioi


# EAGLE-HTTP-API

The Rainforest Automation Eagle is a energy monitoring unit which allows you to monitor your home's power condumption in real time by connecting to your smart meter through Zigbee.

You can purchase an Eagle through the Amazon store (please ensure your house is connected with a smart meter and your utility support HAN registration).
http://www.amazon.com/Rainforest-EAGLE-Ethernet-ZigBee-Gateway/dp/B00AII248U

This API is a Python library which allows you to easily query and configure your device through a HTTP relay server with the credentials you create at rainforestcloud.com

Example usage:

    > python
    > from eagle_http import *
    > eagle = eagle_http('your user name', 'your password', 'your cloud_id')
    > eagle.get_instantaneous_demand()
    https://rainforestcloud.com:9445/cgi-bin/post_manager
    <Command>
      <Name>get_instantaneous_demand</Name>
    </Command>
    
    <InstantaneousDemand>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <MeterMacId>0x000781000081fd17</MeterMacId>
      <TimeStamp>0x1c91ec39</TimeStamp>
      <Demand>0x0003b0</Demand>
      <Multiplier>0x00000001</Multiplier>
      <Divisor>0x000003e8</Divisor>
      <DigitsRight>0x03</DigitsRight>
      <DigitsLeft>0x06</DigitsLeft>
      <SuppressLeadingZero>Y</SuppressLeadingZero>
    </InstantaneousDemand>
    

The returned XML is parsed and placed into the instance as a attribute:

    > eagle.InstantaneousDemand
    <InstantaneousDemand>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <MeterMacId>0x000781000081fd17</MeterMacId>
      <TimeStamp>0x1c91ec39</TimeStamp>
      <Demand>0x0003b0</Demand>
      <Multiplier>0x00000001</Multiplier>
      <Divisor>0x000003e8</Divisor>
      <DigitsRight>0x03</DigitsRight>
      <DigitsLeft>0x06</DigitsLeft>
      <SuppressLeadingZero>Y</SuppressLeadingZero>
    </InstantaneousDemand>
    

Individual attributes of the reponse can also easily be accessed:

    > eagle.InstantaneousDemand.Demand
    0x0003b0

Just as easy as that.
# Prerequisites 

In order to use this API you need:

* A Rainforest Automation Eagle running 2.20 or greater firmware
* An account from https://www.rainforestcloud.com with the target eagle added
* A computer with Python installed

# Installation

Installation is straight forward, and the preqreqs are lxml and requests

    > git clone https://github.com/rainforestautomation/Eagle-Http-API.git
    > cd ./Eagle-Http-API
    > pip install -r requirements.txt

Good to go!


#List Of Commands:

* eagle = eagle_http('your user name', 'your password', 'your cloud_id')

Instantiates the eagle_http object (fill in your details)

* eagle.get_network_info([mac_id])
    * mac_id - (Optional) is intended for eagles with multiple zigbee radios 
    
Returns network info details of eagle.

    <NetworkInfo>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <InstallCode>0x94496e6dcf06b7d1</InstallCode>
      <LinkKeyHigh>0x4aecc18d050a0527</LinkKeyHigh>
      <LinkKeyLow>0x2b8caac18554435f</LinkKeyLow>
      <FWVersion>1.4.48 (6952)</FWVersion>
      <HWVersion>1.2.5</HWVersion>
      <Manufacturer>Rainforest Automation, Inc.</Manufacturer>
      <ModelId>Z109-EAGLE</ModelId>
      <DateCode>2014051823520701</DateCode>
      <ImageType>0x1301</ImageType>
      <Protocol>Zigbee</Protocol>
    </NetworkInfo>

json:

    {
    "NetworkInfo": {
    "DeviceMacId": "0xd8d5b90000002aeb",
    "InstallCode": "0x94496e6dcf06b7d1",
    "LinkKeyHigh": "0x4aecc18d050a0527",
    "LinkKeyLow": "0x2b8caac18554435f",
    "FWVersion": "1.4.48 (6952)",
    "HWVersion": "1.2.5",
    "Manufacturer": "Rainforest Automation, Inc.",
    "ModelId": "Z109-EAGLE",
    "DateCode": "2014051823520701",
    "ImageType": "0x1301",
    "Protocol": "Zigbee"}
    }

You can access the returned data attributes like so:

    > eagle.NetworkInfo.Status
    Connected

* eagle.get_network_status([mac_id])
    * mac_id - (Optional) is intended for eagles with multiple zigbee radios 

Returns network Status of Eagle

    <NetworkInfo>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <Status>Connected</Status>
      <CoordMacId>0x000781000081fd17</CoordMacId>
      <ExtPanId>0x000781000081fd17</ExtPanId>
      <ShortAddr>0x8644</ShortAddr>
      <Channel>18</Channel>
      <LinkStrength>0x64</LinkStrength>
      <Protocol>Zigbee</Protocol>
    </NetworkInfo>   

json:

    {
    "NetworkInfo": {
    "DeviceMacId": "0xd8d5b90000002aeb",
    "Status": "Connected",
    "CoordMacId": "0x000781000081fd17",
    "ExtPanId": "0x000781000081fd17",
    "ShortAddr": "0x8644",
    "Channel": "18",
    "LinkStrength": "0x64",
    "Protocol": "Zigbee"}
    } 

Which can be accessed like:

    >eagle.NetworkInfo.Status
    Connected

* eagle.get_instantaneous_demand([mac_id])
    * mac_id - (Optional) is intended for eagles with multiple zigbee radios 

Returns instantaneous demand from eagle

    <InstantaneousDemand>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <MeterMacId>0x000781000081fd17</MeterMacId>
      <TimeStamp>0x1c91ec39</TimeStamp>
      <Demand>0x0003b0</Demand>
      <Multiplier>0x00000001</Multiplier>
      <Divisor>0x000003e8</Divisor>
      <DigitsRight>0x03</DigitsRight>
      <DigitsLeft>0x06</DigitsLeft>
      <SuppressLeadingZero>Y</SuppressLeadingZero>
    </InstantaneousDemand>

json:

    {
    "InstantaneousDemand": {
    "DeviceMacId": "0xd8d5b90000002aeb",
    "MeterMacId": "0x000781000081fd17",
    "TimeStamp": "0x1c9347b8",
    "Demand": "0x0003b0",
    "Multiplier": "0x00000001",
    "Divisor": "0x000003e8",
    "DigitsRight": "0x03",
    "DigitsLeft": "0x06",
    "SuppressLeadingZero": "Y"}
    }

Which can be accessed like:

    >eagle.InstantaneousDemand.Demand
    0x0003b0

* eagle.get_price([mac_id])
    * mac_id - (Optional) is intended for eagles with multiple zigbee radios 
    
Returns price cluster from Eagle:

    <PriceCluster>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <MeterMacId>0x000781000081fd17</MeterMacId>
      <TimeStamp>0x1c91ec36</TimeStamp>
      <StartTime>0x1c91ec3e</StartTime>
      <Duration>0xffff</Duration>
      <Price>0x0000000a</Price>
      <Currency>0x03d2</Currency>
      <TrailingDigits>0x02</TrailingDigits>
      <Tier>1</Tier>
      <RateLabel>Price1</RateLabel>
    </PriceCluster> 

json:

    {
    "PriceCluster": {
    "DeviceMacId": "0xd8d5b90000002aeb",
    "MeterMacId": "0x000781000081fd17",
    "TimeStamp": "0x1c9347ab",
    "StartTime": "0x1c9347bb",
    "Duration": "0xffff",
    "Price": "0x0000000a",
    "Currency": "0x03d2",
    "TrailingDigits": "0x02",
    "Tier": "1",
    "RateLabel": "Price1"}
    }
    


Which can be accessed like:

    >eagle.PriceCluster.Price
    0x0000000a

* eagle.get_message([mac_id])
    * * mac_id - (Optional) is intended for eagles with multiple zigbee radios 
    
Returns message cluster from Eagle:

    <MessageCluster>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <MeterMacId>0x000781000081fd17</MeterMacId>
      <TimeStamp>0x00000000</TimeStamp>
      <StartTime>0x00000000</StartTime>
      <Duration>0x0000</Duration>
      <Id>0x00000000</Id>
      <ConfirmationRequired>N</ConfirmationRequired>
      <Confirmed>N</Confirmed>
      <Read>Y</Read>
      <Queue>active</Queue>
    </MessageCluster>

Which can be accessed like:

    >eagle.MessageCluster.TimeStamp
    0x00000000

* eagle.confirm_message(message_id, [mac_id])
    * message_id - 0x00-0xff message id number (stringified)
    * mac_id - (Optional) is intended for eagles with multiple zigbee radios 
    
Returns message cluster from Eagle:

    <MessageCluster>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <MeterMacId>0x000781000081fd17</MeterMacId>
      <TimeStamp>0x00000000</TimeStamp>
      <StartTime>0x00000000</StartTime>
      <Duration>0x0000</Duration>
      <Id>0x00000000</Id>
      <ConfirmationRequired>N</ConfirmationRequired>
      <Confirmed>N</Confirmed>
      <Read>Y</Read>
      <Queue>active</Queue>
    </MessageCluster>
    

json:

    {
    "MessageCluster": {
    "DeviceMacId": "0xd8d5b90000002aeb",
    "MeterMacId": "0x000781000081fd17",
    "TimeStamp": "0x00000000",
    "StartTime": "0x00000000",
    "Duration": "0x0000",
    "Id": "0x00000000",
    "ConfirmationRequired": "N",
    "Confirmed": "N",
    "Read": "Y",
    "Queue": "active"}
    }
Which can be accessed like:

    >eagle.MessageCluster.TimeStamp
    0x00000000


* eagle.get_history_data(start_time,[end_time, mac_id)
    * start_time - 0x00000000 - current time (zigbee time, seconds from Jan 1, 2000 UTC)
    * end_time - 0x00000000 - current time (zigbee time, seconds from Jan 1, 2000 UTC)
    * mac_id - (Optional) is intended for eagles with multiple zigbee radios 

Not currently working

eagle.set_schedule('demand', '0x000a', 'Y')

* eagle.set_schedule(event,frequency, enabled, [mac_id])
    * event - how often eagle queries for one of : demand, summation,message,scheduled_prices, price, billing_period,block_period,profile_data 
    * frequency - 0x0000- 0xffff time in seconds for a query
    * enabled - Y or N - whether query is enabled
    * mac_id - (Optional) is intended for eagles with multiple zigbee radios 
    
No response will come back.
    
* eagle.get_schedule(event,frequency, enabled, [mac_id])
    * event - how often eagle queries for one of : demand, summation,message,scheduled_prices, price, billing_period,block_period,profile_data
    * mac_id - (Optional) is intended for eagles with multiple zigbee radios 

Returns ScheduleInfo from Eagle:

    <ScheduleInfo>
      <DeviceMacId>0x0000000000000000</DeviceMacId>
      <MeterMacId>0x0000000000000000</MeterMacId>
      <Event>demand</Event>
      <Frequency>10</Frequency>
    </ScheduleInfo>
    
json:

    {
    "ScheduleInfo": {
    "DeviceMacId": "0x0000000000000000",
    "MeterMacId": "0x0000000000000000",
    "Event": "demand",
    "Frequency": "10"}
    }

Which can be accessed like:

    >eagle.ScheduleInfo.Frequency
    10

## Getting Raw XML Data

This api was designed so you do not need to directly access the xml or json data, but can access instance variables instead. If you would like direct access to XML fragments returned from the HTTP API, you can simply:

* Ensure instance.json = False
* Make a request
* Read the Instance object directly

Example:

    > instance.get_network_info()
    > instance.NetworkInfo
    <NetworkInfo>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <InstallCode>0x94496e6dcf06b7d1</InstallCode>
      <LinkKeyHigh>0x4aecc18d050a0527</LinkKeyHigh>
      <LinkKeyLow>0x2b8caac18554435f</LinkKeyLow>
      <FWVersion>1.4.48 (6952)</FWVersion>
      <HWVersion>1.2.5</HWVersion>
      <Manufacturer>Rainforest Automation, Inc.</Manufacturer>
      <ModelId>Z109-EAGLE</ModelId>
      <DateCode>2014051823520701</DateCode>
      <ImageType>0x1301</ImageType>
      <Protocol>Zigbee</Protocol>
    </NetworkInfo>

## Getting Raw JSON Data

Similarly, and most usefully for most pythonistas, to get the raw data in JSON you would:

* Ensure instance.json = True
* Make a request
* Read the Instance object directly

Example:

    > instance.json = True
    > instance.get_network_info()
    {
    "NetworkInfo": {
    "DeviceMacId": "0xd8d5b90000002aeb",
    "Status": "Connected",
    "CoordMacId": "0x000781000081fd17",
    "ExtPanId": "0x000781000081fd17",
    "ShortAddr": "0x8644",
    "Channel": "18",
    "LinkStrength": "0x64",
    "Protocol": "Zigbee"}
    }
 

##Telling the API to Quiet down
The Eagle-Http-API is by default pretty noisy on the command line.  To quiet it down:

    eagle.noisy = False

The eagle-http object also keeps track of the send/receive history in found in eagle.history list

Objects look like this:

    history_obj = {
        'time':str(datetime.datetime.now()),
        'command':self.command_name.text,
        'sent_xml':sent_xml,
        'recv_xml':recv_xml,
        'obj':return_obj
    }
    

You can access the returned objects like so:

    > eagle.history[0]['command']
    get_network_info
    

If you are using this tool interactively, you can use:

    eagle.readback(1)
    
    Item Number: 8
    Datetime: 2015-03-10 10:56:28.858187
    Command Sent: get_network_info
    SENT XML --------------------------
    <Command>
      <Name>get_network_info</Name>
    </Command>
    
    RECEIVED XML-----------------------
    <NetworkInfo>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <InstallCode>0x94496e6dcf06b7d1</InstallCode>
      <LinkKeyHigh>0x4aecc18d050a0527</LinkKeyHigh>
      <LinkKeyLow>0x2b8caac18554435f</LinkKeyLow>
      <FWVersion>1.4.48 (6952)</FWVersion>
      <HWVersion>1.2.5</HWVersion>
      <Manufacturer>Rainforest Automation, Inc.</Manufacturer>
      <ModelId>Z109-EAGLE</ModelId>
      <DateCode>2014051823520701</DateCode>
      <ImageType>0x1301</ImageType>
      <Protocol>Zigbee</Protocol>
    </NetworkInfo>
    
    <NetworkInfo>
      <DeviceMacId>0xd8d5b90000002aeb</DeviceMacId>
      <Status>Connected</Status>
      <CoordMacId>0x000781000081fd17</CoordMacId>
      <ExtPanId>0x000781000081fd17</ExtPanId>
      <ShortAddr>0x8644</ShortAddr>
      <Channel>18</Channel>
      <LinkStrength>0x64</LinkStrength>
      <Protocol>Zigbee</Protocol>
    </NetworkInfo>
    

Where the arg is a integer, and will pretty print the outgoing request and response

# Commit Details

- March 11th 2015 (1.1)  -  Added Support for JSON, 
                            Adhered to DRY wrt api_classes (now using aliases)
                            Updated documentarion to reflect JSON changes

- March 10th, 2015 (1.0)  - Initial Commit


# Issues

The maintainer of this repo can be contacted at john dot lee at rainforestautomation dot com. Feel free to create issues if the api does something unexpected
