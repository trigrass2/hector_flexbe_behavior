#!/usr/bin/env python
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

import roslib; roslib.load_manifest('behavior_simplemission')
from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from behavior_simplemissioninitialize.simplemissioninitialize_sm import SimpleMissionInitializeSM
from hector_flexbe_states.MarkPoint import MarkPoint
from hector_flexbe_states.Mapping import Mapping
from behavior_simplemissiondoaction.simplemissiondoaction_sm import SimpleMissionDoActionSM
from flexbe_states.wait_state import WaitState
from behavior_simplemissiondriveto.simplemissiondriveto_sm import SimpleMissionDriveToSM
from behavior_simplemissionerror.simplemissionerror_sm import SimpleMissionErrorSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]
from geometry_msgs.msg import PoseStamped
# [/MANUAL_IMPORT]


'''
Created on Thu Jun 02 2016
@author: Gabriel
'''
class SimpleMissionSM(Behavior):
	'''
	Simple mission structure
	'''


	def __init__(self):
		super(SimpleMissionSM, self).__init__()
		self.name = 'SimpleMission'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(SimpleMissionInitializeSM, 'SimpleMissionInitialize')
		self.add_behavior(SimpleMissionDoActionSM, 'SimpleMissionDoAction')
		self.add_behavior(SimpleMissionDriveToSM, 'DriveToEnd')
		self.add_behavior(SimpleMissionDriveToSM, 'DriveToStart')
		self.add_behavior(SimpleMissionErrorSM, 'SimpleMissionError')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:52 y:481, x:134 y:482
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.pose = PoseStamped()
		_state_machine.userdata.startPoint = PoseStamped()
		_state_machine.userdata.endPoint = PoseStamped()
		_state_machine.userdata.switchFalse = False

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:31 y:51
			OperatableStateMachine.add('SimpleMissionInitialize',
										self.use_behavior(SimpleMissionInitializeSM, 'SimpleMissionInitialize'),
										transitions={'finished': 'Operator_Drive', 'failed': 'Operator_Drive'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'startPoint': 'startPoint'})

			# x:496 y:56
			OperatableStateMachine.add('Endpoint',
										MarkPoint(),
										transitions={'succeeded': 'DeactivateMapping'},
										autonomy={'succeeded': Autonomy.Off},
										remapping={'pose': 'endPoint'})

			# x:672 y:55
			OperatableStateMachine.add('DeactivateMapping',
										Mapping(),
										transitions={'succeeded': 'SimpleMissionDoAction'},
										autonomy={'succeeded': Autonomy.Off},
										remapping={'switch': 'switchFalse'})

			# x:673 y:234
			OperatableStateMachine.add('SimpleMissionDoAction',
										self.use_behavior(SimpleMissionDoActionSM, 'SimpleMissionDoAction'),
										transitions={'finished': 'DriveToStart', 'failed': 'SimpleMissionError'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:291 y:56
			OperatableStateMachine.add('Operator_Drive',
										WaitState(wait_time=5),
										transitions={'done': 'Endpoint'},
										autonomy={'done': Autonomy.High})

			# x:432 y:122
			OperatableStateMachine.add('DriveToEnd',
										self.use_behavior(SimpleMissionDriveToSM, 'DriveToEnd'),
										transitions={'finished': 'SimpleMissionDoAction', 'failed': 'SimpleMissionError'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'pose': 'endPoint'})

			# x:221 y:236
			OperatableStateMachine.add('DriveToStart',
										self.use_behavior(SimpleMissionDriveToSM, 'DriveToStart'),
										transitions={'finished': 'DriveToEnd', 'failed': 'SimpleMissionError'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'pose': 'startPoint'})

			# x:440 y:412
			OperatableStateMachine.add('SimpleMissionError',
										self.use_behavior(SimpleMissionErrorSM, 'SimpleMissionError'),
										transitions={'failed': 'failed', 'toStart': 'DriveToStart', 'toEnd': 'DriveToEnd'},
										autonomy={'failed': Autonomy.Inherit, 'toStart': Autonomy.Inherit, 'toEnd': Autonomy.Inherit},
										remapping={'startPoint': 'startPoint', 'endPoint': 'endPoint'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
