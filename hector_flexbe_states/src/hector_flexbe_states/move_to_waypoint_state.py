#!/usr/bin/env python

import rospy
from flexbe_core import EventState, Logger

from flexbe_core.proxy import ProxyActionClient

from hector_move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

'''
Created on 15.06.2015

@author: Philipp Schillinger
'''

class MoveToWaypointState(EventState):
	'''
	Lets the robot move to a given waypoint.

	># waypoint		PoseStamped		Specifies the waypoint to which the robot should move.

	<= reached 						Robot is now located at the specified waypoint.
	<= failed 						Failed to send a motion request to the action server.

	'''

	def __init__(self):
		'''
		Constructor
		'''
		super(MoveToWaypointState, self).__init__(outcomes=['reached', 'failed'],
											input_keys=['waypoint'])
		
		self._action_topic = '/move_base'
		self._client = ProxyActionClient({self._action_topic: MoveBaseAction})

		self._failed = False
		self._reached = False
		
		
	def execute(self, userdata):
		'''
		Execute this state
		'''
		if self._failed:
			return 'failed'
		if self._reached:
			return 'reached'

		if self._client.has_result(self._action_topic):
			result = self._client.get_result(self._action_topic)
			if result.result == 1:
				self._reached = True
				return 'reached'
			else:
				self._failed = True
				Logger.logwarn('Failed to reach waypoint!')
				return 'failed'

			
	def on_enter(self, userdata):
		self._failed = False
		self._reached = False

		action_goal = MoveBaseGoal()
		action_goal.target_pose = userdata.waypoint
		if action_goal.target_pose.header.frame_id == "":
			action_goal.target_pose.header.frame_id = "world"

		try:
			self._client.send_goal(self._action_topic, action_goal)
		except Exception as e:
			Logger.logwarn('Failed to send motion request to waypoint (%(x).3f, %(y).3f):\n%(err)s' % {
				'err': str(e),
				'x': userdata.waypoint.pose.position.x,
				'y': userdata.waypoint.pose.position.y
			})
			self._failed = True
		
		Logger.loginfo('Driving to next waypoint')
			

	def on_stop(self):
		try:
			if self._client.is_available(self._action_topic) \
			and not self._client.has_result(self._action_topic):
				self._client.cancel(self._action_topic)
		except:
			# client already closed
			pass

	def on_pause(self):
		self._client.cancel(self._action_topic)

	def on_resume(self, userdata):
		self.on_enter(userdata)
