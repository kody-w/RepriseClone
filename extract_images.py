#!/usr/bin/env python3
"""
Extract base64-encoded images from HTML snapshot files and replace with local file references.
"""

import re
import base64
import os
from pathlib import Path

def extract_images_from_html(html_file_path):
    """Extract all base64 images from HTML file and replace with local references."""

    # Read the HTML file
    print(f"Reading {html_file_path}...")
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    original_size = len(html_content)
    print(f"Original file size: {original_size:,} bytes ({original_size / 1024 / 1024:.2f} MB)")

    # Create assets directory
    base_dir = Path(html_file_path).parent
    assets_dir = base_dir / 'snapshot-assets'
    assets_dir.mkdir(exist_ok=True)

    # Extract base filename for naming images
    base_name = Path(html_file_path).stem

    # Pattern to match base64 image data URIs
    # Captures: MIME type and base64 data
    pattern = r'data:image/([^;]+);base64,([^"\s)]+)'

    # Find all matches
    matches = list(re.finditer(pattern, html_content))
    print(f"\nFound {len(matches)} base64-encoded images")

    # Count by type
    type_counts = {}
    for match in matches:
        mime_type = match.group(1)
        type_counts[mime_type] = type_counts.get(mime_type, 0) + 1

    print("\nImage types:")
    for mime_type, count in sorted(type_counts.items()):
        print(f"  {mime_type}: {count}")

    # Extract and replace images
    extracted_images = []
    replaced_count = 0
    failed_count = 0

    # Process in reverse order to maintain correct positions during replacement
    for idx, match in enumerate(reversed(matches), 1):
        image_num = len(matches) - idx + 1
        mime_type = match.group(1)
        base64_data = match.group(2)

        # Determine file extension
        ext_map = {
            'svg+xml': 'svg',
            'png': 'png',
            'jpeg': 'jpg',
            'jpg': 'jpg',
            'gif': 'gif',
            'webp': 'webp'
        }
        ext = ext_map.get(mime_type, 'bin')

        # Generate filename
        filename = f"{base_name}-image-{image_num:03d}.{ext}"
        filepath = assets_dir / filename

        try:
            # Decode base64 data
            # Remove any whitespace/newlines that might be in the base64 string
            clean_base64 = base64_data.strip().replace('\n', '').replace('\r', '')
            image_data = base64.b64decode(clean_base64)

            # Verify we got data
            if len(image_data) == 0:
                print(f"  Warning: Image {image_num} decoded to 0 bytes")
                failed_count += 1
                continue

            # Save image file
            with open(filepath, 'wb') as f:
                f.write(image_data)

            extracted_images.append({
                'num': image_num,
                'filename': filename,
                'type': mime_type,
                'size': len(image_data)
            })

            # Replace in HTML with relative path
            old_src = match.group(0)
            new_src = f"snapshot-assets/{filename}"
            html_content = html_content[:match.start()] + new_src + html_content[match.end():]

            replaced_count += 1

            if image_num % 10 == 0:
                print(f"  Processed {image_num}/{len(matches)} images...")

        except Exception as e:
            print(f"  Error processing image {image_num}: {e}")
            failed_count += 1

    # Write updated HTML
    output_path = html_file_path
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    new_size = len(html_content)

    # Calculate statistics
    total_image_size = sum(img['size'] for img in extracted_images)
    size_saved = original_size - new_size
    percent_reduction = (size_saved / original_size) * 100 if original_size > 0 else 0

    # Print summary
    print("\n" + "="*70)
    print("EXTRACTION COMPLETE")
    print("="*70)
    print(f"\nImages Successfully Extracted: {replaced_count}")
    print(f"Images Failed: {failed_count}")
    print(f"\nOriginal HTML Size: {original_size:,} bytes ({original_size / 1024 / 1024:.2f} MB)")
    print(f"New HTML Size: {new_size:,} bytes ({new_size / 1024 / 1024:.2f} MB)")
    print(f"Space Saved: {size_saved:,} bytes ({size_saved / 1024 / 1024:.2f} MB)")
    print(f"Reduction: {percent_reduction:.1f}%")
    print(f"\nTotal Image Data Extracted: {total_image_size:,} bytes ({total_image_size / 1024 / 1024:.2f} MB)")
    print(f"\nAsset Directory: {assets_dir}")
    print(f"Files Created: {replaced_count}")

    # Show sample of extracted images
    print("\n--- Sample of Extracted Images ---")
    for img in extracted_images[:10]:
        print(f"  {img['filename']} ({img['type']}, {img['size']:,} bytes)")
    if len(extracted_images) > 10:
        print(f"  ... and {len(extracted_images) - 10} more")

    print(f"\n--- Backup ---")
    print(f"Backup created at: {html_file_path}.backup")

    return {
        'extracted': replaced_count,
        'failed': failed_count,
        'original_size': original_size,
        'new_size': new_size,
        'size_saved': size_saved,
        'percent_reduction': percent_reduction,
        'images': extracted_images
    }

if __name__ == '__main__':
    html_file = '/Users/kodyw/Documents/GitHub/RepriseClone/snapshot-1760370929454.html'

    if not os.path.exists(html_file):
        print(f"Error: File not found: {html_file}")
        exit(1)

    result = extract_images_from_html(html_file)

    print("\n" + "="*70)
    print("NEXT STEPS")
    print("="*70)
    print("1. Review extracted images in snapshot-assets/ directory")
    print("2. Test the updated HTML file to ensure images load correctly")
    print("3. Delete .backup file if satisfied with results")
    print("4. Consider committing changes to repository")
