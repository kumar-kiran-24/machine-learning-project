import os, sys, json
from datetime import datetime
from flask import Flask, jsonify
from src.utils.logger import logging
from src.utils.exception import CustomException
from src.component.capture.video_capture import VideoRecorder
from src.component.capture.image_capture import ImageCapture
from src.model.face_recognizer import FaceRecognizer
from src.pipeline.attendence_counter import AttendanceMarker
from src.data_preprocessing.image_selector import ImageSelector
from src.data_preprocessing.video_to_image import VideoToImage


class Main:
    def __init__(self):
        try:
            self.face_recognizer = FaceRecognizer()
            self.attendance_counter = AttendanceMarker()
            self.video_recorder = VideoRecorder()
            self.image_capturer = ImageCapture()
            self.video_to_image = VideoToImage()
            self.image_selector = ImageSelector()
        except Exception as e:
            logging.error("Error initializing Main class")
            raise CustomException(e, sys)

    def initiate_main(self):
        try:
            # 1️⃣ Record video
            path_to_video_recorded = self.video_recorder.initiate_videorecorder()

            # 2️⃣ Convert video to frames
            path_to_raw_frames = self.video_to_image.video_to_frames(path_to_video_recorded, frame_skip=5)

            # 3️⃣ Recognize faces
            students_per_image = self.face_recognizer.recognize_images_in_folder(folder_path=path_to_raw_frames)

            # 4️⃣ Attendance marking
            all_students = ["kiran","prasana","suhas","manoj"]
            present, absent = self.attendance_counter.initiate_mark_attendance(
                students_per_image, all_students, threshold=2, min_conf=0.4
            )

            # 5️⃣ Save results
            base_dir = "C:/ht/result"
            os.makedirs(base_dir, exist_ok=True)
            folder_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            folder_path = os.path.join(base_dir, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            file_path = os.path.join(folder_path, "attendance.json")
            with open(file_path, "w") as f:
                json.dump({"present": present, "absent": absent, "time": folder_name}, f, indent=4)

            logging.info(f"Attendance saved at {file_path}")
            return present, absent

        except Exception as e:
            logging.error("Error in initiate_main")
            raise CustomException(e, sys)


# 🔹 Flask API
app = Flask(__name__)
main_obj = Main()

@app.route("/mark_attendance", methods=["GET"])
def mark_attendance():
    try:
        present, absent = main_obj.initiate_main()
        return jsonify({"Present": present, "Absent": absent})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
