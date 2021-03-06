#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger

from flexbe_core.proxy import ProxySubscriberCached
from hector_worldmodel_msgs.msg import Object
from geometry_msgs.msg import PoseStamped
from rospy import Time


class Object_Detection(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(Object_Detection, self).__init__(outcomes = ['continue', 'found'], input_keys = ['pose'], output_keys = ['pose'])

		self._objectTopic = '/worldmodel/object'
		self._sub = ProxySubscriberCached({self._objectTopic: Object})


	def execute(self, userdata):
		# This method is called periodically while the state is active.
		# Main purpose is to check state conditions and trigger a corresponding outcome.
		# If no outcome is returned, the state will stay active.

		current_obj = self._sub.get_last_msg(self._objectTopic)
		if current_obj:
			if current_obj.info.class_id == 'victim' and current_obj.state.state == 2 and current_obj.info.object_id != 'victim_0':
				userdata.pose = PoseStamped()
				userdata.pose.pose = current_obj.pose.pose
				userdata.pose.header.stamp = Time.now()
				userdata.pose.header.frame_id = 'map'
				Logger.loginfo(current_obj.info.object_id)
				return 'found'
			
		

	def on_enter(self, userdata):
		# This method is called when the state becomes active, i.e. a transition from another state to this one is taken.
		# It is primarily used to start actions which are associated with this state.

		# The following code is just for illustrating how the behavior logger works.
		# Text logged by the behavior logger is sent to the operator and displayed in the GUI.

		pass

	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.

		pass # Nothing to do in this example.


	def on_start(self):
		# This method is called when the behavior is started.
		# If possible, it is generally better to initialize used resources in the constructor
		# because if anything failed, the behavior would not even be started.

		# In this example, we use this event to set the correct start time.
		pass

	def on_stop(self):
		# This method is called whenever the behavior stops execution, also if it is cancelled.
		# Use this event to clean up things like claimed resources.

		pass # Nothing to do in this example.
		
