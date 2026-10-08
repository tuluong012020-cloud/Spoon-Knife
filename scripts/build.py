"""Generate a static, dependency-free site. Never reads business-plan originals."""
import json
import re
import shutil
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'site'

def read_json(name):
    return json.loads((ROOT / 'content' / name).read_text(encoding='utf-8'))

def money(value):
    return f'{value:,}'.replace(',', '.') + 'đ'

def build():
    pages = read_json('pages.json')
    packages = read_json('packages.json')
    comparison = read_json('comparison.json')
    assert len(packages) == 4 and len({p['id'] for p in packages}) == 4
    assert [p['price'] for p in packages] == [3000000, 9000000, 18000000, 30000000]
    # Source content is public too: do not place pending/private cases here.
    cases = []
    allowed = {'slug', 'title', 'category', 'summary', 'body', 'publication_status'}
    categories = {'food', 'retail', 'services'}
    for file in sorted((ROOT / 'content' / 'cases').glob('*.json')):
        case = json.loads(file.read_text(encoding='utf-8'))
        if set(case) != allowed or case['publication_status'] != 'approved':
            raise ValueError(f'{file.name}: only approved public fields are permitted')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', case['slug']):
            raise ValueError('Invalid case slug')
        if case['category'] not in categories or case['slug'] == 'cau-truc-phan-tich':
            raise ValueError('Invalid category or reserved slug')
        if any(c['slug'] == case['slug'] for c in cases):
            raise ValueError('Duplicate case slug')
        if not all(isinstance(case[k], str) and case[k].strip() for k in allowed):
            raise ValueError('Case fields must be nonempty public text')
        cases.append(case)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / 'assets', OUT / 'assets')
    layout = (ROOT / 'templates' / 'layout.html').read_text(encoding='utf-8')
    for case in cases:
        pages.append({'path': 'du-an/' + case['slug'], 'label': case['title'],
                      'title': case['title'], 'description': case['summary'],
                      'case_body': '<section class="container section"><p class="sample-notice">Case Study — nội dung được phê duyệt công bố.</p><p>' + escape(case['body']).replace('\n', '</p><p>') + '</p></section>'})
    for page in pages:
        path = page['path']
        prefix = '../' * len(path.split('/')) if path else './'
        cards = []
        for package in packages:
            featured = package['id'] == 'tieu-chuan'
            cards.append(f'''<article class="price-card {'featured' if featured else ''}">
              {'<span class="featured-label">GÓI TIÊU CHUẨN</span>' if featured else ''}
              <p class="package-label">DỊCH VỤ LẬP KẾ HOẠCH KINH DOANH</p>
              <h3>{escape(package['name'])}</h3><p class="price">{money(package['price'])}</p>
              <ul><li>Phạm vi: Chờ phê duyệt</li><li>Tiến độ: Chờ phê duyệt</li><li>Điều kiện: Chờ phê duyệt</li></ul>
              <a class="button {'button-outline' if not featured else ''}" href="{prefix}lien-he/?goi={package['id']}" aria-label="Đăng ký tư vấn gói {escape(package['name'])}">Đăng ký tư vấn <span class="arrow-glyph" aria-hidden="true"></span></a></article>''')
        prices = '<section class="container section"><div class="section-heading centered"><p class="eyebrow">BẢNG GIÁ CHÍNH THỨC</p><h2>Bốn gói dịch vụ cho nhu cầu của bạn.</h2><p>Tên và giá đã được xác nhận. Nội dung công việc từng gói: Chờ phê duyệt.</p></div><div class="pricing-grid">' + ''.join(cards) + '</div><p class="pricing-note">Thuế, thanh toán, thời gian bàn giao và các cam kết: Chờ phê duyệt. Thiết kế nổi bật không phải tuyên bố về mức độ phổ biến của gói.</p></section>'
        headers = ''.join(f'<th scope="col" class="{"highlight-column" if p["id"] == "tieu-chuan" else ""}">{escape(p["name"])}<small>{money(p["price"])}</small></th>' for p in packages)
        rows = ''.join('<tr><th scope="row">' + escape(item) + '</th>' + ''.join('<td class="highlight-column">Chờ phê duyệt</td>' if p['id'] == 'tieu-chuan' else '<td>Chờ phê duyệt</td>' for p in packages) + '</tr>' for item in comparison)
        table = '<div class="table-scroll" tabindex="0" role="region" aria-label="Bảng so sánh bốn gói, có thể cuộn ngang"><table><caption>Hạng mục và điều kiện — chưa xác nhận phạm vi theo gói</caption><thead><tr><th scope="col">Hạng mục</th>' + headers + '</tr></thead><tbody>' + rows + '</tbody></table></div>'
        options = '<option value="">Chưa xác định — cần tư vấn</option>' + ''.join(f'<option value="{p["id"]}">{escape(p["name"])} — {money(p["price"])}</option>' for p in packages)
        sentence = '; '.join(f'Gói {p["name"]}: {money(p["price"])}' for p in packages) + '.'
        case_cards = ''.join(f'<article class="case-card service" data-category="{case["category"]}"><h2 class="small-heading">{escape(case["title"])}</h2><p>{escape(case["summary"])}</p><a class="text-link" href="{prefix}du-an/{case["slug"]}/">Đọc chi tiết →</a></article>' for case in cases)
        body = page.get('case_body') or (ROOT / 'content' / 'pages' / page['file']).read_text(encoding='utf-8')
        for marker, value in [('prices', prices), ('comparison', table), ('options', options), ('package_sentence', sentence), ('cases', case_cards), ('root', prefix)]:
            body = body.replace('{{' + marker + '}}', value)
        nav = ''
        for item in pages[:9]:
            if item['path'] in ['', 'lien-he', 'du-an/cau-truc-phan-tich']:
                continue
            active = path == item['path'] or path.startswith(item['path'] + '/')
            nav += f'<a href="{prefix}{item["path"]}/"' + (' aria-current="page"' if active else '') + '>' + escape(item['label']) + '</a>'
        heading = ''
        if path:
            crumbs = f'<a href="{prefix}">Trang chủ</a><span aria-hidden="true">/</span>'
            if path.startswith('du-an/'):
                crumbs += f'<a href="{prefix}du-an/">Dự án mẫu</a><span aria-hidden="true">/</span>'
            heading = f'<section class="page-hero"><div class="container"><div class="breadcrumbs" role="navigation" aria-label="Đường dẫn trang">{crumbs}<span aria-current="page">{escape(page["label"])}</span></div><p class="eyebrow">KHỞI HƯỚNG / BUSINESS PLANNING</p><h1>{escape(page["title"])}</h1><p>{escape(page["description"])}</p></div></section>'
        values = {'root': prefix, 'title': escape(page['title'] + (' | Khởi Hướng' if path else '')),
                  'description': escape(page['description'], quote=True), 'navigation': nav,
                  'page_heading': heading, 'body': body}
        html = layout
        for key, value in values.items():
            html = html.replace('{{' + key + '}}', value)
        if '{{' in html:
            raise ValueError(f'Unresolved template in {path}')
        folder = OUT / path
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'index.html').write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')
    (OUT / '404.html').write_text('<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Không tìm thấy trang | Khởi Hướng</title><h1>Không tìm thấy trang</h1><p>Kiểm tra đường dẫn hoặc trở về trang chủ.</p><a href="/Spoon-Knife/">Trang chủ Khởi Hướng</a></html>', encoding='utf-8')
    (OUT / '.nojekyll').write_text('')
    print(f'Generated {len(pages)} pages; approved cases: {len(cases)}. No deployment performed.')

if __name__ == '__main__':
    build()
