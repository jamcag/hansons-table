import pandas as pd

df = pd.read_csv("mile_paces.csv")

def time_str_to_sec(t: str):
    """Converts a duration in mm:ss format to seconds."""
    minutes, seconds = map(int, t.split(":"))
    return minutes * 60 + seconds

def sec_to_time_str(s: float):
    """Converts seconds to mm:ss format."""
    minutes = int(s // 60)
    seconds = int(s % 60)
    return f"{minutes}:{seconds:02d}"


if __name__ == "__main__":
    for col in df.columns[2:]:
        df[col] = df[col].apply(lambda x: sec_to_time_str(time_str_to_sec(x) / 1.609344))

    df.to_csv("km_paces.csv", index=False)
    print(df.to_string(index=False))

