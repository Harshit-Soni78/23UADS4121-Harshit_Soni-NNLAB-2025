# Mini Projects

- **Mini Project 1:** Build an image dataset that contains grayscale images of leaves of various plants/trees growing in MBMU campus. Perform necessary preprocessing steps to make the dataset uniform and ready for training. Train a deep autoencoder network that can reproduce any random image of a leaf from MBMU campus.

  - **_Bonus:_** Can we use this network to identify if a leaf is from MBM Campus or not?

---

- **Mini Project 2:** Create an Android App that captures the readings from motion sensors (accelerometer and gyroscope) in an android phone. Build a dataset using this application that contains the motion characteristics of an average person driving a two-wheeler. Build a LSTM classifier that takes any 3 second sample as input and classifies it as Kankar Road, Bitumen Road, Concrete Road, Single Speed Breaker and Multiple Speed Breakers.

  - **_Bonus:_** Can we use this dataset to generate alerts when a person is rash driving?

---

- **Mini Project 3:** Build a Video Dataset that contains short videos (max. 5 seconds) of students performing Yogasanas (atleast 6 asanas) with diverse backgrounds, ambient lighting and clothes. Train a CNN that can identify the asana being performed in the video.

  - **_Bonus:_** Can we further rate the asana pose as Good, Average and Poor?

---

---

## I have got the Mini Project 2

- **Mini Project 2:** Create an Android App that captures the readings from motion sensors (accelerometer and gyroscope) in an android phone. Build a dataset using this application that contains the motion characteristics of an average person driving a two-wheeler. Build a LSTM classifier that takes any 3 second sample as input and classifies it as Kankar Road, Bitumen Road, Concrete Road, Single Speed Breaker and Multiple Speed Breakers.

  - **_Bonus:_** Can we use this dataset to generate alerts when a person is rash driving?

## Steps to do

- Dataset Strategy
- Dataset Collection & Compilation
- Dataset Labelling and Pre-processing
- Model Architecture
- Model Training
- Model Optimization & Comparison
- Bonus Evaluation
- Model Chart Review
- Model Chart Submission

### Dataset Strategy

#### **_App Development with MIT App Inventor to Capture Sensor Data_**

We need an Android app to capture and save motion sensor readings.

Use MIT App Inventor to collect data.

MIT App Inventor is beginner-friendly but limited in advanced features.

**Steps:**

- Create a New Project: Go to MIT App Inventor, log in, and create a new project.
- Add Sensors: Add accelerometer and gyroscope components.
- Design the Interface: Create buttons for actions like “Start Recording” and “Stop Recording.”
- Save Data: Use the TinyDB or File component to save sensor data locally in CSV format.
- Export Data: Add functionality to send the file to your computer using email or Google Drive or do it manually.

We can use MIT App Inventor for this part, and I can guide you through designing the app.

#### **_Data Collection_**

**Prepare Your Environment:**

- Attach the phone securely to the two-wheeler.
- Select diverse routes (kankar, bitumen, concrete roads, etc.).

**Collect Data:**

- Start the app and record sensor readings while driving.
- Manually label the data or use a consistent annotation process during collection.
