def study_schedule(per, tm):
    set_count = 0
    if not tm:
        return None
    for start, out in per:
        if not isinstance(start, int) or not isinstance(out, int):
            return None
        if start <= tm <= out:
            set_count += 1
    return set_count

