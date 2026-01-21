# Web Asset Generator - Claude Code Skill

> 🎨 A Claude Code Skill for generating favicons, app icons, and social media images

Talk to Claude naturally to create production-ready web assets from logos, text, or emojis!

[![Claude Code](https://img.shields.io/badge/Claude-Code_Skill-violet)](https://claude.ai/code)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)
[![SkillCheck](https://img.shields.io/badge/SkillCheck-PASS-brightgreen?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz48L3N2Zz4=)](https://getskillcheck.com)

## What is This?

This is a **Claude Code Skill** - a modular capability that extends Claude's functionality. When installed, Claude can automatically generate web assets through natural conversation.

**Example conversation:**

> **You:** "Create a favicon for my coffee shop website"
>
> **Claude:**
> - Suggests relevant emojis (☕ Coffee, 🏪 Store)
> - Generates all icon sizes (16×16 through 512×512)
> - Validates files and checks accessibility
> - Detects your framework (Next.js, Astro, etc.)
> - Offers to add HTML tags to your code
> - Provides testing validator links

No manual work needed - just ask Claude!

## 🎬 Demo

See the skill in action:


https://github.com/user-attachments/assets/99b37698-98ec-42fe-87aa-f96b86edc00b


<video src="https://github.com/alonw0/web-asset-generator/raw/main/demo.mp4" width="100%" controls>
  Your browser doesn't support video playback. <a href="https://github.com/alonw0/web-asset-generator/raw/main/demo.mp4">Download the demo video</a>.
</video>

*Watch Claude automatically generate favicons, validate them, and integrate them into your project!*

## 🚀 Quick Start

### 1. Prerequisites

- [Claude Code](https://claude.ai/code) 2.0.13 or later
- Python 3.6+ with pip

### 2. Install the Plugin

**Recommended: Via Plugin Marketplace**

The easiest way to install:

```
/plugins marketplace add alonw0/web-asset-generator
and then
/plugin install web-asset-generator@web-asset-generator-marketplace
```

Then install dependencies:
```bash
pip install Pillow

# Optional: For emoji support
pip install pilmoji 'emoji<2.0.0'
```

**Alternative: Manual Installation**

<details>
<summary>Click to expand manual installation steps</summary>

Clone this repository:
```bash
git clone https://github.com/alonw0/web-asset-generator.git
cd web-asset-generator
```

Copy the skill folder to Claude's skills directory:
```bash
# macOS/Linux
cp -r skills/web-asset-generator ~/.claude/skills/

# Windows
xcopy /E /I skills\web-asset-generator %USERPROFILE%\.claude\skills\web-asset-generator
```

Install dependencies:
```bash
pip install Pillow
pip install pilmoji 'emoji<2.0.0'  # Optional
```

</details>

### 3. Restart Claude Code

After installation, restart Claude Code to load the plugin.

### 4. Use It!

Open Claude Code and try:
- "Create a favicon with a rocket emoji"
- "Generate Open Graph images for my blog"
- "Make app icons from my logo.png"

Claude will automatically invoke this skill and guide you through the process!

## ✨ Features

- **Favicons** - Browser icons (16×16, 32×32, 96×96, favicon.ico)
- **App Icons** - PWA/mobile icons (180×180, 192×192, 512×512)
- **PWA Manifest** - Auto-generate manifest.json with icons, colors, and settings
- **Social Images** - Open Graph for Facebook, Twitter, LinkedIn (1200×630, 1200×675)
- **Emoji Support** - 60+ curated emojis with smart suggestions
- **Validation** - File sizes, dimensions, formats, WCAG contrast compliance
- **Auto-Integration** - Framework detection and code insertion
- **Interactive** - Question-based workflow using Claude's UI

## 📸 Examples

<table>
<tr>
<td width="50%">
<img src="docs/examples/rocket-emoji.png" alt="Rocket emoji favicon" width="128">
<br>
<b>Emoji Favicon</b><br>
Generated from 🚀 with custom background
</td>
<td width="50%">
<img src="docs/examples/text-og-image.png" alt="Text-based social image" width="400">
<br>
<b>Social Media Image</b><br>
Text with dynamic font sizing
</td>
</tr>
</table>

## 📁 Repository Structure

```
web-asset-generator/                    # Repository root
├── README.md                           # This file
├── CONTRIBUTING.md                     # How to contribute
├── LICENSE                             # MIT License
├── CHANGELOG.md                        # Version history
├── .claude-plugin/                     # Plugin metadata
│   └── plugin.json                     # Plugin manifest
├── marketplace.json                    # Marketplace distribution
├── docs/                               # Documentation & examples
└── skills/                             # Skills directory
    └── web-asset-generator/           # ⭐ THE SKILL (copy this folder)
        ├── SKILL.md                    # Skill definition (Claude reads this)
        ├── CLAUDE.md                   # Development guidance
        ├── scripts/
        │   ├── generate_favicons.py    # Favicon generator
        │   ├── generate_og_images.py   # Social image generator
        │   ├── emoji_utils.py          # Emoji utilities
        │   ├── check_dependencies.py   # Dependency checker
        │   └── lib/
        │       └── validators.py       # Validation system
        └── references/
            └── specifications.md       # Platform specs
```

**To install:** Copy the `skills/web-asset-generator/` folder to `~/.claude/skills/`

## 💬 Usage Examples

Once installed, use natural language:

### Favicon Generation
```
"Create a favicon for my tech startup"
"Generate app icons from my logo.png"
"Make a favicon using a rocket emoji"
"I need PWA icons for my website"
```

### Social Media Images
```
"Create Open Graph images for my blog"
"Generate Twitter card with my tagline"
"Make social sharing images from my logo"
"Create Facebook preview with custom colors"
```

### Emoji Features
```
"Suggest emojis for my coffee shop"
"Show me good emojis for a fitness app"
"Create favicon from emoji representing growth"
```

### With Validation
```
"Generate favicons and validate them"
"Create social images and check accessibility"
"Make Open Graph images and verify file sizes"
```

## 🛠️ Advanced: Direct Script Usage

You can also use the scripts directly without Claude:

```bash
cd ~/.claude/skills/web-asset-generator

# Generate from emoji
python scripts/generate_favicons.py --emoji "🚀" output/ all

# Generate social images
python scripts/generate_og_images.py output/ --text "Welcome"

# Check dependencies
python scripts/check_dependencies.py
```

See `skills/web-asset-generator/CLAUDE.md` for complete script documentation.

## 🔧 Troubleshooting

### Skill Not Working

1. Verify installation:
   ```bash
   ls ~/.claude/skills/web-asset-generator/SKILL.md
   ```

2. Check dependencies:
   ```bash
   cd ~/.claude/skills/web-asset-generator
   python scripts/check_dependencies.py
   ```

3. Restart Claude Code

4. Your request should include keywords like "favicon", "icon", "social image", or "Open Graph"

### Emoji Not Working

Pilmoji requires `emoji<2.0.0`:
```bash
pip install 'emoji<2.0.0'
```

### Claude Doesn't Invoke the Skill

- Ensure `SKILL.md` is in the skill folder
- Restart Claude Code after installation
- Try explicit requests like "create a favicon"
- Check that the skill folder is named `web-asset-generator`

## 📚 Documentation

- **[PLUGIN_INSTALLATION.md](PLUGIN_INSTALLATION.md)** - Detailed plugin installation guide
- **[skills/web-asset-generator/SKILL.md](skills/web-asset-generator/SKILL.md)** - Complete Skill instructions
- **[skills/web-asset-generator/CLAUDE.md](skills/web-asset-generator/CLAUDE.md)** - Development guide
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines
- **[CHANGELOG.md](CHANGELOG.md)** - Version history

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup
- Code standards
- Testing guidelines
- Pull request process

**Priority areas:**
- Additional platforms (Pinterest, Instagram)
- WebP/AVIF format support
- Unit tests
- Performance optimizations

## 📝 License

MIT License - see [LICENSE](LICENSE)

## 🙏 Acknowledgments

- **Anthropic** for Claude Code and the Skills framework
- **Pillow** - Python Imaging Library
- **Pilmoji** - Emoji rendering

## 🗺️ Roadmap

- [x] ~~PWA manifest.json generation~~ ✅ Completed!
- [ ] WebP and AVIF support
- [ ] Pinterest/Instagram support
- [ ] Dark mode variants
- [ ] Batch processing
- [ ] Web preview interface

## 📞 Support

- 📖 [Claude Code Skills Docs](https://docs.claude.com/en/docs/claude-code/skills)
- 🐛 [Report Issues](https://github.com/alonw0/web-asset-generator/issues)
- 💬 [Discussions](https://github.com/alonw0/web-asset-generator/discussions)
- 🌟 [Anthropic Skills Repo](https://github.com/anthropics/skills)

---

**Built for Claude Code** • **Made with ❤️ by the community**

⭐ Star this repo • Share with Claude Code users!
