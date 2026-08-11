---
name: "wong-kar-wai-lens"
description: "Transform everyday photos into 1990s Hong Kong cinema masterpieces (Wong Kar-wai & Christopher Doyle aesthetic) using true cinematography hardware parameters (ARRI 35mm, Cooke/Zeiss primes, Kodak 500T emulsion, Pro-Mist halation, step-printing, and poetic monologues)."
---

# 王家卫电影镜头 (Wong Kar-wai Lens Skill)

`wong-kar-wai-lens` 是一个将普通摄影照片重塑为 **1980-1990 年代经典香港电影（王家卫 / 杜琪峰 / 摄影大师杜可风）** 级画质的专业摄影场景设计与重塑开源 Skill。

借鉴顶级摄影参数设计规范，本 Skill 不仅提供**物理色彩分级与独白生成**，更通过**真实电影机身、镜头品牌、超广角/大光圈焦段、Kodak 500T 胶卷乳剂、黑柔滤镜发光、色温布光模式**等全套硬件光学参数精确控制画面氛围。

---

## 🎬 1. 核心光学与器材参数矩阵 (Cinematography Optics)

完整的器材与光学参考见：[`prompts/cinematography_optics_guide.md`](prompts/cinematography_optics_guide.md)

### 📷 核心硬件组合推荐

| 风格意图 | 推荐机身 & 镜头 | 胶卷感光乳剂 | 色温与布光 | 经典电影代表 |
| :--- | :--- | :--- | :--- | :--- |
| **都市迷离 / 近身特写** | `ARRIFLEX 535B` + `Cooke S7/i 18mm T2.0` (超广角) | `Kodak Vision3 500T 5219` | 4200K 荧光绿 + 2800K 琥珀霓虹 | 《堕落天使》《重庆森林》 |
| **旗袍夜雨 / 唯美特写** | `ARRI ALEXA 35` + `Zeiss Master Prime 50mm T1.3` | `Kodak 500T / 2383 Print` | 3200K 暖钨丝灯 + 柔和黑柔滤镜 | 《花样年华》 |
| **夕阳公路 / 浪漫宿命** | `Aaton XTR Super 16` + `Leica Summilux-C 35mm T1.4` | `Kodak Ektachrome 100D` | 3000K 低角度金色逆光 | 《春光乍泄》 |
| **深夜街巷 / 红色出租车** | `ARRIFLEX 535B` + `Zeiss Super Speed 28mm T1.3` | `Kodak Vision3 500T 5219` | 6500K 青冷夜色 + 车顶灯红晕 | 《弥敦道街景》 |

---

## 🎨 2. 电影感四大光学支柱 (The 4 Optical Pillars)

1. 🏮 **黑柔滤镜发光与胶卷红晕（Black Pro-Mist Bloom & Halation）**：
   * 光源（车灯、灯笼、夕阳、反光）带有**柔和浪漫的雾状漫射光（Bloom）**，高光边缘渗透一层**柯达微红晕（Red Halation）**，消除数码干涩。
2. 🎨 **柯达 500T 色彩科学（Kodak 500T Matrix）**：
   * **暗部阴影**：深孔雀青绿（Teal-Emerald），提亮黑位（Lifted Blacks）呈现丝绒质感。
   * **高光灯光**：温润暖金琥珀色（Tungsten Amber）。
   * **红色隔离**：浓郁深沉正红（Ruby Red）。
3. 📐 **构图自适应与留白**：
   * 竖版举手保留伸展呼吸空间，横版漫步保留视线延伸空间，推墨镜保留黄金三角构图。
4. ⏳ **90s 经典黄色时间戳**：
   * 角落点缀极简微小的黄色 LCD/LED 怀旧时间码（如 `'95 11 12` / `'97  7 16`）。

---

## ✍️ 3. 王家卫独白生成法则 (Monologue Formula)

当输入一张照片时，按照以下**三大黄金公式**生成独白：
1. **精确到秒的时间戳**（“1997年7月16日下午05:42，加州阳光照在海面的第三百四十八秒。”）
2. **空间的微观距离测量**（“我和她最近的时候，距离只有0.01公分。”）
3. **日常物品的保质期与宿命隐喻**（“秋刀鱼会过期，肉酱会过期，连保鲜纸都会过期...”）

---

## 🚀 4. AI 提示词注入配方 (Prompt Recipe Formula)

```text
A 1990s Hong Kong cinema film still, directed by Wong Kar-wai, cinematography by Christopher Doyle. Shot on ARRIFLEX 535B with Cooke S7/i 18mm T2.0 lens, Kodak Vision3 500T 5219 35mm film stock. [DESCRIBE SUBJECT & ACTION]. Lighting: 4200K fluorescent ambient with 2800K warm tungsten rim light. Optical effects: Schneider Black Pro-Mist 1/4 diffusion, glowing light bloom, organic red halation around bright lights, lifted velvety teal shadows, deep ruby red tones, subtle 8fps step-printing motion trail. Retro yellow digital timestamp in corner ('95 11 12). Cinematic masterpiece, 35mm analog film aesthetic.
```

---

## 🛠️ 5. 本地 Python 命令行一键调用

```bash
# 经典王家卫港影色调（带黑柔滤镜发光与胶卷红晕）
wkw-lens my_photo.jpg -t "'95 11 12"

# 夜景/街景模式
wkw-lens taxi.jpg -s night -t "'95 11 12" --pos top-left

# 暖金黄昏模式
wkw-lens sunset.jpg -s sunset -t "'97  7 01"
```
