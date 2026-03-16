import fs from 'fs';
import path from 'path';

const projectRoot = '/vercel/share/v0-project';

function replacer(dir) {
  const files = fs.readdirSync(dir, { withFileTypes: true });
  
  for (const file of files) {
    const filePath = path.join(dir, file.name);
    
    // Skip node_modules, .git, and .next
    if (['.git', 'node_modules', '.next', '.vercel'].includes(file.name)) continue;
    
    if (file.isDirectory()) {
      replacer(filePath);
    } else if (file.isFile()) {
      // Check file extensions
      const ext = path.extname(file.name);
      if (['.tsx', '.ts', '.jsx', '.js', '.json', '.md', '.mdx', '.txt'].includes(ext)) {
        try {
          let content = fs.readFileSync(filePath, 'utf-8');
          if (content.includes('Ax South')) {
            const updated = content.replace(/Ax South/g, 'Ax Seattle');
            fs.writeFileSync(filePath, updated, 'utf-8');
            console.log(`Updated: ${filePath}`);
          }
        } catch (err) {
          // Skip files that can't be read
        }
      }
    }
  }
}

replacer(projectRoot);
console.log('Replacement complete!');
