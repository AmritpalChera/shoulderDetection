# Shoulder Detection
This code uses the tensorflow pose detection library along with opencv to classify key body points from a live video. The script marks the position of shoulder points for easy visualization.

## How to run
1. Create venv:  `python -m venv .`
2. Activate venv: `source ./Scripts/activate`
4. Intall packages: `pip install -r requirements.txt`
5. Run the pose_estimation.py script: `python pose_estimation.py`

The repo supports 2 installed models from the pose estimation library. Movenet Thunder and Lightning. To achieve the highest accuracy, the Movenet Thunder model must be used. According to performance tests, this model takes about 500ms to classify a frame on a Raspberry Pi 4. On a PC, the lag is minimal.
