#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger


class execute_turn(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(execute_turn, self).__init__(outcomes = ['succeeded', 'aborted', 'done'])


	def execute(self, userdata):
		return 'done'
	
		

	def on_enter(self, userdata):
		pass

	
	def on_exit(self, userdata):
	

		pass # Nothing to do in this example.


	def on_start(self):
		pass


	def on_stop(self):
		

		pass # Nothing to do in this example.
		
