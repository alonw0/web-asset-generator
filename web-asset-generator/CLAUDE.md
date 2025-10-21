# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Type: Claude Skill

This is a **Claude Skill** project. Skills are model-invoked capabilities that Claude automatically triggers based on the description in SKILL.md frontmatter.

### How This Skill Works

- **Entry point**: `SKILL.md` with YAML frontmatter (name + description)
- **Trigger**: Claude reads the description at startup and invokes this skill when users request favicons, app icons, or social media images
- **Execution**: Claude reads SKILL.md instructions and runs the Python scripts in `scripts/`
- **Output**: Generated image assets + HTML meta tags

### Skill Structure

```
web-asset-generator/
├── SKILL.md              # Entry point (name, description, workflows)
├── scripts/
│   ├── generate_favicons.py    # Favicon/app icon generator
│   ├── generate_og_images.py   # Open Graph image generator
│   ├── emoji_utils.py          # Emoji suggestion and rendering
│   └── lib/
│       ├── __init__.py
│       └── validators.py       # Validation utilities (NEW)
└── references/
    └── specifications.md   # Platform specs (FB, Twitter, etc.)
```

## Core Commands

### Generate Favicons/App Icons

**From Image:**
```bash
python scripts/generate_favicons.py <source_image> <output_dir> [icon_type]
# icon_type: 'favicon', 'app', or 'all' (default)
```

**From Emoji (NEW):**
```bash
# Get emoji suggestions
python scripts/generate_favicons.py --suggest "project description" <output_dir> [icon_type]

# Generate from emoji
python scripts/generate_favicons.py --emoji "🚀" <output_dir> [icon_type] [--emoji-bg COLOR]
```

### Generate Social Media Images

**From logo:**
```bash
python scripts/generate_og_images.py <output_dir> --image <source_image>
```

**From text:**
```bash
python scripts/generate_og_images.py <output_dir> --text "Your text" [--logo path] [--bg-color '#4F46E5']
```

### Validation (NEW)

Both scripts support `--validate` flag to check file sizes, dimensions, formats, and accessibility:

```bash
# Validate OG images
python scripts/generate_og_images.py output/ --text "My Site" --validate

# Validate favicons
python scripts/generate_favicons.py logo.png output/ all --validate
```

**What gets validated:**
- **File sizes**: Checks against platform limits (FB <8MB, Twitter <5MB, favicons <100KB)
- **Dimensions**: Verifies sizes match platform specs and aspect ratios
- **Format**: Ensures PNG/JPG/JPEG compatibility
- **Contrast (OG only)**: WCAG AA/AAA compliance for text-based images

## Dependencies

- Python 3.6+
- Pillow: `pip install Pillow --break-system-packages`
- Font path: `/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf` (falls back to default)
- **Pilmoji** (for emoji rendering): `pip install pilmoji` (optional)
- **emoji** (for emoji suggestions): `pip install 'emoji<2.0.0'` (optional, **must use version <2.0.0 for pilmoji compatibility**)

## Implementation Architecture

### generate_favicons.py
- **Image mode**: Converts source to RGBA for transparency, LANCZOS resampling
- **Emoji mode** (NEW): Renders emoji using Pilmoji library, auto-scales to fit icon sizes
- Outputs: favicon.ico (multi-res) + PNGs at 16x16, 32x32, 96x96, 180x180, 192x192, 512x512
- Returns HTML `<link>` tags
- Background: Transparent for favicons, solid (white default) for app icons when using emoji

### emoji_utils.py (NEW)
- **`suggest_emojis(description, count=4)`**: Returns 4 emoji suggestions based on keyword matching
- **`generate_emoji_icon(emoji, size, bg_color)`**: Renders emoji to PIL Image using Pilmoji
- **Emoji database**: 60+ curated emojis with keywords across 10 categories (tech, business, food, health, etc.)
- **Scoring algorithm**: Keyword matching with category diversity for better suggestions

### generate_og_images.py
- **Two modes**: text-based (creates images) or image-based (resizes existing)
- **Outputs**: og-image.png (1200x630), twitter-image.png (1200x675), og-square.png (1200x1200)
- **Text rendering** (line 45): Dynamic font sizing (120-144px), wraps at 85% width, logo at 15% from top (max 20% height)
- **Dynamic font sizing** (line 19): Automatically adjusts based on text length (short=144px, medium=120px, long=102px, very long=84px)
- **Image resizing** (line 138): 'cover' mode with center-crop, LANCZOS resampling
- **Validation** (with --validate): File size, dimensions, format, and contrast ratio checks
- Returns HTML `<meta>` tags for Open Graph and Twitter

### lib/validators.py (NEW)
- **Platform requirements**: Defines specs for Facebook, Twitter, LinkedIn, WhatsApp
- **`validate_file_size()`**: Checks against platform limits (8MB for FB, 5MB for Twitter)
- **`validate_dimensions()`**: Verifies image sizes and aspect ratios
- **`validate_format()`**: Ensures compatible formats (PNG, JPG, JPEG, WebP)
- **`calculate_contrast_ratio()`**: WCAG 2.0 contrast calculation using relative luminance
- **`validate_contrast()`**: Checks WCAG AA (4.5:1) and AAA (7.0:1) compliance
- **`ValidationResult` class**: Structured results with passed/message/level (success/warning/error)

## Skill Development Notes

### Editing SKILL.md
- Keep description under 200 chars (triggers skill invocation)
- Keep body under 500 lines for optimal performance
- YAML frontmatter: `name` must match directory name in hyphen-case

### Testing the Skill
- Install locally in Claude's skills directory
- Test with various user prompts: "create a favicon", "make social sharing images", "generate Open Graph images"
- Verify skill triggers automatically based on description match

### Reference Files
- `references/specifications.md`: Detailed platform specs, aspect ratios, file size limits
- SKILL.md already references this file; Claude reads it when needed
