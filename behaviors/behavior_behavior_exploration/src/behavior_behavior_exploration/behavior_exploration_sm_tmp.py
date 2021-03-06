#!/usr/bin/env python
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

import roslib; roslib.load_manifest('behavior_behavior_exploration')
from flexbe_core import Behavior, Autonomy, OperatableStateMachine, Logger
from hector_flexbe_states.Error_Exploration import Error_Exploration
from hector_flexbe_states.Wait_Exploration import Wait_Exploration
from hector_flexbe_states.START_Exploration_Transform import START_Exploration_Transform
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Nov 19 2015
@author: Elisa und Gabriel
'''
class behavior_explorationSM(Behavior):
	'''
	first try
	'''


	def __init__(self):
		super(behavior_explorationSM, self).__init__()
		self.name = 'behavior_exploration'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:322, x:130 y:322
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:143 y:40
			OperatableStateMachine.add('START',
										START_Exploration_Transform(target_time=3),
										transitions={'succeeded': 'Wait'},
										autonomy={'succeeded': Autonomy.Off})

			# x:506 y:47
			OperatableStateMachine.add('Wait',
										Wait_Exploration(target_time=3),
										transitions={'waiting': 'Wait', 'succeeded': 'Error', 'aborted': 'Error'},
										autonomy={'waiting': Autonomy.Off, 'succeeded': Autonomy.Off, 'aborted': Autonomy.Off})

			# x:200 y:200
			OperatableStateMachine.add('Error',
										Error_Exploration(),
										transitions={'restart': 'START'},
										autonomy={'restart': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
