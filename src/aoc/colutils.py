def index[TValue](l: list[TValue], x: TValue, start: int=0) -> int:
    try:
        return l.index(x, start)
    except:
        return -1