# Freshservice Documentation Portal - GitHub Copilot Instructions

**CRITICAL**: Always follow these instructions first and fallback to additional search and context gathering only if the information in these instructions is incomplete or found to be in error.

## Project Overview

This is a Docusaurus 3.7.0-based documentation portal for Freshservice technical documentation, built with TypeScript and React. The project converts CSV data into high-quality Korean technical documentation following strict content preservation standards.

**Architecture**: 
- Frontend: Docusaurus 3 with React 18, TypeScript 5.6
- Content: MDX/Markdown documentation with 4-tier structure (`docs/{product}/{category}/{folder}/{article}`)
- Styling: Custom CSS with Algolia search integration
- Build: Node.js 18+ with npm, Python 3.12+ for automation scripts

## Environment Setup & Dependencies

### Required Software Versions
- **Node.js**: Version 18 or higher (current: 20.19.5)
- **Python**: Version 3.12+ (current: 3.12.3)
- **npm**: Use npm (not yarn) for consistency with package-lock.json

### Initial Setup Commands
Run these commands in exact order for a fresh repository clone:

```bash
# 1. Install Node.js dependencies
npm install
# Takes ~55 seconds. Do not interrupt - handles 1443+ packages with some deprecation warnings (normal)

# 2. Verify TypeScript configuration
npm run typecheck
# Takes ~3 seconds. Must pass before making any TypeScript changes

# 3. Test build system
npm run build
# Takes 2.4 minutes (145 seconds). NEVER CANCEL - set timeout to 300+ seconds
# Builds for both Korean (ko) and English (en) locales
# Success indicator: "Generated static files in 'build'" message
```

**CRITICAL TIMING WARNING**: 
- `npm install`: ~55 seconds - NEVER CANCEL
- `npm run build`: ~145 seconds (2.4 minutes) - NEVER CANCEL, set timeout to 300+ seconds
- `npm run typecheck`: ~3 seconds
- `npm run clear`: ~1 second

## Development Workflow

### Starting Development Server
```bash
npm start
# Takes ~30 seconds to compile client
# Success: "Docusaurus website is running at: http://localhost:3000/"
# Auto-reloads on file changes, Ctrl+C to stop
```

### Production Build Testing
```bash
npm run serve
# Serves pre-built static files at http://localhost:3000/
# Use this to test final production build output
```

### Cache Management
```bash
npm run clear
# Removes .docusaurus/, node_modules/.cache/, and build/ folders
# Run when experiencing build issues or stale cache problems
```

## Validation & Quality Assurance

### Required Pre-Commit Validation
**ALWAYS run these commands before committing changes:**

```bash
# 1. Type checking (required for TypeScript changes)
npm run typecheck
# Must pass with no errors

# 2. Build validation (required for all changes)
npm run build
# NEVER CANCEL - wait full 2.4 minutes for completion
# Must complete successfully with no errors

# 3. Visual inspection (recommended for content changes)
npm run serve
# Check http://localhost:3000/ for visual issues
```

### MDX Compatibility Fixing
```bash
# Fix HTML compatibility issues in MDX files
python3 scripts/fix_inline_styles.py docs/freshservice/target-directory/
python3 scripts/fix_escaped_br_tags.py docs/freshservice/target-directory/
python3 scripts/fix_escaped_html_imgs.py docs/freshservice/target-directory/

# These scripts auto-fix common HTML→MDX conversion issues
# Safe to run repeatedly, only modifies files with actual issues
```

## Project Structure & Key Locations

### Critical Configuration Files
- `docusaurus.config.ts` - Site configuration, themes, plugins
- `sidebars.ts` - Navigation structure for all sections
- `package.json` - Dependencies and npm scripts
- `tsconfig.json` - TypeScript configuration

### Content Organization
```
docs/                           # Main documentation content
├── freshservice/              # Primary product documentation
│   ├── getting-started/       # Entry point - highest quality reference
│   ├── user-guide-admin/      # Administrative guides
│   ├── platform/              # Platform integration guides
│   └── [18 other categories]  # Auto-generated from CSV data
src/                           # React components and themes
├── components/                # Custom React components
└── css/                       # Global styling
scripts/                       # Python automation utilities
├── fix_inline_styles.py       # HTML→JSX style conversion
├── fix_escaped_br_tags.py     # BR tag MDX compatibility
└── [3 other HTML fixers]      # Additional MDX compatibility tools
static/                        # Static assets (images, files)
.github/instructions/          # Documentation writing guidelines
└── unified-doc-template.md    # Master content template
```

### Reference Documentation Quality Standards
**ALWAYS check these high-quality examples before creating new content:**
- `docs/freshservice/getting-started/` - Master quality reference
- `.github/instructions/unified-doc-template.md` - Writing standards
- `AGENTS.md` - Korean workflow guidelines

## Content Creation & Editing Rules

### Content Preservation Standards (CRITICAL)
**NEVER delete or modify existing working content unless explicitly required:**
- ✅ **Preserve ALL**: Images, tables, HTML markup, links, code blocks
- ✅ **Maintain**: Original formatting, emphasis, styling
- ❌ **Never**: Complete rewrites, arbitrary image removal, style changes

### File Naming & Structure
- **Slugs**: Use lowercase-hyphen format (`auto-close-resolved-tickets-48hours.md`)
- **Frontmatter**: Only include `sidebar_position: N`, remove all other fields
- **4-Tier Structure**: `docs/{product}/{category}/{folder}/{article}.md`

### MDX Syntax Requirements
- **Code blocks**: Always specify language (`jsx`, `bash`, `json`, etc.)
- **Callouts**: Use only `:::info`, `:::warning`, `:::tip`, `:::success`
- **Self-closing tags**: `<img />`, `<br />`, `<hr />` (never `<img>`)
- **Indentation**: 2 spaces for all MDX/TSX files

## Common Troubleshooting

### Build Failures
1. **MDX syntax errors**: Check for unclosed HTML tags, missing language specs
2. **TypeScript errors**: Run `npm run typecheck` for specific error locations
3. **Cache issues**: Run `npm run clear` then retry build
4. **Memory issues**: Build requires ~4GB RAM, ensure sufficient resources

### Development Server Issues
1. **Port conflicts**: Default is 3000, change with `npm start -- --port 3001`
2. **Auto-reload not working**: Check file permissions, restart server
3. **Compilation errors**: Check browser console and terminal for specific errors

### Content Issues
1. **Missing images**: Check `static/` folder, verify relative paths
2. **Broken links**: Use absolute paths from `/` or relative from current file
3. **Korean text encoding**: Ensure UTF-8 encoding for all Korean content

## Testing Scenarios & Validation

### Manual Testing Requirements
After making changes, ALWAYS test these scenarios:

#### 1. Navigation Testing
- **Home page**: Load http://localhost:3000/ successfully
- **Documentation sections**: Navigate through main categories
- **Search functionality**: Test Algolia search with Korean terms
- **Mobile responsiveness**: Check mobile layout if UI changes made

#### 2. Content Functionality
- **Internal links**: Verify cross-references between documents work
- **Code syntax highlighting**: Check code blocks render correctly
- **Images**: Verify all images load and display properly
- **Tables**: Test table formatting and responsiveness

#### 3. Build Output Validation
- **Static generation**: Ensure `npm run build` completes successfully
- **Multi-language**: Verify both `/` (Korean) and `/en/` (English) work
- **Asset optimization**: Check images and styles load in production build

### Performance Expectations
- **Development server startup**: ~30 seconds
- **Build time**: 2.4 minutes (both locales)
- **Page load**: <3 seconds for typical documentation pages
- **Search results**: <1 second for typical queries

## Git Workflow & Commit Standards

### Commit Message Format
Use imperative mood with optional prefixes:
```bash
git commit -m "docs: add new incident management guide"
git commit -m "build: update TypeScript configuration"
git commit -m "fix: resolve MDX compatibility in onboarding docs"
```

### Pre-Push Checklist
- [ ] `npm run typecheck` passes
- [ ] `npm run build` completes successfully  
- [ ] Visual testing completed with `npm run serve`
- [ ] All new/modified content follows preservation standards
- [ ] No unnecessary files in commit (check `.gitignore`)

## Team Workflow & Collaboration

### Documentation Standards
- **Language**: All communication and documentation in Korean
- **Code comments**: English for technical implementation, Korean for business logic
- **Commit messages**: English (imperative mood)
- **Issue descriptions**: Korean with English technical terms in parentheses

### Review Requirements
- **Technical changes**: Must pass TypeScript and build validation
- **Content changes**: Must maintain original formatting and preserve all media
- **New documentation**: Must follow unified template standards
- **Python scripts**: Test on sample files before applying to large directories

## Emergency Procedures

### Build System Recovery
If builds consistently fail:
```bash
# 1. Complete environment reset
rm -rf node_modules package-lock.json .docusaurus build
npm install
npm run clear
npm run build

# 2. If still failing, check Node.js version
node --version  # Must be 18+
npm --version   # Verify npm compatibility
```

### Content Recovery
For MDX compatibility issues affecting multiple files:
```bash
# 1. Backup before bulk operations
cp -r docs/freshservice docs_backup

# 2. Apply automated fixes
python3 scripts/fix_inline_styles.py docs/freshservice/
python3 scripts/fix_escaped_br_tags.py docs/freshservice/

# 3. Test build after each script
npm run build
```

### Performance Issues
If build times exceed 5 minutes or development server is slow:
1. Check available system resources (4GB+ RAM recommended)
2. Clear all caches: `npm run clear`
3. Restart development environment
4. Consider excluding large directories from watch (if modified)

---

## Quick Reference Commands

```bash
# Essential workflow
npm install              # ~55s - Initial setup
npm run build           # ~145s - NEVER CANCEL, production build  
npm run typecheck       # ~3s - TypeScript validation
npm start               # ~30s - Development server
npm run serve          # Production build testing
npm run clear          # Cache cleanup

# Python automation
python3 scripts/fix_inline_styles.py docs/target/
python3 scripts/fix_escaped_br_tags.py docs/target/

# Git workflow
git add .
git commit -m "docs: describe changes"
git push origin branch-name
```

**Remember**: This is a documentation-focused project. Content quality and preservation are more important than performance optimization. Always prioritize maintaining original formatting and ensuring builds succeed over speed improvements.