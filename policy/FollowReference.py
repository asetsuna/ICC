import sys
from TrackingController import TrackingController
import argparse
import os
from IPython import embed

if __name__=="__main__":
	tracking_controller = TrackingController()
	tracking_controller.initialize(configuration_filepath="")
	tracking_controller.followReference()