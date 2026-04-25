import numpy as np

def signalogram(signal, win, overlap):
	win_len = len(win)
	total_frames = int(np.ceil((len(signal) - win_len) / overlap))

	required_len = (total_frames - 1) * overlap + win_len
	pad_len = len(signal) - required_len
	signal = np.concatenate([signal, np.zeros(pad_len)])

	frames = []
	for i in range(total_frames):
		start = i * overlap
		frame = signal[start : start + win_len] * win
		frames.append(frame)

	return np.column_stack(frames) 