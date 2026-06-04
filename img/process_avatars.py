from PIL import Image
import os

src = r'C:\Users\I568276\Desktop\ClaudeOutputs\V6'
dst = r'C:\Users\I568276\Desktop\ClaudeOutputs\SAP-Demo\img'

tasks = [
    # (src_filename, dst_filename, watermark_position)
    ('销售员.png',    'sales_avatar.png',     'bottom'),
    ('物控员.png',    'planner_avatar.png',   'top'),
    ('车间计划员.png', 'engineer_avatar.png', 'bottom'),
    ('开票专员.png', 'invoice_avatar.png', 'bottom'),
    ('仓管员.png',    'warehouse_avatar.png', 'bottom'),
]

for src_name, dst_name, wm_pos in tasks:
    img = Image.open(os.path.join(src, src_name)).convert('RGB')
    w, h = img.size

    if wm_pos == 'bottom':
        # 裁掉底部10%水印
        box = (0, 0, w, int(h * 0.90))
    else:
        # 裁掉顶部10%水印
        box = (0, int(h * 0.10), w, h)

    cropped = img.crop(box)
    cw, ch = cropped.size

    # 等比缩放短边到300，再center crop 300x300
    scale = 300 / min(cw, ch)
    new_w, new_h = int(cw * scale), int(ch * scale)
    resized = cropped.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - 300) // 2
    top  = (new_h - 300) // 2
    final = resized.crop((left, top, left + 300, top + 300))

    out_path = os.path.join(dst, dst_name)
    final.save(out_path, 'PNG', optimize=True)
    print('saved: ' + dst_name)
