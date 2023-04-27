def lru(page_list, frame_count):
    page_faults = 0
    page_hits = 0
    frames = []
    for page in page_list:
        if page not in frames:
            page_faults += 1
            if len(frames) == frame_count:
                frames.pop(0)
            frames.append(page)
        else:
            frames.remove(page)
            frames.append(page)
            page_hits += 1
    print(f"Page hits: {page_hits}, Page misses: {page_faults}")
    print(f"Page hit ratio: {page_hits/(page_hits+page_faults)}, Page miss ratio: {page_faults/(page_hits+page_faults)}")
    return page_faults


seq = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
nof = 4
lru(seq,nof)
