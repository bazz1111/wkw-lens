"""
Process the second batch of 5 photos with Wong Kar-wai Lens Skill:
1. HK Kennedy Town Street to the Sea (Minibuses & Sea through fence)
2. Midnight Japanese Restaurant "卓鮨" (Glowing lantern & sliding door)
3. Sunset Seagulls over Lake & Bridge (Golden sunset & silhouettes)
4. Traditional Chinese Wedding Figurines under Fairy Lights at Night
5. Winter Mountain Pass & Off-road SUV (Snowy mountain solitude)
"""

from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import numpy as np
import os


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
    Continuous, smooth 90s film color grading.
    """
    arr = np.array(img.convert("RGB"), dtype=np.float32)

    if style == "hk_street_sea":
        # Kennedy Town: boost saturated red/green minibuses & deep cyan sea
        enh_c = ImageEnhance.Contrast(img).enhance(1.08)
        enh_s = ImageEnhance.Color(enh_c).enhance(1.15)
        arr = np.array(enh_s, dtype=np.float32)
        arr[:, :, 0] *= 1.04
        arr[:, :, 1] *= 1.01
        arr[:, :, 2] *= 1.02

    elif style == "lantern_night":
        # Warm glowing Japanese lantern in dark night
        enh_c = ImageEnhance.Contrast(img).enhance(1.09)
        enh_s = ImageEnhance.Color(enh_c).enhance(1.12)
        arr = np.array(enh_s, dtype=np.float32)
        arr[:, :, 0] *= 1.06
        arr[:, :, 1] *= 0.99
        arr[:, :, 2] *= 0.96

    elif style == "sunset_birds":
        # 2046 / Happy Together golden hour sunset & silhouettes
        enh_c = ImageEnhance.Contrast(img).enhance(1.06)
        enh_s = ImageEnhance.Color(enh_c).enhance(1.16)
        arr = np.array(enh_s, dtype=np.float32)
        arr[:, :, 0] *= 1.05
        arr[:, :, 1] *= 0.98
        arr[:, :, 2] *= 0.96

    elif style == "wedding_dolls":
        # In the Mood for Love / Chungking Express nostalgic evening lights
        enh_c = ImageEnhance.Contrast(img).enhance(1.08)
        enh_s = ImageEnhance.Color(enh_c).enhance(1.14)
        arr = np.array(enh_s, dtype=np.float32)
        arr[:, :, 0] *= 1.06
        arr[:, :, 1] *= 0.99
        arr[:, :, 2] *= 0.97

    elif style == "snowy_mountain":
        # Ashes of Time / Happy Together melancholic vast landscape
        enh_c = ImageEnhance.Contrast(img).enhance(1.07)
        enh_s = ImageEnhance.Color(enh_c).enhance(1.08)
        arr = np.array(enh_s, dtype=np.float32)
        # Deep cyan mountain tones, cool lifted snow highlights
        arr[:, :, 0] *= 0.98
        arr[:, :, 1] *= 1.01
        arr[:, :, 2] *= 1.05

    arr = np.clip(arr, 0, 255)
    return Image.fromarray(arr.astype(np.uint8))


def process_second_batch():
    brain_dir = r'C:\Users\caoshichuang\.gemini\antigravity\brain\bfd7a2d5-865e-4d99-8f7b-ad798b1d4434'
    uploads_dir = os.path.join(brain_dir, '.user_uploaded')

    tasks = [
        {
            "id": "06_kennedy_town",
            "file": "media_1786475543270.jpg",
            "style": "hk_street_sea",
            "timestamp": "'95  5 20",
            "pos": "top-right",
            "title": "《坚尼地城 · 通往海的下坡路》",
            "monologue": "“从坚尼地城的斜坡看下去，尽头就是大海。每天下午三点，绿色的十六座小巴会排着队往下开。我隔着铁丝网看了很久，以为只要顺着这条路一直走，就能走到世界尽头。”"
        },
        {
            "id": "07_sushi_night",
            "file": "media_1786475543275.jpg",
            "style": "lantern_night",
            "timestamp": "'96 11 08",
            "pos": "top-left",
            "title": "《深夜食堂 · 卓鮨的灯笼》",
            "monologue": "“这盏白色的灯笼每天晚上六点亮起来，凌晨一点熄灭。我常常坐在门外的栏杆上看里面的人进进出出。有些人是为了填饱肚子，有些人只是害怕一个人回家。”"
        },
        {
            "id": "08_sunset_seagulls",
            "file": "media_1786475543281.jpg",
            "style": "sunset_birds",
            "timestamp": "'97  7 01",
            "pos": "top-left",
            "title": "《落日海鸥 · 飞过水面的影子》",
            "monologue": "“太阳落下去需要八分钟，海鸥飞过水面只需要两秒。在那个黄昏，我数到第七十四只海鸥的时候，天已经彻底暗了。有些事情发生得很快，快到你连遗忘的时间都没有。”"
        },
        {
            "id": "09_wedding_dolls",
            "file": "media_1786475543283.jpg",
            "style": "wedding_dolls",
            "timestamp": "'94  2 14",
            "pos": "top-right",
            "title": "《双喜 · 树影下的人偶》",
            "monologue": "“身上贴着双喜的人偶在树下站了整整三年。树上的小灯泡坏了四个，它们还是在笑。在这个城市里，有些笑容是真的，有些只是习惯了挂在脸上。”"
        },
        {
            "id": "10_snow_mountain",
            "file": "media_1786475543309.jpg",
            "style": "snowy_mountain",
            "timestamp": "'95  1 18",
            "pos": "top-left",
            "title": "《雪原孤车 · 山脉的尽头》",
            "monologue": "“以前我认为翻过这座雪山，就能看到另一番天地。等我开着车真正到了山顶，才发现另一边不过是更多的雪和更大的风。但既然已经停在了这里，就索性坐下来抽完这支烟。”"
        }
    ]

    for t in tasks:
        in_path = os.path.join(uploads_dir, t["file"])
        orig_img = Image.open(in_path).convert("RGB")
        
        # Save Before
        before_path = os.path.join(brain_dir, f"batch2_{t['id']}_before.jpg")
        orig_img.save(before_path, quality=98)

        # Grade and add timestamp
        graded = grade_photo_custom(orig_img, style=t["style"])
        stamped = add_delicate_timestamp(graded, timestamp_str=t["timestamp"], pos=t["pos"])
        
        # Save After
        after_path = os.path.join(brain_dir, f"batch2_{t['id']}_after.jpg")
        stamped.save(after_path, quality=98)

        print(f"[+] Successfully processed: {t['title']}")

    print("All 5 photos (Part 2) successfully generated with WKW Skill!")


if __name__ == "__main__":
    process_second_batch()
