---
name: "wong-kar-wai-lens"
description: "Transform everyday photos into authentic 1990s Hong Kong cinematic snapshots (Wong Kar-wai & Christopher Doyle aesthetic) with natural film color grading, clean skin tones, delicate timestamps, and poetic monologues."
---

# 王家卫电影镜头 (Wong Kar-wai Lens Skill)

`wong-kar-wai-lens` 是一个将普通摄影照片重塑为 **1980-1990 年代经典香港电影（尤其是王家卫、杜琪峰美学）** 质感的开源 Skill 与工具箱。

它结合了**多模态画面理解、构图比例自适应、真实通透的胶片色彩分级、无瑕面部光影校准、微小复古黄色时间戳、以及标志性的中英双语王家卫独白生成**。

---

## 🎨 1. 核心视觉与光影规范 (Visual & Lighting Rules)

### 色彩分级与自然光影（Color & Lighting）
* **面部光影原则（Natural Skin & Ambient Light - 关键铁律）**：
  * 面部光线必须**均匀、通透、白皙自然**，严禁出现深橘色、暗沉、或假打光造成的“阴阳脸”光斑。
  * 保持平滑连续的色彩色阶，严禁出现通道溢出导致的绿紫断层坏块（Solarization）。
* **经典港片色调（90s HK Film Tones）**：
  * **暗部与阴影**：深孔雀绿、青蓝色（Cyan/Teal），微微提亮黑位（Lifted Blacks）呈现胶片层次。
  * **高光与夕阳**：温润自然的晚霞漫射金光，红裙饱满浓郁。
* **极微细胶片质感（Silky Micro-Grain）**：
  * 采用极微细的 35mm 银盐胶片质感（ISO 100/200），拒绝粗糙沙化与数码脏斑。

### 📐 构图与画幅自适应准则（Composition & Framing Rules）
* **纵向延伸姿态（如举手、全身/半身站立）**：必须使用 **`2:3` 或 `3:4` 竖画幅**，保留头顶与手臂伸展的充足呼吸空间。
* **横向运动与漫步（如侧身行走、海景眺望）**：使用 **`3:2` 或 `16:9` 横画幅**，在人物视线与行进方向保留视觉延伸空间（Leading Space）。
* **对称与情绪特写（如推墨镜、眼神对视）**：严格保持肢体构建的**天然三角构图（双手-锁骨-面部）**与黄金比例。
* **全画幅纯净无侵入（Clean & Zero Intrusion）**：
  * 主画面保持 100% 纯净、无杂乱遮挡。
  * 仅在画面角落点缀精致微小的 90 年代胶卷相机黄色日期码（如 `'97  7 16`、`'94  5  1`、`'95  8 29`）。

---

## ✍️ 2. 王家卫独白生成法则 (Monologue Formula)

当输入一张照片时，分析画面中的核心人物、微小动作、环境道具与时间线索，按照以下**三大黄金公式**生成独白：

1. **精确到秒的时间戳**：
   * 例：“1997年7月16日下午05:42，加州阳光照在海面的第三百四十八秒。”
2. **空间的微观距离测量**：
   * 例：“我和她最近的时候，距离只有0.01公分。五十七秒之后，她什么都没说。”
3. **日常物品的保质期与宿命隐喻**：
   * 例：“不知道从什么时候开始，每一个东西上面都会有一个日子。秋刀鱼会过期，肉酱会过期，连保鲜纸都会过期...”
4. **排版格式（中英双语港片字幕）**：
   * 中文在上（经典黄色衬线体），英文大写在下（全大写经典无衬线体）。

---

## 🚀 3. AI 重绘提示词模版 (Prompt Formula for Flux / Midjourney / SD)

```text
A candid 1990s Hong Kong vintage 35mm film photograph, directed by Wong Kar-wai, cinematography by Christopher Doyle. [DESCRIBE SUBJECT & ACTION ACCURATELY]. Natural soft evening ambient lighting with gentle skin tones, NO harsh overexposure, NO exaggerated halo, smooth continuous porcelain skin, natural vintage Kodak film color tones with muted cyan-green sea waves and warm golden hour light, subtle 35mm film grain, small delicate retro yellow digital camera timestamp in corner ('97 7 16). Full-bleed natural candid photograph, clean and beautiful.
```

---

## 🛠️ 4. 本地 Python 命令行一键调用

```bash
# 生成全画幅自然胶片快门（微小时间戳 + 细腻微质感）
python -m src.cli input.jpg --style wkw --frame none

# 生成 35mm 柯达胶卷齿孔边框版
python -m src.cli input.jpg --style wkw --frame film
```
