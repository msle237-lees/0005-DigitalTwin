# DigitalTwin
This is a project where I am experimenting with Digital Twin Technology.

## Personal Research
- A Digital Twin of a ny device/system is a working model of all components integrated and mapped together using physical data, virtual data, and interaction between them to make a fully functional replica of the device/system and that too on a digital medium. - geeksforgeeks.org
- Possible data suppliers for AUV:
    - Sonar (2D Map of surroundings)
    - IMU (Accelerometer / Gyroscope / Magenetometer)
    - Voltage / Current Measurements (Voltage and Amperage)
    - Hydrophone heading direction (Compass directions)
    - Leak Detection
    - Depth Sensor (meters)
    - Internal Temperature
    - External Temperature
    - Internal Humidity
    - Internal Pressure
    - External Pressure
    - ZED 3D maps of perspective view point
- This won't be real-time since the host machine is located at the lab
- During run the data will be stored locally and when internet is available it will be uploaded to the remote server
- When data is uploaded, the model will analyze the uploaded data and represent it as a historical record


## What I would like to accomplish for this project:
1. Display a 3D representation of the sub with data views (graphs, charts, tables)
2. Project the Sonar and ZED data as viewable data within the 3D representation (ie. the environment around the sub represented)
3. 

## References:
1. https://www.geeksforgeeks.org/introduction-to-digital-twin/
