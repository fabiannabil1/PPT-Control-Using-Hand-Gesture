# PPT Control with MediaPipe

## Overview
This project enables hands-free control of PowerPoint presentations using hand gestures detected by MediaPipe. The program utilizes a webcam to track hand movements and translates specific gestures into keyboard inputs, allowing users to navigate slides without touching the keyboard.

## Features
- **Hand Detection**: Uses MediaPipe Hands to detect and track hand gestures.
- **Gesture Recognition**: Identifies the number of raised fingers.
- **Keyboard Emulation**: Sends arrow key inputs based on the recognized gesture:
  - **0 fingers** → Move to the next slide (Right Arrow Key)
  - **2 fingers** → Move to the previous slide (Left Arrow Key)
- **Real-time Processing**: Continuously analyzes hand position and updates control actions.

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- OpenCV (`cv2`)
- MediaPipe
- Pynput

To install dependencies, run:
```bash
pip install opencv-python mediapipe pynput asyncio
```

## Usage
1. Run the script:
   ```bash
   python script.py
   ```
2. Position your hand in front of the webcam.
3. Use the following gestures to control the slides:
   - **Close all fingers (0 raised fingers)** → Next slide
   - **Raise two fingers (index & middle)** → Previous slide
4. Press `q` to exit the program.

## Code Explanation
- The script captures video from the webcam.
- MediaPipe detects hand landmarks and determines the number of raised fingers.
- If a recognized gesture remains stable for 300ms, a corresponding keyboard event is triggered.
- The script sends keystrokes (`Key.right` or `Key.left`) to control PowerPoint slides.

## Notes
- Ensure adequate lighting for better hand detection.
- Adjust the gesture detection logic if needed for improved accuracy.
- Works best with a stable webcam setup.

## License
This project is open-source and free to use for educational and personal projects.

---
Enjoy controlling your PowerPoint slides hands-free! 🎤🎥

