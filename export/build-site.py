#!/usr/bin/env python3
"""
JARVIS Prompt Library - Static Site Builder
Scans all .md prompt files and generates a self-contained interactive HTML page.
All data is embedded at build time from trusted local .md files only.
"""

import re
import json
import html
from pathlib import Path
from datetime import datetime

PROMPTS_DIR = Path("/home/turbo/jarvis-prompt-library/prompts")
OUTPUT_FILE = Path("/home/turbo/jarvis-prompt-library/export/site-interactif.html")

# Excluded directories and files
EXCLUDED_DIRS = {"SHARED", "SECURITE"}
EXCLUDED_FILES = {"README.md", "INDEX.md", "CREATION-LOG.md"}

# Category display name mapping
CATEGORY_LABELS = {
    "browseros": "BrowserOS",
    "chatgpt": "ChatGPT",
    "claude-api": "Claude API",
    "claude-code": "Claude Code",
    "cluster": "Cluster IA",
    "codex-cli": "Codex CLI",
    "codex-openai": "Codex OpenAI",
    "cowork-agents": "Cowork Agents",
    "devops-gpu": "DevOps GPU",
    "freelance-business": "Freelance",
    "gemini-app": "Gemini App",
    "gemini-cli": "Gemini CLI",
    "image-generation": "Image Gen",
    "jarvis-core": "JARVIS Core",
    "linkedin-automation": "LinkedIn",
    "models-locaux": "Modeles Locaux",
    "multi-ia": "Multi-IA",
    "n8n": "n8n",
    "openclaw": "OpenClaw",
    "perplexity": "Perplexity",
    "prompts-chat": "Chat Agents",
    "trading-ia": "Trading IA",
    "voice-ia": "Voice IA",
    "MEDIA_FORGE": "Media Forge",
    "BROWSER_OS": "BrowserOS (System)",
    "CHATGPT": "ChatGPT (System)",
    "CLAUDE_CODE": "Claude Code (System)",
    "CODEX_CLI": "Codex CLI (System)",
    "GEMINI_APP": "Gemini App (System)",
    "GEMINI_CLI": "Gemini CLI (System)",
    "JARVIS_CORE": "JARVIS Core (System)",
    "PERPLEXITY": "Perplexity (System)",
    "YOLO_MODE": "YOLO Mode (System)",
}

UPPERCASE_FOLDERS = {
    "BROWSER_OS",
    "CHATGPT",
    "CLAUDE_CODE",
    "CODEX_CLI",
    "GEMINI_APP",
    "GEMINI_CLI",
    "JARVIS_CORE",
    "PERPLEXITY",
    "YOLO_MODE",
}


def get_category(filepath: Path) -> str:
    """Extract category from the first directory under prompts/."""
    rel = filepath.relative_to(PROMPTS_DIR)
    return rel.parts[0]


def extract_title_from_content(content: str, filename: str) -> str:
    """Extract title from first # heading or fallback to filename."""
    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        title = re.sub(r"[*_`]", "", title)
        return title
    return filename.replace(".md", "").replace("-", " ").title()


def split_by_headings(content: str, base_category: str, filename: str) -> list:
    """Split content with multiple ## or ### headings into individual prompts."""
    sections = re.split(r"^(###?\s+.+)$", content, flags=re.MULTILINE)

    if len(sections) <= 2:
        return [
            {"title": extract_title_from_content(content, filename), "content": content}
        ]

    prompts = []
    i = 1
    while i < len(sections):
        heading = sections[i].strip()
        body = sections[i + 1].strip() if i + 1 < len(sections) else ""

        heading_text = re.sub(r"^#{2,3}\s+", "", heading)
        if heading_text.lower() in (
            "sommaire",
            "table des matieres",
            "table of contents",
        ):
            i += 2
            continue

        title = re.sub(r"^[\d.]+\s*", "", heading_text)
        title = re.sub(r"[\U0001f300-\U0001f9ff\u2600-\u27bf\ufe0f]", "", title).strip()

        if body and len(body) > 20:
            full_content = f"{heading}\n\n{body}"
            prompts.append({"title": title, "content": full_content})

        i += 2

    if not prompts:
        return [
            {"title": extract_title_from_content(content, filename), "content": content}
        ]

    return prompts


def get_skill_tag(filepath: Path) -> str:
    """Determine if file is a skill and return appropriate tag."""
    parts = filepath.parts
    if "skills" in parts:
        if filepath.name == "SKILL.md":
            return "Skill"
        return "Skill Ref"
    return ""


def scan_prompts() -> list:
    """Scan all .md files and return prompt data."""
    all_prompts = []

    for md_file in sorted(PROMPTS_DIR.rglob("*.md")):
        if md_file.name in EXCLUDED_FILES:
            continue

        rel = md_file.relative_to(PROMPTS_DIR)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue

        category = get_category(md_file)

        try:
            content = md_file.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  [SKIP] {md_file}: {e}")
            continue

        if not content.strip():
            continue

        category_label = CATEGORY_LABELS.get(category, category)
        skill_tag = get_skill_tag(md_file)

        if category in UPPERCASE_FOLDERS:
            sub_prompts = split_by_headings(content, category, md_file.name)
            for sp in sub_prompts:
                title = sp["title"]
                if skill_tag:
                    title = f"{title} [{skill_tag}]"
                all_prompts.append(
                    {
                        "id": len(all_prompts),
                        "title": title,
                        "category": category,
                        "categoryLabel": category_label,
                        "content": sp["content"],
                        "filename": md_file.name,
                        "path": str(rel),
                    }
                )
        else:
            title = extract_title_from_content(content, md_file.name)
            if skill_tag:
                title = f"{title} [{skill_tag}]"

            all_prompts.append(
                {
                    "id": len(all_prompts),
                    "title": title,
                    "category": category,
                    "categoryLabel": category_label,
                    "content": content,
                    "filename": md_file.name,
                    "path": str(rel),
                }
            )

    return all_prompts


def generate_html(prompts: list) -> str:
    """Generate the full self-contained HTML page."""

    categories = {}
    for p in prompts:
        cat = p["category"]
        if cat not in categories:
            categories[cat] = {"label": p["categoryLabel"], "count": 0}
        categories[cat]["count"] += 1

    sorted_cats = sorted(categories.items(), key=lambda x: x[1]["label"])

    total = len(prompts)
    cat_count = len(categories)
    date_str = datetime.now().strftime("%d/%m/%Y")

    # Serialize prompts to JSON for embedding (trusted local data only)
    prompts_json = json.dumps(prompts, ensure_ascii=False, indent=None)

    filter_buttons = ""
    for cat_key, cat_info in sorted_cats:
        filter_buttons += (
            f'      <button class="filter-btn" data-cat="{html.escape(cat_key)}">'
            f"{html.escape(cat_info['label'])} "
            f'<span class="count">{cat_info["count"]}</span></button>\n'
        )

    # NOTE: This HTML is generated from trusted local markdown files only.
    # All prompt content is pre-escaped via json.dumps and rendered as plain text
    # using textContent/innerText (no raw HTML injection from file content).
    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>JARVIS Prompt Library</title>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#0a0a1a;--bg2:#11112a;--bg3:#1a1a3a;--surface:#1e1e3e;
  --surface-hover:#252550;--border:#2a2a5a;--border-hover:#3a3a7a;
  --text:#e0e0f0;--text2:#a0a0c0;--text3:#707090;
  --purple:#7c6cf0;--purple2:#9d8ff7;--purple-bg:rgba(124,108,240,0.12);
  --cyan:#22d3ee;--cyan-bg:rgba(34,211,238,0.1);
  --green:#34d399;--red:#f87171;--yellow:#fbbf24;
  --radius:12px;--radius-sm:8px;
}}
html{{scroll-behavior:smooth}}
body{{
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  background:var(--bg);color:var(--text);line-height:1.6;
  min-height:100vh;
}}
::selection{{background:var(--purple);color:#fff}}
::-webkit-scrollbar{{width:8px}}
::-webkit-scrollbar-track{{background:var(--bg2)}}
::-webkit-scrollbar-thumb{{background:var(--border);border-radius:4px}}
::-webkit-scrollbar-thumb:hover{{background:var(--purple)}}
.header{{
  background:linear-gradient(135deg,var(--bg2) 0%,#15153a 100%);
  border-bottom:1px solid var(--border);
  padding:2rem 2rem 1.5rem;position:sticky;top:0;z-index:100;
  backdrop-filter:blur(20px);
}}
.header-inner{{max-width:1400px;margin:0 auto}}
.header h1{{
  font-size:1.8rem;font-weight:700;
  background:linear-gradient(135deg,var(--purple2),var(--cyan));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;letter-spacing:-0.02em;
}}
.header h1 span{{font-weight:300;opacity:0.7;-webkit-text-fill-color:var(--text2)}}
.stats{{
  display:flex;gap:1.5rem;margin-top:0.75rem;font-size:0.85rem;color:var(--text2);
}}
.stats .stat{{display:flex;align-items:center;gap:0.4rem}}
.stats .stat-val{{color:var(--cyan);font-weight:600;font-size:1rem}}
.search-wrap{{
  margin-top:1rem;position:relative;max-width:600px;
}}
.search-wrap input{{
  width:100%;padding:0.75rem 1rem 0.75rem 2.8rem;
  background:var(--bg);border:1px solid var(--border);border-radius:var(--radius);
  color:var(--text);font-size:0.95rem;outline:none;
  transition:border-color 0.2s,box-shadow 0.2s;
}}
.search-wrap input:focus{{
  border-color:var(--purple);
  box-shadow:0 0 0 3px var(--purple-bg);
}}
.search-wrap input::placeholder{{color:var(--text3)}}
.search-icon{{
  position:absolute;left:0.9rem;top:50%;transform:translateY(-50%);
  color:var(--text3);pointer-events:none;font-size:1.1rem;
}}
.search-shortcut{{
  position:absolute;right:0.9rem;top:50%;transform:translateY(-50%);
  background:var(--bg3);border:1px solid var(--border);border-radius:4px;
  padding:0.1rem 0.5rem;font-size:0.75rem;color:var(--text3);
  font-family:monospace;
}}
.filters{{
  display:flex;flex-wrap:wrap;gap:0.5rem;margin-top:1rem;
  max-width:1400px;
}}
.filter-btn{{
  padding:0.4rem 0.8rem;border-radius:20px;border:1px solid var(--border);
  background:transparent;color:var(--text2);font-size:0.8rem;
  cursor:pointer;transition:all 0.2s;white-space:nowrap;
  display:flex;align-items:center;gap:0.4rem;
}}
.filter-btn:hover{{border-color:var(--purple);color:var(--text)}}
.filter-btn.active{{
  background:var(--purple-bg);border-color:var(--purple);color:var(--purple2);
}}
.filter-btn .count{{
  background:var(--bg);border-radius:10px;padding:0.1rem 0.4rem;
  font-size:0.7rem;min-width:1.4rem;text-align:center;
}}
.filter-btn.active .count{{background:rgba(124,108,240,0.25)}}
.main{{max-width:1400px;margin:2rem auto;padding:0 2rem}}
.results-info{{
  font-size:0.85rem;color:var(--text3);margin-bottom:1rem;
}}
.grid{{
  display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));
  gap:1rem;
}}
.card{{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius);overflow:hidden;
  transition:all 0.25s cubic-bezier(0.4,0,0.2,1);
  cursor:pointer;position:relative;
}}
.card:hover{{
  border-color:var(--border-hover);
  transform:translateY(-2px);
  box-shadow:0 8px 32px rgba(0,0,0,0.3);
}}
.card-header{{
  padding:1rem 1.2rem;display:flex;flex-direction:column;gap:0.5rem;
}}
.card-title{{
  font-size:0.95rem;font-weight:600;color:var(--text);
  line-height:1.3;
}}
.card-meta{{display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap}}
.badge{{
  padding:0.15rem 0.55rem;border-radius:12px;font-size:0.7rem;
  font-weight:600;letter-spacing:0.02em;
}}
.badge-category{{background:var(--purple-bg);color:var(--purple2);border:1px solid rgba(124,108,240,0.2)}}
.badge-skill{{background:var(--cyan-bg);color:var(--cyan);border:1px solid rgba(34,211,238,0.2)}}
.card-path{{font-size:0.7rem;color:var(--text3);font-family:monospace}}
.card-preview{{
  padding:0 1.2rem 1rem;font-size:0.82rem;color:var(--text2);
  line-height:1.5;display:-webkit-box;-webkit-line-clamp:3;
  -webkit-box-orient:vertical;overflow:hidden;
}}
.card.expanded{{
  grid-column:1/-1;cursor:default;
  border-color:var(--purple);
  box-shadow:0 0 0 1px var(--purple),0 12px 48px rgba(124,108,240,0.15);
}}
.card.expanded .card-preview{{display:none}}
.card-full{{
  display:none;padding:0 1.2rem 1.2rem;
  max-height:70vh;overflow-y:auto;
}}
.card.expanded .card-full{{display:block}}
.card-full pre{{
  background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-sm);
  padding:1rem;overflow-x:auto;font-size:0.82rem;line-height:1.5;
  color:var(--text2);white-space:pre-wrap;word-break:break-word;
}}
.card-actions{{
  display:none;padding:0.75rem 1.2rem;border-top:1px solid var(--border);
  gap:0.5rem;
}}
.card.expanded .card-actions{{display:flex}}
.btn{{
  padding:0.5rem 1rem;border-radius:var(--radius-sm);border:1px solid var(--border);
  background:var(--bg3);color:var(--text);font-size:0.82rem;cursor:pointer;
  transition:all 0.2s;display:flex;align-items:center;gap:0.4rem;
}}
.btn:hover{{border-color:var(--purple);background:var(--purple-bg)}}
.btn-primary{{
  background:var(--purple);border-color:var(--purple);color:#fff;
}}
.btn-primary:hover{{background:var(--purple2)}}
.toast{{
  position:fixed;bottom:2rem;right:2rem;
  background:var(--surface);border:1px solid var(--green);
  color:var(--green);padding:0.75rem 1.2rem;border-radius:var(--radius-sm);
  font-size:0.85rem;z-index:1000;
  transform:translateY(100px);opacity:0;transition:all 0.3s;
}}
.toast.show{{transform:translateY(0);opacity:1}}
.empty{{
  text-align:center;padding:4rem 2rem;color:var(--text3);
}}
.empty h3{{color:var(--text2);margin-bottom:0.5rem}}
@media(max-width:768px){{
  .header{{padding:1rem}}
  .main{{padding:0 1rem}}
  .grid{{grid-template-columns:1fr}}
  .stats{{flex-wrap:wrap;gap:0.75rem}}
}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:translateY(0)}}}}
.card{{animation:fadeIn 0.3s ease both}}
</style>
</head>
<body>

<div class="header">
  <div class="header-inner">
    <h1>JARVIS <span>Prompt Library</span></h1>
    <div class="stats">
      <div class="stat"><span class="stat-val">{total}</span> prompts</div>
      <div class="stat"><span class="stat-val">{cat_count}</span> categories</div>
      <div class="stat">Genere le {date_str}</div>
    </div>
    <div class="search-wrap">
      <span class="search-icon">&#128269;</span>
      <input type="text" id="search" placeholder="Rechercher un prompt..." autocomplete="off">
      <span class="search-shortcut">/</span>
    </div>
    <div class="filters" id="filters">
      <button class="filter-btn active" data-cat="all">
        Tout <span class="count">{total}</span>
      </button>
{filter_buttons}    </div>
  </div>
</div>

<div class="main">
  <div class="results-info" id="results-info"></div>
  <div class="grid" id="grid"></div>
  <div class="empty" id="empty" style="display:none">
    <h3>Aucun prompt trouve</h3>
    <p>Essayez un autre terme de recherche ou changez de filtre.</p>
  </div>
</div>

<div class="toast" id="toast">Copie dans le presse-papiers !</div>

<script>
// All data is embedded at build time from trusted local .md files.
// Content is rendered as plain text only (textContent), never as raw HTML.
const PROMPTS = {prompts_json};

const grid = document.getElementById('grid');
const searchInput = document.getElementById('search');
const filtersEl = document.getElementById('filters');
const resultsInfo = document.getElementById('results-info');
const emptyEl = document.getElementById('empty');
const toast = document.getElementById('toast');

let activeCategory = 'all';
let searchTerm = '';
let expandedId = null;

document.addEventListener('keydown', function(e) {{
  if (e.key === '/' && document.activeElement !== searchInput) {{
    e.preventDefault();
    searchInput.focus();
  }}
  if (e.key === 'Escape') {{
    if (expandedId !== null) {{
      expandedId = null;
      render();
    }} else {{
      searchInput.value = '';
      searchTerm = '';
      render();
      searchInput.blur();
    }}
  }}
}});

searchInput.addEventListener('input', function(e) {{
  searchTerm = e.target.value.toLowerCase().trim();
  expandedId = null;
  render();
}});

filtersEl.addEventListener('click', function(e) {{
  var btn = e.target.closest('.filter-btn');
  if (!btn) return;
  activeCategory = btn.dataset.cat;
  filtersEl.querySelectorAll('.filter-btn').forEach(function(b) {{ b.classList.remove('active'); }});
  btn.classList.add('active');
  expandedId = null;
  render();
}});

function fuzzyMatch(text, term) {{
  if (!term) return true;
  var words = term.split(/\\s+/);
  var lower = text.toLowerCase();
  return words.every(function(w) {{ return lower.indexOf(w) !== -1; }});
}}

function getPreview(content) {{
  var text = content
    .replace(/^#{{1,6}}\\s+.*/gm, '')
    .replace(/```[\\s\\S]*?```/g, '[code]')
    .replace(/`[^`]+`/g, '')
    .replace(/[*_~]/g, '')
    .replace(/\\[([^\\]]+)\\]\\([^)]+\\)/g, '$1')
    .replace(/\\n{{2,}}/g, ' ')
    .trim();
  if (text.length > 180) text = text.substring(0, 180) + '...';
  return text;
}}

function createCard(p, index) {{
  var isExpanded = expandedId === p.id;
  var isSkill = p.title.indexOf('[Skill') !== -1;

  var card = document.createElement('div');
  card.className = 'card' + (isExpanded ? ' expanded' : '');
  card.dataset.id = p.id;
  card.style.animationDelay = Math.min(index, 20) * 30 + 'ms';

  // Header
  var header = document.createElement('div');
  header.className = 'card-header';
  header.addEventListener('click', function() {{ toggleCard(p.id); }});

  var titleEl = document.createElement('div');
  titleEl.className = 'card-title';
  titleEl.textContent = p.title;
  header.appendChild(titleEl);

  var meta = document.createElement('div');
  meta.className = 'card-meta';

  var badge = document.createElement('span');
  badge.className = 'badge badge-category';
  badge.textContent = p.categoryLabel;
  meta.appendChild(badge);

  if (isSkill) {{
    var skillBadge = document.createElement('span');
    skillBadge.className = 'badge badge-skill';
    skillBadge.textContent = 'Skill';
    meta.appendChild(skillBadge);
  }}

  var pathEl = document.createElement('span');
  pathEl.className = 'card-path';
  pathEl.textContent = p.path;
  meta.appendChild(pathEl);

  header.appendChild(meta);
  card.appendChild(header);

  // Preview
  var preview = document.createElement('div');
  preview.className = 'card-preview';
  preview.textContent = getPreview(p.content);
  card.appendChild(preview);

  // Full content
  var full = document.createElement('div');
  full.className = 'card-full';
  var pre = document.createElement('pre');
  pre.textContent = p.content;
  full.appendChild(pre);
  card.appendChild(full);

  // Actions
  var actions = document.createElement('div');
  actions.className = 'card-actions';

  var copyBtn = document.createElement('button');
  copyBtn.className = 'btn btn-primary';
  copyBtn.textContent = 'Copier le prompt';
  copyBtn.addEventListener('click', function(ev) {{
    ev.stopPropagation();
    copyPrompt(p.id);
  }});
  actions.appendChild(copyBtn);

  var closeBtn = document.createElement('button');
  closeBtn.className = 'btn';
  closeBtn.textContent = 'Fermer';
  closeBtn.addEventListener('click', function(ev) {{
    ev.stopPropagation();
    toggleCard(p.id);
  }});
  actions.appendChild(closeBtn);

  card.appendChild(actions);
  return card;
}}

function render() {{
  var filtered = PROMPTS.filter(function(p) {{
    if (activeCategory !== 'all' && p.category !== activeCategory) return false;
    if (searchTerm) {{
      var searchText = p.title + ' ' + p.categoryLabel + ' ' + p.content + ' ' + p.path;
      if (!fuzzyMatch(searchText, searchTerm)) return false;
    }}
    return true;
  }});

  resultsInfo.textContent = filtered.length === PROMPTS.length
    ? PROMPTS.length + ' prompts au total'
    : filtered.length + ' prompt' + (filtered.length > 1 ? 's' : '') + ' trouve' + (filtered.length > 1 ? 's' : '');

  // Clear grid safely
  while (grid.firstChild) grid.removeChild(grid.firstChild);

  if (filtered.length === 0) {{
    emptyEl.style.display = 'block';
    return;
  }}
  emptyEl.style.display = 'none';

  filtered.forEach(function(p, i) {{
    grid.appendChild(createCard(p, i));
  }});
}}

function toggleCard(id) {{
  if (expandedId === id) {{
    expandedId = null;
  }} else {{
    expandedId = id;
  }}
  render();
  if (expandedId !== null) {{
    setTimeout(function() {{
      var el = grid.querySelector('.card[data-id="' + id + '"]');
      if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
    }}, 50);
  }}
}}

function copyPrompt(id) {{
  var p = PROMPTS.find(function(x) {{ return x.id === id; }});
  if (!p) return;
  if (navigator.clipboard && navigator.clipboard.writeText) {{
    navigator.clipboard.writeText(p.content).then(showToast).catch(function() {{
      fallbackCopy(p.content);
    }});
  }} else {{
    fallbackCopy(p.content);
  }}
}}

function fallbackCopy(text) {{
  var ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed';
  ta.style.opacity = '0';
  document.body.appendChild(ta);
  ta.select();
  document.execCommand('copy');
  document.body.removeChild(ta);
  showToast();
}}

function showToast() {{
  toast.classList.add('show');
  setTimeout(function() {{ toast.classList.remove('show'); }}, 2000);
}}

render();
</script>
</body>
</html>"""

    return html_content


def main():
    print("JARVIS Prompt Library - Build Site")
    print("=" * 50)

    print(f"Scanning: {PROMPTS_DIR}")
    prompts = scan_prompts()
    print(f"Found: {len(prompts)} prompts")

    categories = {}
    for p in prompts:
        cat = p["categoryLabel"]
        categories[cat] = categories.get(cat, 0) + 1

    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")

    print("\nGenerating HTML...")
    html_content = generate_html(prompts)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(html_content, encoding="utf-8")

    size_kb = OUTPUT_FILE.stat().st_size / 1024
    print(f"Output: {OUTPUT_FILE} ({size_kb:.0f} KB)")
    print("Done!")


if __name__ == "__main__":
    main()
