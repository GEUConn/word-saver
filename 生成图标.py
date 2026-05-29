"""运行此脚本生成 icon.ico 图标文件"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def make_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 圆角矩形背景（蓝色渐变模拟）
    pad = max(2, size // 16)
    draw.rounded_rectangle(
        [pad, pad, size - pad, size - pad],
        radius=size // 5,
        fill="#3A7BD5",
    )

    # 内部高光
    draw.rounded_rectangle(
        [pad + 2, pad + 2, size - pad - 2, size // 2],
        radius=size // 6,
        fill="#5A9BF5",
    )

    # 字母 W
    font_size = int(size * 0.55)
    try:
        font = ImageFont.truetype("arialbd.ttf", font_size)
    except Exception:
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except Exception:
            font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), "W", font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) // 2 - bbox[0]
    y = (size - th) // 2 - bbox[1] + size // 20
    # 阴影
    draw.text((x + 1, y + 1), "W", fill=(0, 0, 0, 80), font=font)
    draw.text((x, y), "W", fill="white", font=font)

    return img

sizes = [16, 32, 48, 64, 128, 256]
frames = [make_icon(s) for s in sizes]

out = Path(__file__).parent / "icon.ico"
frames[0].save(
    out,
    format="ICO",
    sizes=[(s, s) for s in sizes],
    append_images=frames[1:],
)
print(f"图标已生成: {out}")
