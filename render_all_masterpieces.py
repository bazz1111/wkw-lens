"""
Master Batch Cinema Renderer for All Showcase Scenes.
Applies the full Christopher Doyle / Wong Kar-wai optical physics suite:
- Kodak Vision3 500T / 2383 / Ektachrome color curves
- Schneider Black Pro-Mist bloom & Kodak red halation
- Velvet lifted teal blacks & tungsten amber highlights
- Delicate 90s yellow timestamps
"""

from PIL import Image
import os
import shutil
from src.film_emulation_engine import transform_to_wkw_masterpiece

def run():
    brain_dir = r'C:\Users\caoshichuang\.gemini\antigravity\brain\bfd7a2d5-865e-4d99-8f7b-ad798b1d4434'
    uploads_dir = os.path.join(brain_dir, '.user_uploaded')
    examples_dir = r'C:\Users\caoshichuang\.gemini\antigravity\scratch\wong-kar-wai-lens\examples'

    scenes = [
        {
            "id": "scene_01_kennedy_town",
            "file": "media_1786475543270.jpg",
            "preset": "kennedy_town",
            "timestamp": "'95  5 20",
            "pos": "top-right",
            "title": "《坚尼地城 · 通往海的下坡路》",
            "recipe": "ARRIFLEX 535B + Cooke S7/i 18mm T2.0 + Kodak 500T + Black Pro-Mist 1/4",
            "monologue": "“从坚尼地城的斜坡看下去，尽头就是大海。每天下午三点，绿色的十六座小巴会排着队往下开。我隔着铁丝网看了很久，以为只要顺着这条路一直走，就能走到世界尽头。”"
        },
        {
            "id": "scene_02_sushi_night",
            "file": "media_1786475543275.jpg",
            "preset": "sushi",
            "timestamp": "'96 11 08",
            "pos": "top-left",
            "title": "《深夜食堂 · 卓鮨的灯笼》",
            "recipe": "ARRI ALEXA 35 + Zeiss Super Speed 28mm T1.3 + Kodak 500T + 2800K Tungsten + Pro-Mist Bloom",
            "monologue": "“这盏白色的灯笼每天晚上六点亮起来，凌晨一点熄灭。我常常坐在门外的栏杆上看里面的人进进出出。有些人是为了填饱肚子，有些人只是害怕一个人回家。”"
        },
        {
            "id": "scene_03_sunset_seagulls",
            "file": "media_1786475543281.jpg",
            "preset": "sunset",
            "timestamp": "'97  7 01",
            "pos": "top-left",
            "title": "《落日海鸥 · 飞过水面的影子》",
            "recipe": "Aaton XTR Super 16 + Leica Summilux 35mm T1.4 + Kodak Ektachrome 100D + 3000K Golden Backlight",
            "monologue": "“太阳落下去需要八分钟，海鸥飞过水面只需要两秒。在那个黄昏，我数到第七十四只海鸥的时候，天已经彻底暗了。有些事情发生得很快，快到你连遗忘的时间都没有。”"
        },
        {
            "id": "scene_04_wedding_dolls",
            "file": "media_1786475543283.jpg",
            "preset": "night_noir",
            "timestamp": "'94  2 14",
            "pos": "top-right",
            "title": "《双喜 · 树影下的人偶》",
            "recipe": "ARRIFLEX 535B + Zeiss Master Prime 50mm T1.3 + Kodak 500T + Fairy Light Bokeh Halation",
            "monologue": "“身上贴着双喜的人偶在树下站了整整三年。树上的小灯泡坏了四个，它们还是在笑。在这个城市里，有些笑容是真的，有些只是习惯了挂在脸上。”"
        },
        {
            "id": "scene_05_snow_mountain",
            "file": "media_1786475543309.jpg",
            "preset": "snow",
            "timestamp": "'95  1 18",
            "pos": "top-left",
            "title": "《雪原孤车 · 山脉的尽头》",
            "recipe": "ARRI ALEXA 35 + Angénieux Optimo 28-76mm T2.6 + Kodak 2383 Print Stock + 6500K Cool Tones",
            "monologue": "“以前我认为翻过这座雪山，就能看到另一番天地。等我开着车真正到了山顶，才发现另一边不过是更多的雪和更大的风。但既然已经停在了这里，就索性坐下来抽完这支烟。”"
        },
        {
            "id": "scene_06_taxi_topdown",
            "file": "media_1786473614358.jpg",
            "preset": "taxi",
            "timestamp": "'95 11 12",
            "pos": "top-left",
            "title": "《弥敦道 · 红色的士》（俯拍街景）",
            "recipe": "ARRIFLEX 535B + Zeiss 28mm T1.3 + Kodak Vision3 500T + Red Halation + Wet Asphalt Teal",
            "monologue": "“在香港，每天有两万四千辆红色的士在路上跑。从尖沙咀到旺角，总共要拐十四个弯。那天晚上，我和前面那辆车最近的时候，距离只有两米。后来绿灯亮了，它向左转，我向右转。”"
        },
        {
            "id": "scene_07_skyscraper_fog",
            "file": "media_1786475394042.png",
            "preset": "skyscraper",
            "timestamp": "'97  6 30",
            "pos": "top-left",
            "title": "《仰望高塔 · 雾中的城》",
            "recipe": "ARRIFLEX 535B + Cooke 18mm T2.0 Ultra Wide + Kodak 500T + Moody Mist Cyan Matrix",
            "monologue": "“一九九七年六月三十日，大雾。我站在楼底下往上看，整座大厦的顶端都插在云里面。我不知道上面住着什么样的人，但在雾散开之前，这里安静得像是一个没人知道的秘密。”"
        },
        {
            "id": "scene_08_corner_benz",
            "file": "media_1786475394162.jpg",
            "preset": "street_corner",
            "timestamp": "'96 10 24",
            "pos": "top-left",
            "title": "《街角便利店 · 红绿灯下的停顿》",
            "recipe": "ARRI ALEXA 35 + Zeiss 35mm T1.4 + Kodak Vision3 500T + Saturated 7-11 Red & Deep Blacks",
            "monologue": "“在七十一便利店门口，红灯会亮四十五秒。那辆黑色的奔驰停在斑马线前，后面紧跟着一辆红色的士。在那个下午，我和那辆车最近的时候只有三米。四十五秒之后，绿灯亮了，大家都急着赶去下一个地方。”"
        },
        {
            "id": "scene_09_taxi_rear_night",
            "file": "media_1786475394175.jpg",
            "preset": "taxi",
            "timestamp": "'95 12 04",
            "pos": "top-left",
            "title": "《夜行的士 · NU 3090》（追尾视角）",
            "recipe": "ARRIFLEX 535B + Zeiss 50mm T1.3 + Kodak 500T + Tail Light Bloom & Halation",
            "monologue": "“这辆车牌号是 NU 3090 的红色的士，车顶灯在深夜里亮得很扎眼。在香港的深夜，总有一些人坐着它去往某个人的身边，也总有一些人坐着它离开。车尾灯亮起来的时候，我知道又一段故事结束了。”"
        }
    ]

    for s in scenes:
        in_fp = os.path.join(uploads_dir, s["file"])
        before_fp = os.path.join(brain_dir, f"{s['id']}_before.jpg")
        after_fp = os.path.join(brain_dir, f"{s['id']}_after.jpg")
        
        # Save Before
        orig = Image.open(in_fp).convert("RGB")
        orig.save(before_fp, quality=98)
        
        # Render and Save After
        transform_to_wkw_masterpiece(
            in_fp,
            after_fp,
            preset=s["preset"],
            timestamp=s["timestamp"],
            timestamp_pos=s["pos"]
        )
        print(f"[+] Rendered: {s['title']}")

    print("All master scenes rendered successfully!")

if __name__ == "__main__":
    run()
