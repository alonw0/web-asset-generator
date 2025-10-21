# Changelog

All notable changes to the Web Asset Generator project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-21

### Added
- Initial release of Web Asset Generator as a Claude Skill
- **Favicon Generation**
  - Generate from image files
  - Generate from emojis with smart suggestions
  - Support for browser icons (16×16, 32×32, 96×96)
  - Support for PWA/mobile icons (180×180, 192×192, 512×512)
  - Multi-resolution .ico file generation
  - Custom background colors for emoji icons

- **Social Media Image Generation**
  - Text-based Open Graph images
  - Image-based Open Graph images
  - Logo integration with text
  - Custom colors and branding
  - Platform-specific sizes (Facebook, Twitter, LinkedIn)
  - Dynamic font sizing based on text length

- **Emoji Features**
  - Smart emoji suggestions based on project description
  - 60+ curated emojis across 10 categories
  - Keyword-based matching algorithm
  - Category diversity in suggestions
  - High-quality emoji rendering using Pilmoji

- **Validation System**
  - File size validation against platform limits
  - Dimension validation with aspect ratio checking
  - Format compatibility verification
  - WCAG 2.0 contrast ratio calculation
  - WCAG AA/AAA accessibility compliance checking
  - Color-coded validation output

- **Claude Skill Integration**
  - Interactive question patterns using AskUserQuestion
  - Automatic framework detection (Next.js, Astro, SvelteKit, etc.)
  - Code integration offers
  - Testing link generation
  - Emoji selection workflow

- **Developer Experience**
  - Comprehensive argparse CLI for both scripts
  - Helpful error messages
  - Usage tips and suggestions
  - Auto-generated HTML tags
  - Validation feedback

- **Documentation**
  - Complete README with examples
  - Detailed SKILL.md for Claude
  - CLAUDE.md for development guidance
  - Platform specifications reference
  - Contributing guidelines
  - MIT License

### Technical Details
- Python 3.6+ support
- Pillow for image processing
- Pilmoji for emoji rendering
- LANCZOS resampling for quality
- Optimized PNG output
- Modular validator system

---

## Planned for Future Releases

### [1.1.0] - Planned
- PWA manifest.json generation
- WebP and AVIF format support
- Additional platform support (Pinterest, Instagram)
- Batch processing capabilities
- Enhanced error handling

### [1.2.0] - Planned
- Web-based preview interface
- Dark mode variants
- AI-powered design suggestions
- Custom font support
- Template system

---

## Version History

- **1.0.0** (2025-01-21): Initial public release

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute to this project.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
