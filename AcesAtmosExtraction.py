import os
import subprocess
import sys

def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def detect_layout(m4a):
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "a:0",
        "-show_entries", "stream=channel_layout",
        "-of", "default=noprint_wrappers=1:nokey=1",
        m4a
    ]
    r = run(cmd)
    layout = r.stdout.strip()

    if "7.1" in layout:
        return "7.1"
    if "5.1" in layout:
        return "5.1"
    return None

def extract(m4a, out_ext):
    base = os.path.splitext(os.path.basename(m4a))[0]
    parent = os.path.dirname(m4a)
    out_dir = os.path.join(parent, f"{base} Atmos")
    os.makedirs(out_dir, exist_ok=True)

    layout = detect_layout(m4a)
    if not layout:
        print(f"❌ Could not detect channel layout: {base}")
        return

    if layout == "5.1":
        channels = ["FL", "FR", "FC", "LFE", "SL", "SR"]
    else:  # 7.1
        channels = ["FL", "FR", "FC", "LFE", "BL", "BR", "SL", "SR"]

    # Build filter_complex string with channel labels
    filter_labels = "".join(f"[{ch}]" for ch in channels)
    filter_complex = f"channelsplit=channel_layout={layout}{filter_labels}"

    cmd = ["ffmpeg", "-y", "-i", m4a, "-filter_complex", filter_complex]

    for i, ch in enumerate(channels):
        out_file = os.path.join(out_dir, f"{base} Track {i+1}.{out_ext}")
        # If user chose M4A but this is single-channel, switch to WAV
        final_ext = out_ext
        if out_ext == "m4a":
            final_ext = "wav"
            out_file = os.path.splitext(out_file)[0] + ".wav"
        cmd += ["-map", f"[{ch}]", out_file]

    print(f"Extracting: {base} ({layout}) -> {out_ext}")
    result = subprocess.run(cmd)

    if result.returncode != 0:
        print(f"❌ FFmpeg failed on {base}")

def main():
    print("- Directory containing Amazon Music Atmos m4a files?")
    root = input("* ").strip()

    if not os.path.isdir(root):
        print(f"❌ Directory does not exist: {root}")
        sys.exit(1)

    print("- Remux extracted channels?")
    print("0 = No (keep m4a)")
    print("1 = FLAC")
    print("2 = WAV")
    print("3 = MP3")
    choice = input("* ").strip()

    ext_map = {
        "0": "m4a",
        "1": "flac",
        "2": "wav",
        "3": "mp3"
    }

    if choice not in ext_map:
        print("❌ Invalid choice")
        sys.exit(1)

    out_ext = ext_map[choice]

    found = False
    for item in os.listdir(root):
        if item.lower().endswith(".m4a"):
            found = True
            extract(os.path.join(root, item), out_ext)

    if not found:
        print("⚠️ No .m4a files found in that directory")

if __name__ == "__main__":
    main()
