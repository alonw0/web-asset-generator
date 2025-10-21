# Example Images

This directory contains example images referenced in the main README.

## Generating Examples

To recreate these examples:

### Rocket Emoji Favicon
```bash
python scripts/generate_favicons.py --emoji "🚀" --emoji-bg "#4F46E5" docs/examples/ favicon
mv docs/examples/favicon-96x96.png docs/examples/rocket-emoji.png
```

### Text-Based Social Image
```bash
python scripts/generate_og_images.py docs/examples/ --text "Welcome to My Site" --bg-color "#4F46E5"
mv docs/examples/og-image.png docs/examples/text-og-image.png
```

## Note

Example images should be committed to the repository for documentation purposes.
They are excluded from the main .gitignore via the `!docs/**/*.png` rule.
