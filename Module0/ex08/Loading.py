import os


def get_time(elapsed: float) -> str:
    """
    Format seconds as MM:SS
    """
    if elapsed < 0:
        elapsed = 0
    minutes = int(elapsed) // 60
    seconds = int(elapsed) % 60
    return f"{minutes:02d}:{seconds:02d}"


def render(i: int, total: int, start: float) -> None:
    """
    Render a tqdm-like progress line.
    """
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80

    now = os.times().elapsed
    elapsed = now - start if start is not None else 0.0
    rate = (i/elapsed) if elapsed > 0 else 0.0
    eta = ((total - i) / rate) if rate > 0 else 0.0

    percent = int(i * 100 / total) if total else 100

    left = f"{percent:3d}%|"
    right = f"| {i}/{total} [{get_time(elapsed)} < "
    right += f"{get_time(eta)}, {rate:.2f}it/s]"

    width = columns - len(left) - len(right)
    if width < 10:
        width = 10
    if i >= total:
        bar = "█" * width
    else:
        filled = int(i * width / total)
        if filled >= width:
            filled = width - 1
        bar = "█" * filled + " " * (width - filled - 1)
    line = "\r" + left + bar + right
    os.write(1, line.encode("utf-8", errors="ignore"))


def ft_tqdm(lst: range):
    """
    Yield elements from lst while displaying progress.
    """
    total = len(lst)
    if total == 0:
        return
    start = os.times().elapsed
    i = 0
    render(i, total, start)
    for elem in lst:
        yield elem
        i += 1
        render(i, total, start)
