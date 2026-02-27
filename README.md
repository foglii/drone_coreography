# drone_coreography
This project consists in the developing of a 6 drones choreography using Crazyflies equipped with LightHouse positioning decks.
## Requirements
- 6 Crazyflie drones by Bitcraze equipped with Lighthouse decks.
- Crazyradio PA
- Indoor flight space of at least 2mx2mx2m

## Trajectories' formations
Firstly, time position pairs that described the main checkpoints were defined using checkpoint.py 
```bash
python3 checkpoint.py
```
Using https://github.com/whoenig/uav_trajectories to fit 8th order polynomials through the given time/position pair,it was possible to define smooth curves between each checkpoint. To ensure maximum fidelity to the checkpoints, the trajectories created were approximately 3 seconds long for each segment.
Run:

```bash
python3 scripts/generate_trajectory.py timed_waypoints_circle1.csv part1_.csv --pieces 38
python3 scripts/generate_trajectory.py timed_waypoints_circle2.csv part2_.csv --pieces 38
python3 scripts/generate_trajectory.py timed_waypoints_circle3.csv part3_.csv --pieces 38
python3 scripts/generate_trajectory.py timed_waypoints_circle4.csv part4_.csv --pieces 38
python3 scripts/generate_trajectory.py timed_waypoints_circle5.csv part5_.csv --pieces 38
python3 scripts/generate_trajectory.py timed_waypoints_circle6.csv part6_.csv --pieces 38
```

To check results before deploying any hardware, a visualization script for uncompressed poly8D curves (trajectory_video.py) was developed. 

<img width="623" height="614" alt="image" src="https://github.com/user-attachments/assets/b4469c92-3cc3-481c-9c24-bb5297a7a6a2" />

## Crazyflie Deployment
For each drone, a specific .csv file with the trajectory specifications has been written. Since the memory in each Crazyflie is limited, the upload was divided in two segments, with the second one being uploaded as soon as the first has finished running.
Note that all drones need to be on the same channel and, to ensure maximum performance in indoor environments, a datarate of 2Mhz is preferred. 
Before running, all the drones need to have been calibrated and be near their starting position.
The choreography can be started with
```bash
python3 coreo.py
```
and if necessary it can be interrupted via Keyboard Interrupt any moment.




