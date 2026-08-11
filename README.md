# 🎬 Wong Kar-wai Lens (王家卫镜头 / 港影工坊)

<p align="center">
  <b>把日常照片重塑为 1990 年代香港真实胶片快门与王家卫电影质感作品</b><br>
  <i>Transform everyday photos into authentic 1990s Hong Kong cinematic art & candid film snapshots.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Style-90s%20HK%20Film-red.svg" alt="HK Style">
  <img src="https://img.shields.io/badge/CLI-wkw--lens-orange.svg" alt="CLI">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" alt="PRs Welcome">
</p>

---

## 🌟 核心特性 (Key Features)

- 📸 **全画幅纯净无遮挡（Full-Bleed & Clean）**：去除生硬黑边与多余元素，完整保留人物神态与环境构图。
- 🌅 **通透平滑的 90s 胶片影调（Continuous Color Science）**：采用严格单调连续的胶片调色曲线，**100% 杜绝色阶断层、绿紫坏斑与假打光**，肤色温润通透。
- ⏳ **90s 经典胶卷相机时间戳（Delicate Yellow Timestamp）**：角落点缀精致微小的 LCD/LED 怀旧时间码（如 `'97  7 16` / `'95 11 12` / `'97  4 16`）。
- 🎞️ **多重经典画框支持**：支持 `full-bleed`（纯净全画幅）、`film`（35mm 柯达齿孔底片框）、`cinema`（2.39:1 宽荧幕中英双语字幕）。
- ✍️ **王家卫语录生成引擎（Monologue Engine）**：多模态大模型（VLM）提示词驱动，自动生成包含“精确时间戳 + 微观空间距离 + 保质期隐喻”的王家卫式电影旁白。
- 🤖 **全能复合生态**：既是可直接接入 **Antigravity / Claude Code / Cursor / GPTs** 的标准 `SKILL.md`，也是无需付费 API 的**纯本地 Python 命令行工具**。

---

## 🖼️ 官方实战展厅 · 5 张金标港风全集 (Showcase Gallery)

### 📸 场景一 · 《自由的夏日》 (Freedom & Twilight · 官方基准)
<p align="center">
  <img src="examples/gold_standard_01.jpg" width="460" alt="Showcase 1">
</p>

* **【美学特点】**：温润通透的夕阳天际线，红裙色泽自然饱满，左上角微小的 `'97 7 16` 黄色时间印记。
* **【王家卫独白】**：“我一直以为，有些夏天永远不会过去。那天在海边，我逆着光站了很久。后来我才发现，有些事情你想留是留不住的，就像海水退潮，天总会黑。”

---

### 📸 场景二 · 《海边的青椰》 (Dusk Stroll & Coconut)
<p align="center">
  <img src="examples/gold_standard_02.jpg" width="620" alt="Showcase 2">
</p>

* **【美学特点】**：层叠涌动的青绿海浪，暖夕阳侧光勾勒出自然生动的五官与笑颜，右下角 `'94 5 1'`。
* **【王家卫独白】**：“秋刀鱼会过期，肉酱会过期，连保鲜纸都会过期。我抱着这颗青椰子在海边走了四十分钟，我想知道，这个夏天的记忆，到底能保存多久。”

---

### 📸 场景三 · 《回眸凝视》 (The Gaze)
<p align="center">
  <img src="examples/gold_standard_03.jpg" width="460" alt="Showcase 3">
</p>

* **【美学特点】**：推墨镜经典眼神与锁骨光影，深青蓝海面衬托红裙，右上角微小的 `'95 8 29'`，质感清透高级。
* **【王家卫独白】**：“那天晚上浪很大，她推下墨镜看我的那一瞬间，我们之间的距离只有0.01公分。五十七秒之后，她什么都没有说，只是转身重新走回了夜色里。”

---

### 🚕 场景四 · 《弥敦道 · 红色的士》 (HK Red Taxis at Night)
<p align="center">
  <img src="examples/gold_standard_04_taxi.jpg" width="460" alt="Taxi Night">
</p>

* **【美学特点】**：深冷青蓝沥青柏油路面，经典香港皇冠红色出租车浓郁车漆与发光车顶灯，左上角 `'95 11 12'`。
* **【王家卫独白】**：“在香港，每天有两万四千辆红色的士在路上跑。从尖沙咀到旺角，总共要拐十四个弯。那天晚上，我和前面那辆车最近的时候，距离只有两米。后来绿灯亮了，它向左转，我向右转。”

---

### 🕶️ 场景五 · 《维多利亚港 · 无脚鸟的下午》 (Victoria Harbour Portrait)
<p align="center">
  <img src="examples/gold_standard_05_man.jpg" width="460" alt="Man at Harbour">
</p>

* **【美学特点】**：面部光影均匀通透白皙，维港海水深邃青蓝，黑色墨镜与西装层次分明，右上角微小的 `'97 4 16'`。
* **【王家卫独白】**：“一九九七年四月十六日下午四点十六分，加州阳光照在维多利亚港。我戴着墨镜在海边站了一分钟，海水很蓝，风很轻。我不知道那只没有脚的鸟飞去了哪里，但我知道，这一分钟，谁都抢不走。”

---

## 🚀 快速上手 (Quick Start)

### 1. 一键安装 (Installation)

#### 方式 A：通过 Git 直接安装（推荐）
```bash
pip install -e .
```

#### 方式 B：极简依赖安装
```bash
pip install pillow numpy
```

---

### 2. 命令行一键出片 (CLI Usage)

安装完成后，可直接在终端使用全局命令 `wkw-lens` 或 `python -m src.cli`：

#### 🌟 基础用法：全画幅纯净胶片（带经典时间戳）
```bash
wkw-lens my_photo.jpg -t "'97  7 16"
```

#### 🚕 夜景与街景模式（增强深青与浓郁红调）
```bash
wkw-lens taxi.jpg -s night -t "'95 11 12" --pos top-left
```

#### 🎞️ 渲染 35mm 柯达胶卷齿孔画框
```bash
wkw-lens portrait.jpg -f film -o my_film_still.jpg
```

#### 🎬 渲染 2.39:1 电影宽荧幕与双语字幕
```bash
wkw-lens beach.jpg -f cinema -zh "有些事情你想留是留不住的" -en "SOME THINGS YOU CANNOT KEEP"
```

#### ⚙️ CLI 参数完整列表
| 参数 | 缩写 | 可选值 | 说明 |
| :--- | :--- | :--- | :--- |
| `--style` | `-s` | `wkw`, `night`, `romance` | 影调预设：`wkw`（通用经典）, `night`（夜景/出租车）, `romance`（温润文艺） |
| `--frame` | `-f` | `none`, `film`, `cinema` | 画框排版：`none`（全画幅）, `film`（35mm胶卷框）, `cinema`（宽荧幕字幕） |
| `--timestamp` | `-t` | 文本 / `'none'` | 黄色复古时间戳（如 `"'97 7 16"`，传 `'none'` 可关闭） |
| `--pos` | | `top-left`, `top-right`, `bottom-right` | 时间戳位置（默认: `top-left`） |
| `--chinese` | `-zh` | 文本 | 中文字幕内容（仅在 `-f cinema` 下生效） |
| `--english` | `-en` | 文本 | 英文字幕内容（仅在 `-f cinema` 下生效） |

---

### 3. 在 Python 代码中使用 (Python API)

```python
from PIL import Image
from src.color_grading import grade_image
from src.candid_processor import add_delicate_timestamp

# 打开照片并进行港风调色
img = Image.open("photo.jpg")
graded = grade_image(img, style="wkw")

# 添加 90s 复古时间戳
final_img = add_delicate_timestamp(graded, timestamp_str="'97  7 16", position="top-left")
final_img.save("output_wkw.jpg", quality=98)
```

---

## 🤖 作为 AI Agent Skill 使用

本项目根目录下的 [`SKILL.md`](SKILL.md) 遵循 **Antigravity / Claude Code / Cursor / Open-Agents** 标准规范。

### 如何接入你的 Agent：
1. **Antigravity / Open-Agents**：将本仓库 clone 到 Agent 的 skills 目录下，或在对话中直接 `@wong-kar-wai-lens`。
2. **Claude Code / Cursor**：直接在配置中将 `SKILL.md` 作为 Rule 或 Skill 引用。
3. **调用示例**：
   > *“请调用 wong-kar-wai-lens skill，分析我刚上传的这张香港街景照片，生成一段王家卫式的内心独白，并按金标规范输出 90s 胶片调色成片。”*

---

## 📂 项目结构 (Repository Structure)

```text
wong-kar-wai-lens/
├── README.md                  # 中英双语项目介绍与官方展厅
├── SKILL.md                   # Agent Skill 标准规范定义
├── LICENSE                    # MIT 开源协议
├── setup.py                   # pip 一键安装配置
├── requirements.txt           # Python 依赖
├── prompts/                   # 提示词库
│   ├── wkw_monologue.md       # 多模态 VLM 台词生成规则与 Few-shot 示例
│   ├── image_to_image.md      # Midjourney / Flux / SD 港风重绘咒语
│   └── director_presets.md    # 导演风格矩阵（王家卫 / 杜琪峰 / 经典文艺）
├── src/                       # 核心渲染引擎
│   ├── __init__.py
│   ├── cli.py                 # wkw-lens 命令行工具入口
│   ├── color_grading.py       # 连续平滑无断层色彩分级引擎
│   ├── candid_processor.py    # 时间戳与自然胶片快门渲染器
│   ├── film_effects.py        # 35mm 胶片微微粒与光学漫射
│   ├── frame_renderer.py      # 2.39:1 CinemaScope 与 35mm 齿孔胶卷框生成
│   ├── subtitle_engine.py     # 经典港片黄字黑边中英双语字幕渲染
│   └── pipeline.py            # 端到端处理管线
└── examples/                  # 官方 Showcase 展厅样片
```

---

## 🤝 参与贡献 (Contributing)

欢迎提交 Issue 与 PR 扩充更多港片导演风格、LUT 查找表或优化排版字体！
1. Fork 本仓库
2. 创建分支 (`git checkout -b feature/cool-preset`)
3. 提交更改 (`git commit -m 'Add new cinema preset'`)
4. 推送分支 (`git push origin feature/cool-preset`)
5. 开启 Pull Request

---

## 📜 开源协议 (License)

本项目采用 [MIT License](LICENSE) 开源协议。
