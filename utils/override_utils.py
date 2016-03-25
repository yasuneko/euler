def inclusive_range(start, stop=None, step=None):
	if stop:
		if step:
			return range(start, stop + 1, step)
		return range(start, stop + 1)
	elif step:
		return range(0, start + 1, step)
	return range(start + 1)
	
