import sounddevice as sd
import numpy as np
import time

# Simple voice activity / speaking pace estimator
# Uses RMS energy over short windows

class AudioAnalyzer:
    def __init__(self, fs=16000, block_duration=0.5):
        self.fs = fs
        self.block_duration = block_duration
        self.last_time = time.time()
        self.activity = []

    def _callback(self, indata, frames, time_info, status):
        rms = np.sqrt(np.mean(indata**2))
        self.activity.append(rms)

        # keep last ~60 samples
        if len(self.activity) > 60:
            self.activity = self.activity[-60:]

    def start(self):
        self.stream = sd.InputStream(
            samplerate=self.fs,
            channels=1,
            callback=self._callback,
            blocksize=int(self.fs * self.block_duration)
        )
        self.stream.start()

    def stop(self):
        try:
            self.stream.stop()
            self.stream.close()
        except:
            pass

    def speaking_pace_score(self):
        if len(self.activity) < 5:
            return 40

        arr = np.array(self.activity)

        # normalize
        arr = arr / (arr.max() + 1e-6)

        # percentage of frames with "voice"
        voiced = np.sum(arr > 0.2) / len(arr)

        # map to 0–100
        return int(min(100, max(30, voiced * 120)))
