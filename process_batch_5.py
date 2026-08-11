"""
Process the 5 newly uploaded photos with Wong Kar-wai Lens Skill:
1. Skyscraper in the Mist (Shanghai Tower / IFC vertical look up)
2. Quiet Ancient / Old Town Street under blue sky
3. Rubber Boots with Flowers & "总有人正年轻/年少" floor calligraphy
4. Black Mercedes Benz at Hong Kong 7-Eleven Corner with Red Taxi
5. Hong Kong Red Taxi at Night from Behind with City Lights
"""

from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import numpy as np
import os
import shutil


def add_delicate_timestamp(img: Image.Image, timestamp_str: str, pos: str = "top-left") -> Image.Image:
    result = img.copy()
    draw = ImageDraw.Draw(result)
    w, h = result.size

    font_size = max(16, int(min(w, h) * 0.032))
    font_candidates = [
        "C:\\Windows\\Fonts\\consola.ttf",
        "C:\\Windows\\Fonts\\lucon.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
    ]
    font = None
    for fp in font_candidates:
        if os.path.exists(fp):
            try:
                font = ImageFont.truetype(fp, font_size)
                break
            except Exception:
                continue
    if not font:
        font = ImageFont.load_default()

    margin_x = int(w * 0.045)
    margin_y = int(h * 0.04)

    if pos == "top-left":
        tx, ty = margin_x, margin_y
    elif pos == "top-right":
        try:
            bbox = draw.textbbox((0, 0), timestamp_str, font=font)
            tw = bbox[2] - bbox[0]
        except Exception:
            tw = len(timestamp_str) * (font_size // 2)
        tx, ty = w - tw - margin_x, margin_y
    else:  # bottom-right
        try:
            bbox = draw.textbbox((0, 0), timestamp_str, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
        except Exception:
            tw = len(timestamp_str) * (font_size // 2)
            th = font_size
        tx, ty = w - tw - margin_x, h - th - margin_y

    text_color = (248, 185, 38)
    draw.text((tx + 1, ty + 1), timestamp_str, font=font, fill=(25, 20, 10))
    draw.text((tx, ty), timestamp_str, font=font, fill=text_color)
    return result


def grade_photo_custom(img: Image.Image, style: str = "wkw") -> Image.Image:
    """
    Applies continuous, artifact-free 90s film curves:
    - 'skyscraper': moodier cyan-grey mist, lifted blacks, subtle window lights
    - 'street': warm nostalgic sunlight, muted retro greens and cyan sky
    - 'boots': melancholic moody indoor low-key film, rich warm flower tones
    - 'street_corner': high contrast 90s street, rich red 7-11/taxi, deep black car
    - 'taxi_night': glowing night lights, deep cyan-teal road, rich ruby red taxi
    """
    arr = np.array(img.convert("RGB"), dtype=np.float32)

    if style == "skyscraper":
        # Moody vertical architectural film
        enh_c = ImageEnhance.Contrast(img).enhance(1.08)
        enh_s = ImageEnhance.Color(enh_c).enhance(1.05)
        arr = np.array(enh_s, dtype=np.float32)
        # Deepen cyan in mist and clouds
        arr[:, :, 0] *= 0.96
        arr[:, :, 1] *= 0.99
        arr[:, :, 2] *= 1.04

    elif style == "street":
        # Nostalgic afternoon street
        enh_c = ImageEnhance.Contrast(img).enhance(1.05)
        enh_s = ImageEnhance.Color(enh_c).enhance(1.10)
        arr = np.array(enh_s, dtype=np.float32)
        # Warm golden daylight + soft teal sky
        arr[:, :, 0] *= 1.03
        arr[:, :, 1] *= 1.00
        arr[:, :, 2] *= 0.97

    elif style == "boots":
        # Melancholic indoor still-life
        enh_c = ImageEnhance.Contrast(img).enhance(1.06)
        enh_s = ImageEnhance.Color(enh_c).enhance(1.12)
        arr = np.array(enh_s, dtype=np.float32)
        # Warm nostalgic film tone
        arr[:, :, 0] *= 1.04
        arr[:, :, 1] *= 0.99
        arr[:, :, 2] *= 0.98

    elif style == "street_corner":
        # Chungking Express street corner
        enh_c = ImageEnhance.Contrast(img).enhance(1.08)
        enh_s = ImageEnhance.Color(enh_c).enhance(1.15)
        arr = np.array(enh_s, dtype=np.float32)
        # Rich saturated red taxi & 7-11 sign, deep glossy blacks
        arr[:, :, 0] *= 1.05
        arr[:, :, 1] *= 0.98
        arr[:, :, 2] *= 1.01

    elif style == "taxi_night":
        # Fallen Angels midnight taxi
        enh_c = ImageEnhance.Contrast(img).enhance(1.10)
        enh_s = ImageEnhance.Color(enh_c).enhance(1.18)
        arr = np.array(enh_s, dtype=np.float32)
        # Glowing warm highlights, deep cyan-teal night shadows
        arr[:, :, 0] *= 1.06
        arr[:, :, 1] *= 0.98
        arr[:, :, 2] *= 1.03

    arr = np.clip(arr, 0, 255)
    return Image.fromarray(arr.astype(np.uint8))


def process_5_photos():
    brain_dir = r'C:\Users\caoshichuang\.gemini\antigravity\brain\bfd7a2d5-865e-4d99-8f7b-ad798b1d4434'
    uploads_dir = os.path.join(brain_dir, '.user_uploaded')

    tasks = [
        {
            "id": "01_skyscraper",
            "file": "media_1786475394042.png",
            "style": "skyscraper",
            "timestamp": "'97  6 30",
            "pos": "top-left",
            "title": "《仰望高塔 · 雾中的城》",
            "monologue": "“一九九七年六月三十日，大雾。我站在楼底下往上看，整座大厦的顶端都插在云里面。我不知道上面住着什么样的人，但在雾散开之前，这里安静得像是一个没人知道的秘密。”"
        },
        {
            "id": "02_ancient_street",
            "file": "media_1786475394048.jpg",
            "style": "street",
            "timestamp": "'94  8 15",
            "pos": "top-right",
            "title": "《老街午后 · 一条街的距离》",
            "monologue": "“那天下午阳光很好，这条石板路大概有三百米长。我从街头走到街尾花了六分半钟，路过七家店铺，两个遮阳伞，还有一位坐在轮椅上的老人。我和他们擦肩而过的时候，谁都没有看谁。”"
        },
        {
            "id": "03_boots_flowers",
            "file": "media_1786475394086.jpg",
            "style": "boots",
            "timestamp": "'95  9 12",
            "pos": "top-right",
            "title": "《雨靴与花 · 总有人正年少》",
            "monologue": "“地面上的字不知道是谁写上去的，雨靴里的花也不知道是谁插进去的。所有的花都会枯萎，雨靴也会积满灰尘。但在这个世界上，总有人正年少，就像明天太阳照常升起一样笃定。”"
        },
        {
            "id": "04_corner_benz",
            "file": "media_1786475394162.jpg",
            "style": "street_corner",
            "timestamp": "'96 10 24",
            "pos": "top-left",
            "title": "《街角便利店 · 红绿灯下的停顿》",
            "monologue": "“在七十一便利店门口，红灯会亮四十五秒。那辆黑色的奔驰停在斑马线前，后面紧跟着一辆红色的士。在那个下午，我和那辆车最近的时候只有三米。四十五秒之后，绿灯亮了，大家都急着赶去下一个地方。”"
        },
        {
            "id": "05_taxi_rear_night",
            "file": "media_1786475394175.jpg",
            "style": "taxi_night",
            "timestamp": "'95 12 04",
            "pos": "top-left",
            "title": "《夜行的士 · NU 3090》",
            "monologue": "“这辆车牌号是 NU 3090 的红色的士，车顶灯在深夜里亮得很扎眼。在香港的深夜，总有一些人坐着它去往某个人的身边，也总有一些人坐着它离开。车尾灯亮起来的时候，我知道又一段故事结束了。”"
        }
    ]

    for t in tasks:
        in_path = os.path.join(uploads_dir, t["file"])
        orig_img = Image.open(in_path).convert("RGB")
        
        # Save Before
        before_path = os.path.join(brain_dir, f"batch_{t['id']}_before.jpg")
        orig_img.save(before_path, quality=98)

        # Grade and add timestamp
        graded = grade_photo_custom(orig_img, style=t["style"])
        stamped = add_delicate_timestamp(graded, timestamp_str=t["timestamp"], pos=t["pos"])
        
        # Save After
        after_path = os.path.join(brain_dir, f"batch_{t['id']}_after.jpg")
        stamped.save(after_path, quality=98)

        print(f"[+] Successfully processed: {t['title']}")

    print("All 5 photos successfully generated with WKW Skill!")


if __name__ == "__main__":
    process_5_photos()
