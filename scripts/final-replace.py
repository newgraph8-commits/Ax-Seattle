#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# List of remaining files to update
remaining_files = [
    "/vercel/share/v0-project/app/unmatched-global-presense/page.tsx",
    "/vercel/share/v0-project/app/entertainment/page.tsx",
    "/vercel/share/v0-project/app/board-assessment-tools/page.tsx",
    "/vercel/share/v0-project/app/ax-rpo/page.tsx",
    "/vercel/share/v0-project/app/strategic-execution/page.tsx",
    "/vercel/share/v0-project/app/board-restructuring-tools/page.tsx",
    "/vercel/share/v0-project/app/digitaladvantage/page.tsx",
    "/vercel/share/v0-project/app/sales/page.tsx",
    "/vercel/share/v0-project/app/board-consummating-tools/page.tsx",
    "/vercel/share/v0-project/app/director-level-technology/page.tsx",
    "/vercel/share/v0-project/app/law/page.tsx",
    "/vercel/share/v0-project/app/personnel/page.tsx",
    "/vercel/share/v0-project/app/performance-structure/page.tsx",
    "/vercel/share/v0-project/app/marketplace-position/page.tsx",
    "/vercel/share/v0-project/app/marketing/page.tsx",
    "/vercel/share/v0-project/app/get-in-touch/page.tsx",
    "/vercel/share/v0-project/app/outcome-driven-excellence/page.tsx",
    "/vercel/share/v0-project/app/leadership-succession-planning/page.tsx",
    "/vercel/share/v0-project/app/finance/page.tsx",
    "/vercel/share/v0-project/app/executive-assessment-services/page.tsx",
    "/vercel/share/v0-project/app/external-leadership-search/page.tsx",
    "/vercel/share/v0-project/app/exclusive-search-engagements/page.tsx",
    "/vercel/share/v0-project/app/education/page.tsx",
]

for file_path in remaining_files:
    if Path(file_path).exists():
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace all occurrences of "Ax South" with "Ax Seattle"
            new_content = content.replace("Ax South", "Ax Seattle")
            
            # Also replace email addresses
            new_content = new_content.replace("info@axsouth.com", "info@axseattle.com")
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Updated: {file_path}")
        except Exception as e:
            print(f"✗ Error updating {file_path}: {e}")
    else:
        print(f"✗ File not found: {file_path}")

print("\nAll files processed!")
