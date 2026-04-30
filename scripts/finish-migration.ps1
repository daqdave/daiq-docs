# finish-migration.ps1
#
# One-shot recovery + finalization script for the HTML-with-embedded-images
# migration. Run this from a Windows PowerShell terminal on David's machine.
#
# Why this script exists:
#   The migration was performed in a Linux sandbox that mounts the Dropbox
#   folder. Dropbox blocked the sandbox from deleting any file, which left
#   .git/index.lock files behind and corrupted the git index. The actual
#   working tree (49 new index.html files, _config.yml, sitemap.xml, and
#   the new converter script) is fully intact and correct on disk.
#
# What this script does:
#   1. Removes the stale .git/index.lock and tmp_obj_* files that Dropbox
#      prevented from being cleaned up in the sandbox.
#   2. Resets git's index from HEAD so it can be rebuilt cleanly.
#   3. Stages the new HTML files, the modified _config.yml and sitemap.xml,
#      and the new scripts/markdown_to_html.py converter.
#   4. (Optional, prompted) Deletes the obsolete docs/<slug>/index.md files
#      and docs/<slug>/images/ folders since images are now embedded.
#   5. Commits and pushes.
#
# Usage:
#   cd C:\Users\david.green\Dropbox\Work\GitHub\daiq-docs
#   powershell -ExecutionPolicy Bypass -File .\scripts\finish-migration.ps1
#
# Safety:
#   The pre-migration state is preserved as the git tag 'pre-html-migration'
#   and at <workspace>\daiq-docs-md-backup\. Either provides a clean rollback.

$ErrorActionPreference = 'Stop'

$repo = Resolve-Path "$PSScriptRoot\.."
Set-Location $repo
Write-Host "Working in: $repo" -ForegroundColor Cyan

# Locate git.exe. Order:
#   1. PATH
#   2. Standard Git for Windows install paths
#   3. GitHub Desktop's bundled portable git (newest app-* folder wins)
function Find-Git {
    $cmd = Get-Command git -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }

    $candidates = @(
        "$env:ProgramFiles\Git\cmd\git.exe",
        "$env:ProgramFiles\Git\bin\git.exe",
        "${env:ProgramFiles(x86)}\Git\cmd\git.exe",
        "${env:ProgramFiles(x86)}\Git\bin\git.exe",
        "$env:LOCALAPPDATA\Programs\Git\cmd\git.exe"
    )
    foreach ($c in $candidates) {
        if (Test-Path $c) { return $c }
    }

    # GitHub Desktop bundles a portable git under
    #   %LOCALAPPDATA%\GitHubDesktop\app-<version>\resources\app\git\cmd\git.exe
    # The app-<version> folder name changes on every update; pick the newest.
    $ghdRoot = Join-Path $env:LOCALAPPDATA "GitHubDesktop"
    if (Test-Path $ghdRoot) {
        $latestApp = Get-ChildItem -Path $ghdRoot -Directory -Filter "app-*" -ErrorAction SilentlyContinue |
                     Sort-Object Name -Descending | Select-Object -First 1
        if ($latestApp) {
            $ghdGit = Join-Path $latestApp.FullName "resources\app\git\cmd\git.exe"
            if (Test-Path $ghdGit) { return $ghdGit }
            $ghdGit2 = Join-Path $latestApp.FullName "resources\app\git\mingw64\bin\git.exe"
            if (Test-Path $ghdGit2) { return $ghdGit2 }
        }
    }

    return $null
}

$git = Find-Git
if (-not $git) {
    Write-Host ""
    Write-Host "Git was not found on PATH or in standard install locations." -ForegroundColor Red
    Write-Host "Looked in:" -ForegroundColor Red
    Write-Host "  - PATH (Get-Command git)" -ForegroundColor Red
    Write-Host "  - Program Files\Git\..." -ForegroundColor Red
    Write-Host "  - LOCALAPPDATA\Programs\Git\..." -ForegroundColor Red
    Write-Host "  - LOCALAPPDATA\GitHubDesktop\app-*\resources\app\git\..." -ForegroundColor Red
    Write-Host ""
    Write-Host "Either install Git for Windows (https://git-scm.com/download/win)" -ForegroundColor Red
    Write-Host "or set `$env:Path to include your git folder before running this script." -ForegroundColor Red
    exit 1
}
Write-Host "Using git at: $git" -ForegroundColor Cyan

# When using GitHub Desktop's bundled git, it needs a few env vars set so
# git can find its templates, hooks, and ssh helper. Set them based on the
# git.exe path.
$gitDir = Split-Path -Parent $git
$gitRoot = Split-Path -Parent $gitDir
if (Test-Path (Join-Path $gitRoot "mingw64\bin")) {
    $env:Path = "$gitRoot\mingw64\bin;$gitRoot\usr\bin;$env:Path"
}

# 1. Clean up stale git locks and partial-write temp objects
Write-Host ""
Write-Host "[1/5] Removing stale git locks and tmp objects..." -ForegroundColor Yellow
Get-ChildItem -Path .git -Filter "index.lock*" -Force -ErrorAction SilentlyContinue | Remove-Item -Force -ErrorAction SilentlyContinue
Get-ChildItem -Path .git\objects -Filter "tmp_obj_*" -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Force -ErrorAction SilentlyContinue
Write-Host "  Locks and temp objects cleaned."

# 2. Rebuild the git index from HEAD (the index file may be corrupt)
Write-Host ""
Write-Host "[2/5] Rebuilding git index from HEAD..." -ForegroundColor Yellow
$indexFile = Join-Path $repo ".git\index"
if (Test-Path $indexFile) {
    Remove-Item $indexFile -Force
}
& $git reset --mixed HEAD | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "  git reset failed. Try 'git status' manually to diagnose." -ForegroundColor Red
    exit 1
}
Write-Host "  Index rebuilt."

# 3. Show what's about to be staged
Write-Host ""
Write-Host "[3/5] Files that will be committed:" -ForegroundColor Yellow
& $git status --short

# 4. Optional cleanup of obsolete .md files and images/ folders
Write-Host ""
Write-Host "[4/5] Optional cleanup of obsolete sources" -ForegroundColor Yellow
Write-Host "  The migration replaced 49 docs/<slug>/index.md files with index.html"
Write-Host "  and embedded all images inline. The old .md files and images/ folders"
Write-Host "  are now redundant (Jekyll already excludes them via _config.yml)."
Write-Host "  You can either delete them now or leave them on disk for later."
$choice = Read-Host "  Delete the old .md files and images/ folders now? (y/N)"
if ($choice -match '^[Yy]') {
    Write-Host "  Deleting old per-article markdown files..."
    Get-ChildItem -Path docs -Recurse -Filter "index.md" -ErrorAction SilentlyContinue |
        Where-Object { $_.DirectoryName -ne $repo.Path } |
        Remove-Item -Force -ErrorAction SilentlyContinue

    Write-Host "  Deleting old per-article images folders..."
    Get-ChildItem -Path docs -Recurse -Directory -Filter "images" -ErrorAction SilentlyContinue |
        Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

    Write-Host "  Updated status:"
    & $git status --short | Select-Object -First 12
    Write-Host "  ..."
} else {
    Write-Host "  Skipped. You can run this script again any time to delete them."
}

# 5. Stage all changes, commit, push
Write-Host ""
Write-Host "[5/5] Stage, commit, push" -ForegroundColor Yellow
$proceed = Read-Host "  Stage everything, commit with the standard message, and push to origin/main? (y/N)"
if ($proceed -match '^[Yy]') {
    & $git add -A
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  git add failed." -ForegroundColor Red
        exit 1
    }

    $commitMsg = @'
Migrate articles to self-contained HTML with embedded images

- Convert all 49 articles from index.md to index.html with base64-embedded
  images, eliminating external image references.
- Strip duplicate DAQ logo occurrences within each article (5+ repeats):
  980 logo copies removed across the corpus, content images preserved.
- Add scripts/markdown_to_html.py: idempotent MD-to-HTML converter that
  handles front matter preservation, image hashing/dedup, and Liquid
  escaping with a raw guard around the body.
- Update _config.yml to exclude docs/*/index.md and docs/*/images so
  Jekyll builds only from the new HTML and ignores the legacy sources.
- Simplify sitemap.xml: drop the per-image enumeration loop.
- Backup of original markdown is at <workspace>/daiq-docs-md-backup/
  and the pre-migration state is preserved as the pre-html-migration
  git tag.
'@

    & $git commit -m $commitMsg
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  git commit failed." -ForegroundColor Red
        exit 1
    }

    & $git push origin main
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  git push failed. Commit succeeded locally - run 'git push' manually." -ForegroundColor Red
        exit 1
    }

    Write-Host ""
    Write-Host "Done. GitHub Pages should rebuild within a minute or two." -ForegroundColor Green
    Write-Host "Verify at: https://daqdave.github.io/daiq-docs/" -ForegroundColor Green
} else {
    Write-Host "  Skipped commit/push. Index is staged; run 'git commit' and 'git push' manually." -ForegroundColor Yellow
}
