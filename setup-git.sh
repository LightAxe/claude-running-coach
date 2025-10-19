#!/bin/bash

# Running Training Plans Skill - Git Setup Helper
# This script helps you initialize and push the skill to GitHub

echo "=== Running Training Plans Skill - Git Setup ==="
echo ""

# Check if git is available
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

echo "📁 Current directory: $(pwd)"
echo ""

# Check if already a git repo
if [ -d ".git" ]; then
    echo "⚠️  This directory is already a git repository."
    echo ""
    read -p "Do you want to continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 0
    fi
fi

echo "This script will help you set up git and push to GitHub."
echo ""
echo "Before running these commands, make sure you have:"
echo "  1. Created a repository on GitHub"
echo "  2. Have your GitHub username and repository name ready"
echo ""
read -p "Press Enter to see the git commands you need to run..."
echo ""

echo "=== Step-by-Step Git Commands ==="
echo ""
echo "1. Initialize git repository (if not already done):"
echo "   git init"
echo ""
echo "2. Add all files:"
echo "   git add ."
echo ""
echo "3. Create initial commit:"
echo "   git commit -m \"Initial commit: Running training plans skill v1.1\""
echo ""
echo "4. Add your GitHub repository as remote:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
echo "   (Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual values)"
echo ""
echo "5. Push to GitHub:"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "=== Alternative: Copy-paste these commands ==="
echo ""
echo "git init"
echo "git add ."
echo "git commit -m \"Initial commit: Running training plans skill v1.1\""
echo "git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
echo "git branch -M main"
echo "git push -u origin main"
echo ""
echo "=== Files that will be committed ==="
echo ""
git ls-files 2>/dev/null || find . -type f -not -path '*/\.*' | grep -v "setup-git.sh"
echo ""
echo "✅ Done! Run the commands above to push to GitHub."
