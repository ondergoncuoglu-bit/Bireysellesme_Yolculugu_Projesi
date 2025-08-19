
import os
import re
import json

def extract_dream_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'#\s*(.*?):\s*(.*)', content)
    date_match = re.search(r'\*\*Tarih:\*\*\s*(.*)', content)
    dream_text_match = re.search(r'### Rüya Metni\n\n(.*?)(?:\n---\n### İlk Analiz ve Semboller|$)', content, re.DOTALL)
    analysis_text_match = re.search(r'### İlk Analiz ve Semboller\n\n(.*?)(?:\n### Potansiyel Etiketler|$)', content, re.DOTALL)

    title = title_match.group(1).strip() if title_match else os.path.basename(file_path).replace('.md', '')
    date = date_match.group(1).strip() if date_match else ''
    dream_text = dream_text_match.group(1).strip() if dream_text_match else ''
    analysis_text = analysis_text_match.group(1).strip() if analysis_text_match else ''

    # Extract image name from dream text if available, or try to infer from title
    image_name = ''
    if 'Rüya-001' in file_path: image_name = 'rüya 001.jpg'
    elif 'Rüya-002' in file_path: image_name = 'rüya 002.jpg'
    elif 'Rüya-003' in file_path: image_name = 'rüya 003.jpg'
    elif 'Rüya-004' in file_path: image_name = 'rüya 004.jpg'
    elif 'Rüya-005' in file_path: image_name = 'rüya 005.jpg'
    elif 'Rüya-006' in file_path: image_name = 'rüya 006.jpg'
    elif 'Rüya-007' in file_path: image_name = 'rüya 007.jpg'
    elif 'Rüya-008.md' in file_path: image_name = 'rüya 8,5.jpg' # Special case for 8.md
    elif 'Rüya-009.md' in file_path: image_name = 'rüya 9,5.jpg' # Special case for 9.md
    elif 'Rüya-010' in file_path: image_name = 'rüya 010.jpg'
    elif 'Rüya-011' in file_path: image_name = 'rüya 011.jpg'
    elif 'Rüya-012' in file_path: image_name = 'rüya 012.jpg'
    elif 'Rüya-013' in file_path: image_name = 'rüya 013.jpg'
    elif 'Rüya-014' in file_path: image_name = 'rüya 014.jpg'
    elif 'Rüya-015' in file_path: image_name = 'rüya 015.jpg'
    elif 'Rüya-016' in file_path: image_name = 'rüya 016.jpg'
    elif 'Rüya-017' in file_path: image_name = 'rüya 017.jpg'
    elif 'Rüya-018' in file_path: image_name = 'rüya 018.jpg'
    elif 'Rüya-019' in file_path: image_name = 'rüya 019.jpg'
    elif 'Rüya-020' in file_path: image_name = 'rüya 020.jpg'
    elif 'Rüya-021' in file_path: image_name = 'rüya 021.jpg'
    elif 'Rüya-022' in file_path: image_name = 'rüya 022.jpg'
    elif 'Rüya-023' in file_path: image_name = 'rüya 023.jpg'
    elif 'Rüya-024' in file_path: image_name = 'rüya 024.jpg'
    elif 'Rüya-025' in file_path: image_name = 'rüya 025.jpg'
    elif 'Rüya-026' in file_path: image_name = 'rüya 026.jpg'
    elif 'Rüya-027' in file_path: image_name = 'rüya 027.jpg'
    elif 'Rüya-028' in file_path: image_name = 'rüya 028.jpg'
    elif 'Rüya-051' in file_path: image_name = 'rüya 051.jpg'
    elif 'Rüya-073' in file_path: image_name = 'rüya 073.jpg'
    elif 'Rüya-093' in file_path: image_name = 'rüya 093.jpg'
    elif 'Rüya-113' in file_path: image_name = 'rüya 113.jpg'
    elif 'Rüya-124' in file_path: image_name = 'rüya 124.jpg'
    elif 'Rüya-128' in file_path: image_name = 'rüya 128.jpg'
    elif 'Rüya-131' in file_path: image_name = 'rüya 131.jpg'
    elif 'Rüya-136' in file_path: image_name = 'rüya 136.jpg'
    elif 'Rüya-137' in file_path: image_name = 'rüya 137.jpg'
    elif 'Rüya-175' in file_path: image_name = 'rüya 175.jpg'
    elif 'Rüya-1.md' in file_path: image_name = 'rüya 1.jpg'
    elif 'Rüya-2.md' in file_path: image_name = 'rüya 2.jpg'
    elif 'Rüya-4.md' in file_path: image_name = 'rüya 4.jpg'
    elif 'Rüya-5.md' in file_path: image_name = 'rüya 5.jpg'

    return {
        'id': os.path.basename(file_path).replace('.md', '').lower(),
        'title': title,
        'date': date,
        'dream_text': dream_text,
        'analysis_text': analysis_text,
        'image': image_name
    }

def extract_article_data(file_path):
    # For simplicity, just read the content for now. PDF/DOCX parsing is more complex.
    # In a real scenario, you'd use libraries like PyPDF2 or python-docx.
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    return {
        'id': os.path.basename(file_path).replace('.pdf', '').replace('.docx', '').lower(),
        'title': os.path.basename(file_path).replace('.pdf', '').replace('.docx', ''),
        'content': content[:500] + '...' # Truncate for brevity
    }

def extract_image_data(file_path):
    return {
        'id': os.path.basename(file_path).replace('.png', '').replace('.jpg', '').lower(),
        'title': os.path.basename(file_path).replace('.png', '').replace('.jpg', ''),
        'image': os.path.basename(file_path)
    }

ruyalar_data = []
ruya_dir = '/home/ubuntu/Bireysellesme_Projesi/Bireysellesme_Projesi/01_Ruyalar/Etiketli_Analizli'
for filename in os.listdir(ruya_dir):
    if filename.endswith('.md'):
        ruyalar_data.append(extract_dream_data(os.path.join(ruya_dir, filename)))

makaleler_data = []
makale_dir = '/home/ubuntu/Bireysellesme_Projesi/Bireysellesme_Projesi/08_Akademik_Kaynaklar/Makaleler'
for filename in os.listdir(makale_dir):
    if filename.endswith(('.pdf', '.docx')):
        makaleler_data.append(extract_article_data(os.path.join(makale_dir, filename)))

imgeler_data = []
imge_dir = '/home/ubuntu/Bireysellesme_Yolculugu_Projesi/bireysellesme-yolculugu-app/src/assets'
for filename in os.listdir(imge_dir):
    if filename.endswith(('.png', '.jpg')) and ('Kitap_EM' in filename or 'rüya' in filename):
        imgeler_data.append(extract_image_data(os.path.join(imge_dir, filename)))


output_content = f"""export const ruyalar = {json.dumps(ruyalar_data, indent=2, ensure_ascii=False)};

export const makaleler = {json.dumps(makaleler_data, indent=2, ensure_ascii=False)};

export const imgeler = {json.dumps(imgeler_data, indent=2, ensure_ascii=False)};
"""

with open('/home/ubuntu/Bireysellesme_Yolculugu_Projesi/bireysellesme-yolculugu-app/src/data.js', 'w', encoding='utf-8') as f:
    f.write(output_content)

print("data.js dosyası başarıyla oluşturuldu.")


