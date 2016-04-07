#!/usr/bin/env python
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

import roslib; roslib.load_manifest('behavior_exploration2')
from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, Logger
from hector_flexbe_states.START_Exploration_Transform import START_Exploration_Transform
from hector_flexbe_states.Wait_Exploration import Wait_Exploration
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Jan 15 2016
@author: Elisa
'''
class Exploration2SM(Behavior):
	'''
	exploration nr.2
	'''


	def __init__(self):
		super(Exploration2SM, self).__init__()
		self.name = 'Exploration2'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:73 y:324
		_state_machine = OperatableStateMachine(outcomes=['finished'])
		_state_machine.userdata.goalId = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('StartExploration',
										START_Exploration_Transform(),
										transitions={'succeeded': 'Wait'},
										autonomy={'succeeded': Autonomy.Off},
										remapping={'goalId': 'goalId'})

			# x:455 y:40
			OperatableStateMachine.add('Wait',
										Wait_Exploration(),
										transitions={'restart': 'StartExploration', 'waiting': 'Wait'},
										autonomy={'restart': Autonomy.Off, 'waiting': Autonomy.Off},
										remapping={'goalId': 'goalId'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]