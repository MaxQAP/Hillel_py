from datetime import datetime

# Константа для фільтрації конкретного потоку
TARGET_KEY = "TSTFEED0300|7E3E|0400"
INPUT_FILE = "hblog.txt"
OUTPUT_FILE = "hb_test.log"


def get_filter_timestamps(file_path, key):
    timestamps = []
    with open(file_path, 'r') as file:
        for line in file:
            if key in line:
                start_index = line.find("Timestamp ") + len("Timestamp ")
                time_str = line[start_index:start_index + 8]
                time_obj = datetime.strptime(time_str, "%H:%M:%S")
                timestamps.append(time_obj)
    return timestamps


def analyze_heartbeat(timestamps):
    with open(OUTPUT_FILE, 'w') as log_file:
        for i in range(len(timestamps) - 1):
            diff = abs((timestamps[i] - timestamps[i + 1]).total_seconds())
            error_time = timestamps[i + 1].strftime("%H:%M:%S")
            if 31 < diff < 33:
                log_file.write(f"[{error_time}] WARNING: Heartbeat is {diff} sec\n")
            elif diff >= 33:
                log_file.write(f"[{error_time}] ERROR: Heartbeat is {diff} sec\n")


def run_homework20():
    data = get_filter_timestamps(INPUT_FILE, TARGET_KEY)
#створюємо hb_test.log
    analyze_heartbeat(data)

    print(f"Результати записані у {OUTPUT_FILE}")


if __name__ == "__main__":
    run_homework20()

