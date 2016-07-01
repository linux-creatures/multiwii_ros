#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example Python node to publish on a specific topic.
"""

# Import required Python code.
import rospy

# Give ourselves the ability to run a dynamic reconfigure server.
from dynamic_reconfigure.server import Server as DynamicReconfigureServer

# Import custom message data and dynamic reconfigure variables.
from multiwii_ros.msg import nav_data
from multiwii_ros.cfg import nodeExampleConfig as ConfigType

class NodeExample(object):
    '''
    Node example class.
    '''
    def __init__(self):
        # Get the private namespace parameters from command line or launch file.
        init_message = rospy.get_param('~message', 'hello')
        rate = float(rospy.get_param('~rate', '1.0'))
        rospy.loginfo('rate = %d', rate)
        # Create a dynamic reconfigure server.
        self.server = DynamicReconfigureServer(ConfigType, self.reconfigure_cb)
        # Create a publisher for our custom message.
        self.pub = rospy.Publisher('example', nav_data, queue_size=10)
        # Initialize message variables.
        self.int_a = 1
        self.int_b = 2
        self.message = init_message

        # Create a timer to go to a callback. This is more accurate than
        # sleeping for a specified time.
        rospy.Timer(rospy.Duration(1 / rate), self.timer_cb)

        # Allow ROS to go to all callbacks.
        rospy.spin()

    def timer_cb(self, _event):
        """
        Called at a specified interval. Publishes message.
        """
        # Set the message to publish as our custom message.
        msg = nav_data()
        # Fill in custom message variables with values updated from dynamic
        # reconfigure server.
        msg.message = self.message
        msg.batteryPercent = 
        msg.state = 
        msg.magX = self.message
        msg.magY = 
        msg.magZ = 
        msg.pressure = self.message
        msg.temp = 
        msg.rotX = 
        msg.rotX = self.message
        msg.rotX = 
        msg.altd = 
        msg.vx = self.message
        msg.vx = 
        msg.vx = 
        msg.ax = self.message
        msg.ax = 
        msg.ax =
        msg.motor1 = 
        msg.motor2 =
        msg.motor3 = 
        msg.motor4 =
        
        # Publish our custom message.
        self.pub.publish(msg)

    def reconfigure_cb(self, config, dummy):
        '''
        Create a callback function for the dynamic reconfigure server.
        '''
        # Fill in local variables with values received from dynamic reconfigure
        # clients (typically the GUI).
        self.message = config["message"]
        self.int_a = config["a"]
        self.int_b = config["b"]
        # Return the new variables.
        return config

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('pytalker')
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        NodeExample()
    except rospy.ROSInterruptException:
        pass
