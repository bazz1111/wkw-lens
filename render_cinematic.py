from src.film_emulation_engine import transform_to_wkw_masterpiece
import os

def run():
    brain_dir = r'C:\Users\caoshichuang\.gemini\antigravity\brain\bfd7a2d5-865e-4d99-8f7b-ad798b1d4434'
    uploads_dir = os.path.join(brain_dir, '.user_uploaded')
    examples_dir = r'C:\Users\caoshichuang\.gemini\antigravity\scratch\wong-kar-wai-lens\examples'

    items = [
        # 1. Kennedy Town Slope to Sea
        ("media_1786475543270.jpg", "cinema_01_kennedy_town.jpg", "kennedy_town", "'95  5 20", "top-right"),
        # 2. Japanese Sushi Restaurant with glowing lantern
        ("media_1786475543275.jpg", "cinema_02_sushi_night.jpg", "sushi", "'96 11 08", "top-left"),
        # 3. Sunset Seagulls over Lake & Bridge
        ("media_1786475543281.jpg", "cinema_03_sunset_seagulls.jpg", "sunset", "'97  7 01", "top-left"),
        # 4. Chinese Wedding Dolls under Fairy Lights
        ("media_1786475543283.jpg", "cinema_04_wedding_dolls.jpg", "night_noir", "'94  2 14", "top-right"),
        # 5. Snowy Mountain SUV
        ("media_1786475543309.jpg", "cinema_05_snow_mountain.jpg", "snow", "'95  1 18", "top-left"),
        # 6. Hong Kong Red Taxis at Night
        ("media_1786473614358.jpg", "cinema_06_taxi_night.jpg", "taxi", "'95 11 12", "top-left"),
    ]

    for orig_name, out_name, preset, stamp, pos in items:
        in_fp = os.path.join(uploads_dir, orig_name)
        out_fp = os.path.join(examples_dir, out_name)
        brain_out_fp = os.path.join(brain_dir, out_name)
        
        transform_to_wkw_masterpiece(in_fp, out_fp, preset=preset, timestamp=stamp, timestamp_pos=pos)
        transform_to_wkw_masterpiece(in_fp, brain_out_fp, preset=preset, timestamp=stamp, timestamp_pos=pos)
        print(f"[+] Rendered true cinema masterpiece: {out_name}")

if __name__ == "__main__":
    run()
