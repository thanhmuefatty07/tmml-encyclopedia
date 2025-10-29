#!/usr/bin/env python3
"""
TMML Encyclopedia PDF Merger
Automatically merges 29 individual session PDFs into 6 consolidated session binders

Usage:
    python scripts/merge_pdfs.py
    
Requirements:
    pip install PyPDF2
"""

import os
import sys
from pathlib import Path
try:
    from PyPDF2 import PdfWriter, PdfReader
except ImportError:
    print("Error: PyPDF2 not installed. Run: pip install PyPDF2")
    sys.exit(1)

# Session mappings from original structure
SESSION_MAPPINGS = {
    "session-1-foundation-research": [
        "executive-thesis-the-consciousness-revolution-in-ai-trading-supreme-system-v5-phase-3c-1a.pdf",
        "algorithmic-sentience-iit-consciousness.pdf",
        "iit-ai-consciousness-in-trading.pdf"
    ],
    "session-2-core-systems": [
        "ban-ke-hoach-nghien-cuu-phat-trien-nguyen-mau-tmml-lite-cho-ung-dung-giao-dich-tan-suat-cao-hft.pdf",
        "supreme-system-v5-phan-tich-toan-dien-va-ke-hoac.pdf"
    ],
    "session-3-supporting-materials": [
        "conscious-ai-trading-system-production.pdf",
        "the-gemini-protocol-a-mathematical-framework-for-cognitive-arbitrage-in-high-frequency-markets.pdf",
        "collective-and-bci-consciousness-integration.pdf",
        "supreme-system-v5-tmml-complex-adaptive-systems.pdf",
        "supreme-system-v5-tmml-encyclopedia-phase-2-initiation.pdf",
        "gemini-pro-framework-and-tmml.pdf",
        "doc-va-lam-theo-prompt.pdf"
    ],
    "session-4-advanced-research": [
        "phase-3-genuinely-conscious-ai-trading-systems.pdf",
        "supreme-system-v5-tmml-comprehensive-research-extension.pdf",
        "research-plan-publication-grade-document-transformation.pdf",
        "ai-consciousness-encyclopedia-consolidation-task.pdf",
        "phase-3-ai-consciousness-and-panpsychist-computi.pdf",
        "nghien-cuu-y-thuc-ai-toan-dien.pdf"
    ],
    "session-5-implementation-and-architecture": [
        "supreme-system-v5-tmml-qica-pham-van-thanh.pdf",
        "tmml-lite-qica-lite-upgrade-plan-for-supreme-system-v5.pdf",
        "tuyen-tap-nghien-cuu-supreme-system-v5-hop-nhat-2025-10-25.pdf",
        "supreme-system-v5-tmml-qica-revolutionary-architecture.pdf",
        "luan-an-kien-truc-nhan-thuc-giao-thoa-luong-tu-qica.pdf"
    ],
    "session-6-professional-enhancement-and-quality-assurance": [
        "chinh-sua-tai-lieu-nghien-cuu-khoa-hoc.pdf",
        "ke-hoach-nghien-cuu-v5-toi-uu.pdf",
        "co-loi-sua-loi-va-rebuild-lai-file-doc-qua-tai-lie.pdf",
        "huong-dan-gop-pdf-chuyen-nghiep.pdf",
        "chuyen-nghiep-hoa-tai-lieu-nghien-cuu-ai.pdf",
        "duoi-day-la-nhan-xet-chuyen-gia-tap-trung-thang.pdf"
    ]
}

def merge_session_pdfs(session_name, file_list, input_dir, output_dir):
    """
    Merge multiple PDFs into a single session binder
    """
    print(f"\n🔄 Processing {session_name}...")
    
    writer = PdfWriter()
    total_pages = 0
    processed_files = 0
    
    for filename in file_list:
        file_path = input_dir / filename
        
        if not file_path.exists():
            print(f"  ⚠️  Warning: {filename} not found, skipping...")
            continue
            
        try:
            reader = PdfReader(str(file_path))
            pages = len(reader.pages)
            
            # Add all pages from this PDF
            for page in reader.pages:
                writer.add_page(page)
                
            total_pages += pages
            processed_files += 1
            print(f"  ✅ Added {filename} ({pages} pages)")
            
        except Exception as e:
            print(f"  ❌ Error processing {filename}: {e}")
            continue
    
    # Write consolidated PDF
    output_file = output_dir / f"{session_name}.pdf"
    try:
        with open(output_file, 'wb') as output:
            writer.write(output)
        
        print(f"  ✅ Session binder created: {output_file}")
        print(f"  📄 Total pages: {total_pages} from {processed_files} files")
        return total_pages, processed_files
        
    except Exception as e:
        print(f"  ❌ Error writing {output_file}: {e}")
        return 0, 0

def main():
    """
    Main execution function
    """
    print("🚀 TMML Encyclopedia PDF Merger")
    print("=" * 50)
    
    # Setup paths
    base_dir = Path(".").resolve()
    input_dir = base_dir / "docs" / "pdfs" / "sessions"
    output_dir = base_dir / "docs" / "pdfs"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 Input directory: {input_dir}")
    print(f"📁 Output directory: {output_dir}")
    
    if not input_dir.exists():
        print(f"❌ Error: Input directory {input_dir} does not exist")
        print("   Please ensure all 29 PDF files are in docs/pdfs/sessions/")
        return 1
    
    # Process each session
    total_pages_all = 0
    total_files_processed = 0
    sessions_created = 0
    
    for session_name, file_list in SESSION_MAPPINGS.items():
        pages, files = merge_session_pdfs(session_name, file_list, input_dir, output_dir)
        total_pages_all += pages
        total_files_processed += files
        if pages > 0:
            sessions_created += 1
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 MERGE SUMMARY")
    print(f"├── Sessions created: {sessions_created}/6")
    print(f"├── Files processed: {total_files_processed}/29")
    print(f"├── Total pages: {total_pages_all}")
    print(f"└── Target pages: ~1000 ({total_pages_all/1000*100:.1f}% of target)")
    
    if sessions_created == 6 and total_files_processed >= 25:  # Allow some missing files
        print("\n✅ SUCCESS: All session binders created successfully!")
        print("📁 Session binders are ready in: docs/pdfs/")
        print("🔄 Next: Update LaTeX file to reference these 6 binders")
        return 0
    else:
        print("\n⚠️  WARNING: Some files may be missing or failed to process")
        print("   Please check the input directory and file names")
        return 1

if __name__ == "__main__":
    sys.exit(main())