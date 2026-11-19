#!/usr/bin/env python3
"""Build the gta6-meme-x-01 meme image (meme.png) from the AI-generated scene.

Pipeline, all in this session:
  1. assets/media-generation-scene-*.png -- the launch-day scene, generated
     in-session with an image model (no text in it; the model mangles text).
  2. The make.fun ghost is DRAWN here with Pillow, to the judge's spec:
     white ghost, thick black outline, two black four-pointed sparkle eyes,
     a round little hand, holding a magenta coin with a white star.
  3. Captions are drawn here in bold type with a black stroke, so they stay
     crisp and readable when the judge shrinks the picture to 480x480.

Layout (1080x1080, classic top/bottom meme bars):
  top bar 170px | scene 740px | bottom bar 170px
"""

import math
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCENE = os.path.join(
    ROOT, "assets",
    "media-generation-scene-0-cb5720db-0523-46b4-91f6-c1d6dd5f576d.png",
)
OUT = os.path.join(ROOT, "meme.png")

W, H = 1080, 1080
TOP_H, BOT_H = 170, 170
IMG_H = H - TOP_H - BOT_H

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

MAGENTA = (236, 0, 140)      # make.fun coin magenta
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def font(size):
    return ImageFont.truetype(FONT_PATH, size)


def fit_lines(draw, lines, max_width, start_size):
    """Shrink the font until the widest line fits max_width."""
    size = start_size
    while size > 20:
        f = font(size)
        if all(draw.textlength(t, font=f) <= max_width for t in lines):
            return f
        size -= 2
    return font(20)


def draw_centered_lines(draw, lines, box_top, box_height, max_width, start_size):
    f = fit_lines(draw, lines, max_width, start_size)
    ascent, descent = f.getmetrics()
    line_h = ascent + descent
    total = line_h * len(lines)
    y = box_top + (box_height - total) // 2
    for line in lines:
        draw.text(
            (W // 2, y),
            line,
            font=f,
            fill=WHITE,
            anchor="ma",
            stroke_width=max(3, f.size // 14),
            stroke_fill=BLACK,
        )
        y += line_h


def four_point_star(cx, cy, outer, inner):
    """Vertices of a 4-pointed sparkle, points up/right/down/left."""
    pts = []
    for i in range(8):
        ang = math.radians(-90 + i * 45)
        r = outer if i % 2 == 0 else inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts


def five_point_star(cx, cy, outer, inner):
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        r = outer if i % 2 == 0 else inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts


def ghost_body_points(w, h, inset=0):
    """Outline points of the ghost silhouette, inset by `inset` px."""
    cx = w / 2.0
    r = w / 2.0 - inset
    top_y = inset + r  # centre of the dome circle
    hem_y = h - 130 - inset  # where the wavy hem starts
    pts = []
    # Dome: semicircle from left side over the top to the right side.
    for deg in range(180, 361, 3):
        a = math.radians(deg)
        pts.append((cx + r * math.cos(a), top_y + r * math.sin(a)))
    # Right side down to the hem.
    pts.append((cx + r, hem_y))
    # Wavy hem: three scallops bulging upward, leftwards.
    n_sc = 3
    steps = 24
    for s in range(n_sc):
        x0 = cx + r - s * (2 * r / n_sc)
        x1 = cx + r - (s + 1) * (2 * r / n_sc)
        for i in range(steps + 1):
            t = i / steps
            x = x0 + (x1 - x0) * t
            y = hem_y - 62 * math.sin(math.pi * t)
            pts.append((x, y))
    # Left side back up to the dome start.
    pts.append((cx - r, top_y))
    return pts


def draw_ghost(size):
    """Return an RGBA image of the make.fun ghost holding its coin."""
    ss = 4  # supersample for smooth edges
    gw, gh = size[0] * ss, size[1] * ss
    layer = Image.new("RGBA", (gw, gh), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)

    # Body: black silhouette, then a smaller white one on top -> outline.
    outline = 16 * ss
    d.polygon(ghost_body_points(gw, gh, 0), fill=BLACK + (255,))
    d.polygon(ghost_body_points(gw, gh, outline), fill=WHITE + (255,))

    # Eyes: two black four-pointed sparkles.
    for ex in (0.36, 0.64):
        d.polygon(
            four_point_star(gw * ex, gh * 0.36, 29 * ss, 9 * ss),
            fill=BLACK + (255,),
        )

    # Round little hand, drawn first so the coin sits in its grip.
    hand_c = (gw * 0.58, gh * 0.76)
    hand_r = 26 * ss
    d.ellipse(
        [hand_c[0] - hand_r, hand_c[1] - hand_r,
         hand_c[0] + hand_r, hand_c[1] + hand_r],
        fill=WHITE + (255,), outline=BLACK + (255,), width=8 * ss,
    )

    # Coin: magenta disc with black outline, white star, held low at the
    # body's right edge, overlapping the hand.
    coin_c = (gw * 0.76, gh * 0.70)
    coin_r = 40 * ss
    d.ellipse(
        [coin_c[0] - coin_r, coin_c[1] - coin_r,
         coin_c[0] + coin_r, coin_c[1] + coin_r],
        fill=MAGENTA + (255,), outline=BLACK + (255,), width=10 * ss,
    )
    d.polygon(
        five_point_star(coin_c[0], coin_c[1], 28 * ss, 12 * ss),
        fill=WHITE + (255,),
    )

    return layer.resize(size, Image.LANCZOS)


def main():
    scene = Image.open(SCENE).convert("RGB")
    # Crop the square scene to the meme's picture band aspect (1080x740),
    # keeping the TV, the gamer and the coffee table; drop the far bottom.
    sw, sh = scene.size
    target_ratio = W / IMG_H
    crop_h = int(sw / target_ratio)
    crop_top = 130
    scene = scene.crop((0, crop_top, sw, crop_top + crop_h))
    scene = scene.resize((W, IMG_H), Image.LANCZOS)

    canvas = Image.new("RGB", (W, H), BLACK)
    canvas.paste(scene, (0, TOP_H))

    # Soft shadow where the ghost floats, so it sits in the scene.
    shadow = Image.new("RGBA", (W, IMG_H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.ellipse([305, 615, 465, 645], fill=(0, 0, 0, 110))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    canvas.paste(
        Image.alpha_composite(canvas.crop((0, TOP_H, W, TOP_H + IMG_H)).convert("RGBA"), shadow),
        (0, TOP_H),
    )

    # The ghost floats beside the gamer, like his little accomplice.
    ghost = draw_ghost((190, 237))
    canvas.paste(ghost, (290, TOP_H + 375), ghost)

    draw = ImageDraw.Draw(canvas)
    draw_centered_lines(
        draw,
        ["WAITED 13 YEARS", "FOR GTA 6"],
        0, TOP_H, 1000, 72,
    )
    draw_centered_lines(
        draw,
        ["DAY ONE: 'SORRY BOSS,", "I'VE GOT LEONIDA FLU'"],
        TOP_H + IMG_H, BOT_H, 1000, 64,
    )

    canvas.save(OUT, "PNG")
    print(f"wrote {OUT} {canvas.size}")


if __name__ == "__main__":
    main()
