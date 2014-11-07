
# Domestic Security System
----------------------------------------------

## About ##
The Domestic Security System takes advantage of all the diverse features that this robot has. Using the myro robot, we aim to build a domestic security management tool. While the owners of the home are asleep, the always-on robot can sense change in the lighting of the room. A timer will then be activated, if it is not turned off by entering in a pre-set security code, the robot will start beeping and take pictures.

## Features Used ##
 - Brightness Sensors
 - IR Sensors

## Functions ##
 - Start and End time Function
 - Check Time function
 - Check change of light 
 - Send security code to Smartphone
 - Use IR Sensors to check if security code is correct


## Part 1 ##
Security system
 - Security system goes off with change of light
 - Timer starts going off
 - Person has (5s) time to input the security code.

## Part 2 ##
Security code
 - As soon as the time goes off the person’s smartphone gets a notification
 - Colours/ patterns get sent to the phone and 
 - Have to show the colour to the sensor to turn it off
 - Repeat 3 times with different patterns
 - Or have sheets of colours on the robot 

## Part 3 ##
If no input , calls a security number 
 - Sends a message to a phone 

## How to get Photos Working ##
Will most likely give error: "IOError: decoder jpeg not available"

#### How to Solve: ####
 - Follow second answer at [a link](http://stackoverflow.com/questions/8404956/installing-pil-with-jpeg-support-on-mac-os-x)
 - ???
 - Profit
