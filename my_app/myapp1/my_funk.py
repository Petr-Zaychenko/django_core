def trans_b_in_kb(size_in_bytes):
    if not size_in_bytes:
        return 0
    try:
        return round(float(size_in_bytes) / 1024, 2)
    except (TypeError, ValueError):
        return 0