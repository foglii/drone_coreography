
import logging
import sys
import time
from threading import Event

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import PositionHlCommander
from cflib.utils import uri_helper

URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

DEFAULT_HEIGHT = 0.5
BOX_LIMIT = 0.5

deck_attached_event = Event()

logging.basicConfig(level=logging.ERROR)

position_estimate = [0, 0]


import time
from cflib.crazyflie.high_level_commander import PositionHlCommander

BOX_LIMIT = 0.5  # Set to your desired bounding box in meters
DEFAULT_HEIGHT = 0.5

# position_estimate must be updated externally, e.g., via Crazyflie callbacks or estimator

def move_box_limit(scf, position_estimate):
    with PositionHlCommander(scf, default_z=DEFAULT_HEIGHT, controller=PositionHlCommander.CONTROLLER_MELLINGER) as pc:
        print("Started PositionHlCommander control")

        pc.takeoff(DEFAULT_HEIGHT, 2.0)
        time.sleep(3)

        while True:
            target_x = position_estimate[0]
            target_y = position_estimate[1]

            # Invert direction when reaching box limits
            if position_estimate[0] > BOX_LIMIT:
                target_x = BOX_LIMIT - 0.1
            elif position_estimate[0] < -BOX_LIMIT:
                target_x = -BOX_LIMIT + 0.1

            if position_estimate[1] > BOX_LIMIT:
                target_y = BOX_LIMIT - 0.1
            elif position_estimate[1] < -BOX_LIMIT:
                target_y = -BOX_LIMIT + 0.1

            # Go to new target position
            pc.go_to(target_x, target_y, DEFAULT_HEIGHT, 0.0)
            time.sleep(0.5)  # Tune this for responsiveness

        # Not reached normally, but you could add landing logic on interrupt
         pc.land(0.0, 2.0)
         time.sleep(3)



def move_linear_simple(scf):
    with PositionHlCommander(scf, default_z=DEFAULT_HEIGHT, controller=PositionHlCommander.CONTROLLER_MELLINGER) as pc:
        time.sleep(1)
        # Take off
        pc.takeoff(DEFAULT_HEIGHT, 2.0)
        time.sleep(3)

        # Move forward (along +Y axis, 0.5m)
        pc.go_to(0, 0.5, DEFAULT_HEIGHT, 0)
        time.sleep(2)

        # Turn left 180 degrees
        pc.go_to(0, 0.5, DEFAULT_HEIGHT, 180)
        time.sleep(2)

        # Move forward again (which is now in the -Y direction due to the yaw)
        pc.go_to(0, 0.0, DEFAULT_HEIGHT, 180)
        time.sleep(2)


def take_off_simple(scf):
     with PositionHlCommander(scf, default_z=DEFAULT_HEIGHT, controller=PositionHlCommander.CONTROLLER_MELLINGER) as pc:
        time.sleep(3)
        pc.takeoff(0.5, 2.0)
        time.sleep(1)


def log_pos_callback(timestamp, data, logconf):
    print(data)
    position_estimate[0] = data['stateEstimate.x']
    position_estimate[1] = data['stateEstimate.y']


def param_deck_flow(_, value_str):
    value = int(value_str)
    print(value)
    if value:
        deck_attached_event.set()
        print('Deck is attached!')
    else:
        print('Deck is NOT attached!')


if __name__ == '__main__':
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        scf.cf.param.add_update_callback(group='deck', name='bcLighthouse4',
                                         cb=param_deck_flow)
        time.sleep(1)

        logconf = LogConfig(name='Position', period_in_ms=10)
        logconf.add_variable('stateEstimate.x', 'float')
        logconf.add_variable('stateEstimate.y', 'float')
        scf.cf.log.add_config(logconf)
        logconf.data_received_cb.add_callback(log_pos_callback)

        if not deck_attached_event.wait(timeout=5):
            print('No flow deck detected!')
            sys.exit(1)

        # Arm the Crazyflie
        scf.cf.platform.send_arming_request(True)
        time.sleep(1.0)

        logconf.start()

        #take_off_simple(scf)
        move_linear_simple(scf)
        # move_box_limit(scf)
        logconf.stop()
