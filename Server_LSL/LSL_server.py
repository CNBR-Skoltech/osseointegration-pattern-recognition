import mne
import numpy as np
import matplotlib.pyplot as plt
import pylsl


LEG_RECORDING = False
NUMBER_OF_CHANNELS = 10
EVENT_NAMES = {'Pronation': 10001, 'Supination': 10003, 'Elbow flexion': 10004, 'Elbow extension': 10005,
              'Wrist flexion': 10006, 'Wrist extension': 10007, 'Fist closing': 10009, 'Fist opening': 10010,
              'Precise grip closing': 10011, 'Precise grip opening': 10012, 'Pointing grip closing': 10013,
              'Pointing grip opening': 10014, 'Rest state': 10015, 'Thumb to center': 10016, 'Thumb to lateral': 10017}
print("Starting server...")
raw = mne.io.read_raw_brainvision('../Data_copy/Server_LSL/test_data/NeoRec_2022-12-12_15-58-45.vhdr', preload=True)
if LEG_RECORDING:
    NUMBER_OF_CHANNELS = 12
    raw = raw.pick_channels([f"EMG_{i}" for i in range(1, NUMBER_OF_CHANNELS + 1)])
else:
    NUMBER_OF_CHANNELS = 10
    raw = raw.pick_channels([f"EMG_{i}" for i in range(1, NUMBER_OF_CHANNELS + 1)])
events = mne.events_from_annotations(raw)[0]
raw_np = raw.get_data()
# epochs = mne.Epochs(raw, events, tmin=0, tmax=2, event_id=EVENT_NAMES, preload=True, baseline=None)


# Opening LSL stream
stream_info = pylsl.StreamInfo(name="EMG_stream", type="EEG", channel_count=NUMBER_OF_CHANNELS, channel_format="double64", source_id="00000")
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
    # stream_outlet.push_sample(np.ones((10, 1)) * events[event_idx+1, 2])
    i += 1




