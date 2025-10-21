# Plugin Installation Guide

This guide explains how to install the Web Asset Generator as a Claude Code plugin.

## What is a Plugin?

Plugins are packaged extensions for Claude Code that bundle Skills, commands, and other capabilities. Installing as a plugin provides:

- ✅ **One-command installation** via `/plugins`
- ✅ **Automatic updates** when new versions are released
- ✅ **Centralized management** of all your Claude Code extensions
- ✅ **Dependency tracking** for easier setup

## Installation Methods

### Method 1: Plugin Marketplace (Recommended)

The easiest way to install is through Claude Code's plugin system:

1. **Open Claude Code** in any project

2. **Install the plugin**:
   ```
   /plugins add https://github.com/alonw0/web-asset-generator
   ```

3. **Install dependencies**:
   ```bash
   pip install Pillow

   # Optional: For emoji support
   pip install pilmoji 'emoji<2.0.0'
   ```

4. **Restart Claude Code** (if needed)

5. **Test it**:
   - Type: "Create a favicon with a rocket emoji"
   - Claude should automatically invoke the Web Asset Generator skill

### Method 2: From Marketplace File

If you have the marketplace.json URL:

1. **Add the marketplace**:
   ```
   /plugins marketplace add https://raw.githubusercontent.com/alonw0/web-asset-generator/main/marketplace.json
   ```

2. **Browse available plugins**:
   ```
   /plugins
   ```

3. **Install** "Web Asset Generator" from the list

4. **Install dependencies** (same as Method 1)

### Method 3: Manual Skill Installation

If you prefer the traditional method:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alonw0/web-asset-generator.git
   cd web-asset-generator
   ```

2. **Copy the skill folder**:
   ```bash
   # macOS/Linux
   cp -r skills/web-asset-generator ~/.claude/skills/

   # Windows
   xcopy /E /I skills\web-asset-generator %USERPROFILE%\.claude\skills\web-asset-generator
   ```

3. **Install dependencies**:
   ```bash
   pip install Pillow
   pip install pilmoji 'emoji<2.0.0'  # Optional
   ```

4. **Restart Claude Code**

## Verifying Installation

### Check Plugin Status

```
/plugins list
```

You should see "web-asset-generator" in the list.

### Check Dependencies

```bash
cd ~/.claude/skills/web-asset-generator
python scripts/check_dependencies.py
```

Expected output:
```
======================================================================
Web Asset Generator - Dependency Check
======================================================================

Python Version:
  ✓ Python 3.x.x (OK)

Required Dependencies:
  ✓ Pillow x.x.x

Optional Dependencies (for emoji support):
  ✓ Pilmoji (OK)
  ✓ emoji x.x.x (compatible with pilmoji)

======================================================================
Summary:
======================================================================
✓ All required dependencies are installed
✓ All optional dependencies are installed
```

### Test the Skill

In Claude Code, try:
```
"Create a favicon for my coffee shop website"
```

Claude should:
1. Ask if you have a logo or want emoji/text-based
2. Suggest relevant emojis if you choose emoji
3. Generate icon files
4. Show HTML tags
5. Offer to integrate into your codebase

## Troubleshooting

### Plugin Not Found

**Error**: "Plugin 'web-asset-generator' not found"

**Solutions**:
1. Verify the GitHub URL is correct
2. Check your internet connection
3. Try the manual installation method
4. Ensure you're using Claude Code 2.0.13 or later

### Dependencies Not Installing

**Error**: "Module 'PIL' not found" or similar

**Solutions**:
```bash
# Ensure pip is working
pip --version

# Install dependencies explicitly
pip install Pillow --break-system-packages  # macOS with system Python
pip install Pillow  # Standard installation

# For emoji support
pip install pilmoji 'emoji<2.0.0'
```

### Skill Not Triggering

**Issue**: Claude doesn't invoke the skill when you request web assets

**Solutions**:
1. **Restart Claude Code** after installation
2. **Be specific** in your request:
   - ✅ "Create a favicon"
   - ✅ "Generate Open Graph images"
   - ✅ "Make app icons from my logo"
   - ❌ "Help me with my website" (too vague)
3. **Check skill is installed**:
   ```bash
   ls ~/.claude/skills/web-asset-generator/SKILL.md
   ```
4. **Verify SKILL.md has proper frontmatter**:
   ```bash
   head -5 ~/.claude/skills/web-asset-generator/SKILL.md
   ```
   Should show:
   ```yaml
   ---
   name: web-asset-generator
   description: Generate web assets including favicons...
   ---
   ```

### Emoji Features Not Working

**Error**: "Emoji support requires pilmoji library"

**Solution**:
```bash
# Pilmoji requires emoji version <2.0.0
pip install 'emoji<2.0.0'
pip install pilmoji

# Verify installation
python -c "from pilmoji import Pilmoji; print('✓ Pilmoji working')"
```

**Common Issue**: `AttributeError: module 'emoji.unicode_codes' has no attribute 'get_emoji_unicode_dict'`

This means emoji library is too new. Downgrade:
```bash
pip install 'emoji<2.0.0' --force-reinstall
```

### Permission Issues (macOS)

**Error**: "Permission denied" when installing to system Python

**Solution**:
```bash
# Use --break-system-packages flag
pip install Pillow --break-system-packages

# Or use a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On macOS/Linux
pip install Pillow pilmoji 'emoji<2.0.0'
```

## Updating the Plugin

### Via Plugin System

```
/plugins update web-asset-generator
```

### Manual Update

```bash
cd ~/.claude/skills/web-asset-generator
git pull origin main

# Or re-copy from repository
cd /path/to/cloned/repo
git pull
cp -r web-asset-generator ~/.claude/skills/
```

## Uninstalling

### Via Plugin System

```
/plugins remove web-asset-generator
```

### Manual Removal

```bash
rm -rf ~/.claude/skills/web-asset-generator
```

## Getting Help

- 📖 [Main README](README.md)
- 📖 [Skill Documentation](skills/web-asset-generator/SKILL.md)
- 🐛 [Report Issues](https://github.com/alonw0/web-asset-generator/issues)
- 💬 [Discussions](https://github.com/alonw0/web-asset-generator/discussions)
- 📚 [Claude Code Plugins Docs](https://docs.claude.com/en/docs/claude-code/plugins)

## Advanced Configuration

### Custom Skill Location

If you want to install the skill in a project-specific location:

```bash
cd your-project/
mkdir -p .claude/skills
cp -r /path/to/web-asset-generator/skills/web-asset-generator .claude/skills/
```

This makes the skill available only in that specific project.

### Dependency Management

For team environments, create a `requirements.txt`:

```txt
Pillow>=10.0.0
pilmoji>=2.0.0
emoji<2.0.0
```

Install for everyone:
```bash
pip install -r requirements.txt
```

---

**Need more help?** Check the [troubleshooting section in the main README](README.md#troubleshooting) or [open an issue](https://github.com/alonw0/web-asset-generator/issues).
