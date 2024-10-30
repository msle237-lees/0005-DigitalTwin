# DigitalTwin
This is a project where I am experimenting with Digital Twin Technology.

## Use Case:
This project will use KSU AUV's HOPE design as the model. 

## Data inputs at current:
- Gyroscope / Accelerometer / Compass Data
- Thruster Values (PWM) / Claw Value (PWM) / Torpedoe Value (dual Boolean Value)
- Internal Temperature Values for both Orin and Electrical Housing
- Internal Humidity Values for Electrical Housing
- Hydrophone Location data
- Sonar Mapping data
- 3D mapping from ZED Camera

## Digital Twins are simulated 3D models that allow for accurate and precise data representation. 
## It can also be used to predict faults later but we won't be using it. 

## Current Plan:
- Using Electron.js and Three.JS create the 3D interface
- Using Hope's design in a wireframe format
- Use Python for the back end to handle data collection and the AI
- Data Inputs:
    - Gyroscope / Accelerometer / Compass Data
    - Thruster Values (PWM) / Claw Value (PWM) / Torpedoe Value (dual Boolean Value)
    - Internal Temperature Values for both Orin and Electrical Housing
    - Internal Humidity Values for Electrical Housing
    - Hydrophone Location data
    - Sonar Mapping data
    - 3D mapping from ZED Camera

## Step 1: 
- Create the front-end representation using Electron and Three.js

## Step 2:
- Create the Data representation from the back-end data from competition