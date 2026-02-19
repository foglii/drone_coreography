import time

import numpy as np
import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
import sys
import uav_trajectory
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.mem import MemoryElement
from cflib.crazyflie.mem import Poly4D
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.utils import uri_helper

# Change uris and sequences according to your setup
# URIs in a swarm using the same radio must also be on the same channel
URI1 = 'radio://0/80/2M/E7E7E7E7E5'
URI2 = 'radio://0/80/2M/E7E7E7E7E7'
URI3 = 'radio://0/80/2M/E7E7E7E7E8'
URI4 = 'radio://0/80/2M/E7E7E7E7E9'
URI5 = 'radio://0/80/2M/E7E7E7E7E5'
URI6 = 'radio://0/80/2M/E7E7E7E7E4'


# drone1 = [list(map(float, row)) for row in __import__("csv").reader(open("drone1.csv", encoding="utf-8-sig"))]
# drone2 = [list(map(float, row)) for row in __import__("csv").reader(open("drone2.csv", encoding="utf-8-sig"))]
# drone3 = [list(map(float, row)) for row in __import__("csv").reader(open("drone3.csv", encoding="utf-8-sig"))]
# drone4 = [list(map(float, row)) for row in __import__("csv").reader(open("drone4.csv", encoding="utf-8-sig"))]
# drone5 = [list(map(float, row)) for row in __import__("csv").reader(open("drone5.csv", encoding="utf-8-sig"))]
# drone6 = [list(map(float, row)) for row in __import__("csv").reader(open("drone6.csv", encoding="utf-8-sig"))]
global iterr
iterr= 1
dronee1= uav_trajectory.Trajectory()
dronee1.loadcsv('drone1.csv')
dronee2= uav_trajectory.Trajectory()
dronee2.loadcsv('drone2.csv')
dronee3= uav_trajectory.Trajectory()
dronee3.loadcsv('drone3.csv')
dronee4= uav_trajectory.Trajectory()
dronee4.loadcsv('drone4.csv')
dronee5= uav_trajectory.Trajectory()
dronee5.loadcsv('drone5.csv')
dronee6= uav_trajectory.Trajectory()
dronee6.loadcsv('drone6.csv')
droneee1 = np.loadtxt('drone1.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone11=droneee1.tolist()
drone2 = np.loadtxt('drone2.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone2=np.asarray(drone2,dtype=float)
droneee3 = np.loadtxt('drone3.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone33=droneee3.tolist()
drone3=drone11[:len(drone33)//2]
drone3_2=drone11[len(drone33)//2+1:]
droneee4 = np.loadtxt('drone4.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone44=droneee4.tolist()
drone4=drone44[:len(drone44)//2]
drone4_2=drone44[len(drone44)//2+1:]
drone5 = np.loadtxt('drone5.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone6 = np.loadtxt('drone6.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone1=drone11[:len(drone11)//2]
drone1_2=drone11[len(drone11)//2:]
seq_args_ = {
    #URI1: [1,drone1],
   # URI2: [2,drone2],
    URI3: [3,drone3],
    URI4: [4,drone4],
    #URI5: [5,drone5],
    #URI6: [6,drone6],
    
}
seq_args_2 = {
     #URI1: [1,drone1_2],
     #URI2: [2,drone2_2],
     URI3: [3,drone3_2],
     URI4: [4,drone4_2],
    #URI5: [5,drone5],
    #URI6: [6,drone6],
    
}
seq_argss_ = {
    #URI1: [1,dronee1.duration/2],
     #URI2: [2,60],
    URI3: [3,dronee3.duration/2],
    URI4: [4,dronee4.duration/2],
    #URI5: [5,dronee5.duration],
    #URI6: [6,11.1],
    #URI7: [sequence7],
    #URI8: [sequence8],
    #URI9: [sequence9],
    #URI10: [sequence10],
}

# List of URIs, comment the one you do not want to fly
uris = {
   #URI1,
     #URI2,
    URI3,
     URI4,
   # URI5,
   # URI6,
   # URI7,
   # URI8,
   # URI9,
   # URI10
}

#######
def activate_mellinger_controller(scf):
    scf.cf.param.set_value('stabilizer.controller', '2')


def upload_trajectory(scf, trajectory_id, trajectory):
    """Upload one trajectory to one Crazyflie"""
    try:
        mems = scf.cf.mem.get_mems(MemoryElement.TYPE_TRAJ)
        if not mems:
            print(f"[{scf.cf.link_uri}] No trajectory memory found!")
            return
        trajectory_mem = mems[0]
        trajectory_mem.trajectory = []

        total_duration = 0
        for row in trajectory:
            duration = row[0]
            x = Poly4D.Poly(row[1:9])
            y = Poly4D.Poly(row[9:17])
            z = Poly4D.Poly(row[17:25])
            yaw = Poly4D.Poly(row[25:33])
            trajectory_mem.trajectory.append(Poly4D(duration, x, y, z, yaw))
            total_duration += duration

        if not trajectory_mem.write_data_sync():
            print(f"[{scf.cf.link_uri}] Upload failed.")
            print(trajectory)
            return

        scf.cf.high_level_commander.define_trajectory(trajectory_id, 0, len(trajectory))
        print(f"[{scf.cf.link_uri}] Trajectory uploaded ({len(trajectory)} segments, {total_duration:.1f}s)")
        print(total_duration)
        return total_duration

    except Exception as e:
        print(f"[{scf.cf.link_uri}] ERROR uploading trajectory: {e}")
        print(trajectory)
        

def landd(scf):
    commander = scf.cf.high_level_commander
    commander.land(0.0,4.0)
    time.sleep(4.0)
    commander.stop()
def run_trajectory(scf, trajectory_id, duration):
    try:
        print('run_trajectory function')
        """Execute a defined trajectory"""
        commander = scf.cf.high_level_commander
        if iterr==1:
            commander.takeoff(0.5, 2.0)
            time.sleep(3.0)
        commander.start_trajectory(trajectory_id, 1.5, False)
        print(f"[{scf.cf.link_uri}] Running trajectory {trajectory_id} for {duration:.1f}s")
        time.sleep(duration+1)
       
        if iterr==2:
                commander.land(0.0, 2.0)
                time.sleep(3.0)
                commander.stop()
        else: commander.up(0.2,0.1)
    except Exception as e:
        print(f"[{scf.cf.link_uri}] ERROR uploading trajectory: {e}")
        commander.land(0.0, 2.0)


def wait_for_param_download(scf):
    while not scf.cf.param.is_updated:
        time.sleep(0.5)
    print(f"[{scf.cf.link_uri}] Parameters ready")


def light_check(scf):
    scf.cf.param.set_value('led.bitmask', 255)
    time.sleep(1)
    scf.cf.param.set_value('led.bitmask', 0)


# --- Swarm execution ---
if __name__ == '__main__':
    cflib.crtp.init_drivers()

    factory = CachedCfFactory(rw_cache='./cache')

    with Swarm(uris, factory=factory) as swarm:
        try:
            swarm.parallel_safe(wait_for_param_download)
            swarm.parallel_safe(light_check)
            swarm.reset_estimators()
            swarm.parallel_safe(activate_mellinger_controller)

            # Upload trajectories to each Crazyflie
            durations = swarm.parallel_safe(upload_trajectory, args_dict=seq_args_)
           # durations=[30.3,30.3,30.3,30.3]
           # print("Durations:", durations)
              
            # Wait before flight
            time.sleep(3.0)

            # Run trajectories
            #run_args = {uri: [seq_args_[uri][0], durations[uri]] for uri in seq_args_}
            print("ciao0")
            swarm.parallel_safe(run_trajectory, args_dict=seq_argss_)
            print("ciao")
            iterr= iterr+1
            swarm.parallel_safe(wait_for_param_download)
            
            durations = swarm.parallel_safe(upload_trajectory, args_dict=seq_args_2)
            swarm.parallel_safe(run_trajectory, args_dict=seq_argss_)
        except KeyboardInterrupt:
            print("Emergency stop triggered by user.")
            swarm.parallel_safe(landd)
        except Exception as e:
            print(f"Errorr: {e}")
            swarm.parallel_safe(landd)

""" def activate_mellinger_controller(cf):
    cf.param.set_value('stabilizer.controller', '2')


def upload_trajectory(cf, trajectory_id, trajectory):
    try:
        print('hello')
        trajectory_mem = cf.cf.mem.get_mems(MemoryElement.TYPE_TRAJ)[0]
        trajectory_mem.trajectory = []

        total_duration = 0
        for row in trajectory:
            duration = row[0]
            x = Poly4D.Poly(row[1:9])
            y = Poly4D.Poly(row[9:17])
            z = Poly4D.Poly(row[17:25])
            yaw = Poly4D.Poly(row[25:33])
            trajectory_mem.trajectory.append(Poly4D(duration, x, y, z, yaw))
            total_duration += duration

        upload_result = trajectory_mem.write_data_sync()
        print('Uploaded')
        if not upload_result:
            print('Upload failed, aborting!')
            sys.exit(1)
        cf.cf.high_level_commander.define_trajectory(trajectory_id, 0, len(trajectory_mem.trajectory))
        print(total_duration)
        return total_duration
    except Exception as e:
        print(e)

#####
def activate_led_bit_mask(scf):
    scf.cf.param.set_value('led.bitmask', 255)

def deactivate_led_bit_mask(scf):
    scf.cf.param.set_value('led.bitmask', 0)

def light_check(scf):
    activate_led_bit_mask(scf)
    time.sleep(2)
    deactivate_led_bit_mask(scf)

def wait_for_param_download(scf):
    while not scf.cf.param.is_updated:
        time.sleep(1.0)
    print('Parameters downloaded for', scf.cf.link_uri)


def arm(scf):
    scf.cf.platform.send_arming_request(True)
    time.sleep(1.0)


def take_off(cf, position):
    take_off_time = 1.0
    sleep_time = 0.1
    steps = int(take_off_time / sleep_time)
    vz = position[2] / take_off_time

    print(vz)

    for i in range(steps):
        cf.commander.send_velocity_world_setpoint(0, 0, vz, 0)
        time.sleep(sleep_time)


def land(cf, position):
    landing_time = 1.0
    sleep_time = 0.1
    steps = int(landing_time / sleep_time)
    vz = -position[2] / landing_time

    print(vz)

    for _ in range(steps):
        cf.commander.send_velocity_world_setpoint(0, 0, vz, 0)
        time.sleep(sleep_time)

    cf.commander.send_stop_setpoint()
    # Hand control over to the high level commander to avoid timeout and locking of the Crazyflie
    cf.commander.send_notify_setpoint_stop()

    # Make sure that the last packet leaves before the link is closed
    # since the message queue is not flushed before closing
    time.sleep(0.1)


def run_sequence(scf, sequence):
    try:
        cf=scf.cf

        take_off(scf, sequence[0])
        for position in sequence:
            print('Setting position {}'.format(position))
            end_time = time.time() + position[3]
            while time.time() < end_time:
                cf.commander.send_position_setpoint(position[0],
                                                    position[1],
                                                    position[2], 0)
                time.sleep(0.1)
        land(scf, sequence[-1])
    except Exception as e:
        print(e)

def run_sequencee(scf, trajectory_id,figure8):
    try:
        print('run function')
        commander = scf.cf.high_level_commander
        relative_yaw=False
        print('second print')
        duration=21
        #duration = upload_trajectory(cf, trajectory_id, figure8)
        print(duration)
        print('The sequence is {:.1f} seconds long'.format(duration))
        # Arm the Crazyflie
        #cf.platform.send_arming_request(True)
        print('third print')
        time.sleep(1.0)

        takeoff_yaw = 3.14 / 2 if relative_yaw else 0.0
        commander.takeoff(0.5, 2.0, yaw=takeoff_yaw)
        time.sleep(3.0)
        commander.start_trajectory(trajectory_id, 1.0, True)
        time.sleep(duration)
        commander.land(0.0, 2.0)
        time.sleep(2)
        commander.stop()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    cflib.crtp.init_drivers()

    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        try:
            # If the copters are started in their correct positions this is
            # probably not needed. The Kalman filter will have time to converge
            # any way since it takes a while to start them all up and connect. We
            # keep the code here to illustrate how to do it.
            

            # The current values of all parameters are downloaded as a part of the
            # connections sequence. Since we have 10 copters this is clogging up
            # communication and we have to wait for it to finish before we start
            # flying.
            swarm.parallel_safe(light_check)

            durat=swarm.parallel_safe(upload_trajectory,args_dict=seq_args_)
            
            print(durat)
            #swarm.parallel(wait_for_param_download)
            time.sleep(5)

            swarm.reset_estimators()
        
        

            swarm.parallel_safe(activate_mellinger_controller)
            
            
        
            
            
            swarm.parallel_safe(arm)
            #swarm.parallel(run_sequence,args_dict=seq_args_)
            swarm.parallel_safe(run_sequencee,args_dict=seq_args_)

        # swarm.parallel(run_sequence, args_dict=seq_args)
        except Exception as e:
                print(f"Error occurred: {e}")
                swarm.parallel_safe(emergency_stop())


# --- Helper functions ---
 """
