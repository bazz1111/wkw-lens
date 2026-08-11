# 图像生成与重绘提示词库 (Image to Image & Redraw Prompts)

本模块提供了针对主流图像生成大模型（如 Midjourney v6、Flux.1、Stable Diffusion XL）的港风电影咒语配方。

---

## 🎞️ 1. 核心通用港片咒语配方 (Universal Prompt Formula)

```text
[Main Subject & Action Description], 
a 1990s Hong Kong cinema 35mm film still, directed by Wong Kar-wai, cinematography by Christopher Doyle, 
vintage Kodak Portra color grading, rich emerald-cyan ocean waves, warm amber golden dusk light, 
35mm analog film grain, subtle motion blur, dreamy optical halation, nostalgic romantic atmosphere, 
cinematic lighting, shot on 35mm lens, authentic Hong Kong movie screenshot --ar 16:9 --style raw --v 6.1
```

---

## 🎨 2. 细分场景配方 (Scene-Specific Presets)

### A. 海滩与夕阳 (Beach & Twilight Dusk)
```text
A young East Asian woman in a crimson red sundress walking barefoot on the beach at twilight, 
holding retro sunglasses, ocean waves crashing in deep teal and cyan hues, warm tungsten amber sunlight 
grazing her shoulders and face, 1990s Hong Kong movie aesthetic, 35mm Kodak Ektachrome film grain, 
Christopher Doyle style step-printing motion blur, cinematic romance.
```

### B. 重庆大厦与夜市霓虹 (Chungking Mansion & Neon Night)
```text
Candid portrait in a narrow neon-lit alleyway in 1990s Hong Kong, raining night, wet asphalt reflections, 
glowing neon signs in red and turquoise green, steam and cigarette smoke haze, high contrast cinematic chiaroscuro, 
Fallen Angels aesthetic, wide angle 21mm lens perspective distortion, nostalgic film grain.
```

### C. 复古室内与百叶窗 (Indoor Tea Restaurant & Venetian Blinds)
```text
Sitting inside a nostalgic 1990s Hong Kong Cha Chaan Teng cafe, light casting striped shadows through 
venetian blinds across the face, vintage green mosaic tiles, glass of iced milk tea on wooden table, 
warm tungsten lamp glow, Kodak Vision3 500T movie film stock look, melancholic mood.
```

---

## 🚫 3. 负向提示词 (Negative Prompts)

用于 SD / ComfyUI / Flux 避免塑料感与现代数码感：

```text
modern digital photo, oversaturated HDR, plastic smooth skin, sharp 3D render, cartoon, anime, illustration, washed out, low quality, deformed hands, unnatural collage, floating logos.
```
