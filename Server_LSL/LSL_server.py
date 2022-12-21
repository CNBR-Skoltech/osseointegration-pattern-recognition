import mne
import numpy as np
import matplotlib.pyplot as plt
import pylsl
import time

print("Starting server...")
raw = mne.io.read_raw_brainvision('test_data/NeoRec_2022-11-03_11-57-36.vhdr', preload=True)
raw.drop_channels(['X', 'Y', 'Z', 'EMG_11', 'EMG_12', 'EMG_13', 'EMG_14', 'EMG_15', 'EMG_16'])
events = mne.events_from_annotations(raw)[0]
raw_np = raw.get_data()

# Opening LSL stream
stream_info = pylsl.StreamInfo(name="EMG_stream", type="EEG", channel_count=10, channel_format="double64", source_id="00000")
stream_outlet = pylsl.StreamOutlet(stream_info)

print("Start data streaming...")
i = 0
event_idx = 0
while True:
    for j in range(5000): # Roughly corresponds to 0.2ms delay in code with i7-7700HQ
        pass
    if i > events[event_idx+1, 0]:
        event_idx += 1
    stream_outlet.push_sample(raw_np[:, i])
    stream_outlet.push_sample(np.ones((10, 1)) * events[event_idx+1, 2])
    i += 1




