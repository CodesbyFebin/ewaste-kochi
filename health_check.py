
import os, re, glob
html_files = glob.glob("**/*.html", recursive=True)
print(f'Checking {len(html_files)} files...')
for source in html_files:
    with open(source, 'r', encoding='utf-8', errors='ignore') as f_obj:
        content = f_obj.read()
        # Find local href paths
        links = re.findall(r'href=["']([^#"\s][^"\s]*)["']', content)
        for link in links:
            if link.startswith(('http', 'tel:', 'mailto:', 'data:')): continue
            # Handle directory paths or absolute slugs
            link_clean = link.split('?')[0].split('#')[0]
            if not link_clean: continue
            
            target = os.path.join(os.path.dirname(os.path.abspath(source)), link_clean)
            if not os.path.exists(target) and not os.path.exists(target + '.html'):
                if 'assets' not in link and 'images' not in link:
                     print(f'404 Detected in {source} -> {link_clean}')
