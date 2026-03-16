#!/bin/bash

# Find all files containing "Ax South" and replace with "Ax Seattle"
find /vercel/share/v0-project -type f \( -name "*.tsx" -o -name "*.ts" -o -name "*.jsx" -o -name "*.js" -o -name "*.json" -o -name "*.md" -o -name "*.mdx" \) -exec sed -i 's/Ax South/Ax Seattle/g' {} +

echo "Replacement complete!"
