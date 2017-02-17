#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file KDistance.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist
import random


def rand():
	return random.randint(0,10)

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
kdistance_spec = ["implementation_id", "KDistance", 
		 "type_name",         "KDistance", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "VenderName", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class KDistance
# @brief ModuleDescription
# 
# 
class KDistance(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		#distance_arg = [None] * ((len(RTC._d_TimedFloat) - 4) / 2)
		#self._d_distance = RTC.TimedFloat(*distance_arg)
		self._d_distance = RTC.TimedFloat(RTC.Time(0,0),0)
		"""
		"""
		self._DistanceIn = OpenRTM_aist.InPort("Distance", self._d_distance)
		#vel2d_arg = [None] * ((len(RTC._d_TimedVelocity2D) - 4) / 2)
		#self._d_vel2d = RTC.TimedVelocity2D(*vel2d_arg)
		self._d_vel2d = RTC.TimedVelocity2D(RTC.Time(0,0),RTC.Velocity2D(0.0, 0.0, 0.0))
		"""
		"""
		self._VelocityOut = OpenRTM_aist.OutPort("Velocity", self._d_vel2d)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addInPort("Distance",self._DistanceIn)
		
		# Set OutPort buffers
		self.addOutPort("Velocity",self._VelocityOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The activated action (Active state entry action)
	#	# former rtc_active_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	# 
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onActivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
		#preparation
		vx = 0.0
		vy = 0.0
		va = 0.0

		if(self._DistanceIn.isNew()):
			
			self._d_distance = self._DistanceIn.read()
			
			if(self._d_distance.data < 30):
				
				self._d_vel2d.data.va = 0.0;
				self._d_vel2d.data.vx = 0.0;
				self._d_vel2d.data.vy = 0.0;	
				self._VelocityOut.write()
				
				time.sleep(2.0)
				
				if(rand() >=5):
					for i in range(0,150):
						self._d_vel2d.data.va = 1.0
						self._VelocityOut.write()
					time.sleep(2.0)
					
				else:
					for i in range(0,150):
						self._d_vel2d.data.va = -1.0
						self._VelocityOut.write()
					time.sleep(2.0)

    					
		else:
			va = 0.0
			vx = 0.2
			vy = 0.0
			
			
			self._d_vel2d.data.va = va
			self._d_vel2d.data.vx = -vx
			self._d_vel2d.data.vy = vy
			self._VelocityOut.write() 
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def KDistanceInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=kdistance_spec)
    manager.registerFactory(profile,
                            KDistance,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    KDistanceInit(manager)

    # Create a component
    comp = manager.createComponent("KDistance")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

