# camera_stream.py
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
import numpy as np
import cv2
import threading
import time

Gst.init(None)

class CameraStream:
    """GStreamer ile kamera okuma sınıfı."""

    def __init__(self, device="/dev/video0", width=640, height=480, fps=30):
        self.device = device
        self.width = width
        self.height = height
        self.fps = fps
        self.frame = None
        self.running = False
        self.pipeline = None
        self.appsink = None
        self.lock = threading.Lock()

    def _gst_loop(self):
        pipeline_str = (
            f"v4l2src device={self.device} ! "
            f"videoconvert ! "
            f"video/x-raw,format=BGR,width={self.width},height={self.height},framerate={self.fps}/1 ! "
            f"appsink name=appsink0 emit-signals=true max-buffers=1 drop=true"
        )
        try:
            self.pipeline = Gst.parse_launch(pipeline_str)
        except Exception as e:
            print(f"❌ Pipeline oluşturma hatası: {e}")
            return

        self.appsink = self.pipeline.get_by_name("appsink0")
        self.appsink.set_property("emit-signals", True)
        self.appsink.set_property("max-buffers", 1)
        self.appsink.set_property("drop", True)

        self.pipeline.set_state(Gst.State.PLAYING)

        while self.running:
            sample = self.appsink.emit("try-pull-sample", 1000000000)
            if sample:
                buf = sample.get_buffer()
                caps = sample.get_caps()
                struct = caps.get_structure(0)
                width = struct.get_value("width")
                height = struct.get_value("height")
                data = np.frombuffer(buf.extract_dup(0, buf.get_size()), dtype=np.uint8)
                frame = data.reshape((height, width, 3))
                with self.lock:
                    self.frame = frame
            time.sleep(0.001)

        self.pipeline.set_state(Gst.State.NULL)

    def start(self):
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self._gst_loop, daemon=True)
        self.thread.start()
        print(f"✅ Kamera başlatıldı: {self.device}")

    def read(self):
        with self.lock:
            return self.frame.copy() if self.frame is not None else None

    def stop(self):
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
        print("🛑 Kamera kapatıldı")


if __name__ == "__main__":
    cam = CameraStream()
    cam.start()
    try:
        while True:
            frame = cam.read()
            if frame is not None:
                cv2.imshow("Camera Test", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    finally:
        cam.stop()
        cv2.destroyAllWindows()
