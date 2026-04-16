# Step-by-step setup guide (Windows, GitHub Desktop)

This guide takes you from a fresh Windows machine to a live public
documentation site at `https://<your-username>.github.io/daiq-docs/`,
with no prior Git or GitHub experience required.

We'll use **GitHub Desktop**, which is GitHub's official free Windows app.
It bundles Git, handles sign-in, and gives you a friendly point-and-click
interface instead of typed commands. You do not need to learn any Git
commands to use it.

Total time: roughly 20–30 minutes. You can pause between any two steps.

---

## Step 1 — Put the `daiq-docs` folder somewhere on your PC

1. On your computer, create a folder at `C:\Users\<you>\Documents\GitHub\`
   (or anywhere you'll remember). If the `GitHub` folder doesn't exist yet,
   right-click in `Documents`, choose **New → Folder**, and name it `GitHub`.
2. Move or copy the `daiq-docs` folder (the one I produced for you) into that
   `GitHub` folder. So the final path looks like:

   ```
   C:\Users\<you>\Documents\GitHub\daiq-docs\
   ```

3. Open the `daiq-docs` folder in File Explorer. You should see files like
   `README.md`, `_config.yml`, `index.md`, and subfolders `docs\` and
   `scripts\`. Good — that's your entire site.

Tip: if you don't see file extensions like `.md` and `.yml`, turn them on:
in File Explorer's top menu, click **View → Show → File name extensions**.

---

## Step 2 — Install GitHub Desktop

1. Go to <https://desktop.github.com/>.
2. Click the big **Download for Windows (64-bit)** button.
3. Open the downloaded `GitHubDesktopSetup-x64.exe`. It installs silently
   and launches itself.
4. You'll land on a welcome screen that says **Welcome to GitHub Desktop**.

---

## Step 3 — Sign in with your existing GitHub account

1. On the welcome screen, click **Sign in to GitHub.com**.
2. Your browser will open. Sign in with your existing personal GitHub
   account. Click **Authorize desktop** when prompted.
3. Your browser will redirect back to GitHub Desktop. You'll see
   **Configure Git** showing your name and email — click **Finish**.

You now have Git installed (bundled with Desktop) and you're logged in.

---

## Step 4 — Add the `daiq-docs` folder to GitHub Desktop

1. In GitHub Desktop's top-left menu, click **File → Add local repository…**
2. Click **Choose…** and navigate to
   `C:\Users\<you>\Documents\GitHub\daiq-docs`. Click **Select Folder**.
3. You'll see a message saying: *"This directory does not appear to be a Git
   repository."* That's expected. Click the blue link that says
   **"create a repository"**.
4. A dialog appears. Confirm the values:
   - **Name**: `daiq-docs`
   - **Description**: e.g. `DAQ Electronics customer support documentation`
   - **Local path**: `C:\Users\<you>\Documents\GitHub` (leave as-is)
   - **Initialise this repository with a README**: **UNCHECK** this.
     We already have a README.
   - **Git ignore**: *None* (we already have one).
   - **License**: *None* unless you want one (you can add one later).
5. Click **Create repository**.

GitHub Desktop now shows your `daiq-docs` repo. It will say
**0 changed files** — that's correct, because the initial commit already
happened when you created the repo.

---

## Step 5 — Publish the repo to GitHub.com

1. At the top of GitHub Desktop, click the blue **Publish repository** button.
2. A dialog appears:
   - **Name**: `daiq-docs` (leave as-is)
   - **Description**: leave as-is
   - **Keep this code private**: **UNCHECK** this. We want it public so
     GitHub Pages can serve it for free and image URLs work for anyone.
   - **Organization**: leave as *None* (publish under your personal account).
3. Click **Publish repository**.

GitHub Desktop uploads everything. When it's done, click the
**View on GitHub** button (or go to
`https://github.com/<your-username>/daiq-docs` in your browser) to confirm
you can see all the files listed.

---

## Step 6 — Enable GitHub Pages

This is what actually turns your files into a browsable website.

1. On the GitHub page for your repo, click the **Settings** tab
   (near the top, far right of the row that starts with **Code**, **Issues**,
   **Pull requests**, etc.).
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Under **Branch**, choose:
   - Branch: **`main`**
   - Folder: **`/ (root)`**
5. Click **Save**.

The page will now show a yellow box that says *"Your site is live at
`https://<your-username>.github.io/daiq-docs/`"* once it finishes building
(usually 30 seconds to 2 minutes).

---

## Step 7 — Verify the site works

1. Wait 1–2 minutes.
2. Open `https://<your-username>.github.io/daiq-docs/` in your browser
   (replace `<your-username>` with your real username).
3. You should see the **DAQ Electronics Support Docs** home page with
   "How To Shrink SQL Database Log Files" in the left sidebar.
4. Click into the article. You should see the formatted steps and the
   embedded screenshots.

If you see a 404 or broken images, wait another minute and refresh — GitHub
Pages can take a couple of builds to fully settle. If it still looks wrong
after 5 minutes, jump to the Troubleshooting section below.

---

## Step 8 — Fill in `_config.yml` with your real URL

Now that you know your live URL, tell Jekyll about it so internal links
resolve correctly.

1. In File Explorer, open `daiq-docs\_config.yml` with Notepad (right-click →
   **Open with → Notepad**) or any text editor.
2. Find these two lines near the top — they start with `#` (commented out):

   ```yaml
   # url: "https://<your-github-username-or-org>.github.io"
   # baseurl: "/daiq-docs"
   ```

3. Remove the `#` and the space after it, and fill in your username:

   ```yaml
   url: "https://<your-username>.github.io"
   baseurl: "/daiq-docs"
   ```

4. Save the file.
5. Open GitHub Desktop. It will now show **1 changed file** (`_config.yml`).
6. In the bottom-left, type a commit message like
   `Set site URL and baseurl` in the **Summary** box.
7. Click **Commit to main**.
8. Click **Push origin** at the top.

Wait 1–2 minutes, then refresh your site. Search, navigation, and links
should now all work correctly.

---

## Step 9 — Install Python (for converting more PDFs)

You only need to do this the first time. If you already have Python 3 installed,
skip this step.

1. Go to <https://www.python.org/downloads/windows/>.
2. Click the big yellow **Download Python 3.x.x** button for Windows.
3. Run the installer. **Important:** on the first screen, tick the checkbox
   that says **"Add python.exe to PATH"** before you click **Install Now**.
4. Click **Install Now** and wait for it to finish.

Verify it worked: press **Windows key + R**, type `cmd`, hit Enter to open
Command Prompt. Type:

```cmd
python --version
```

You should see something like `Python 3.12.5`.

Now install the PDF library the converter needs:

```cmd
pip install pymupdf
```

Wait for it to finish. You should see `Successfully installed pymupdf-...`.

---

## Step 10 — Convert a new PDF

1. Create a folder `source_pdfs` inside your `daiq-docs` folder. (The
   `.gitignore` is configured so PDFs in this folder are NOT uploaded to
   GitHub — only the generated Markdown and images are.)
2. Drop your PDF into `source_pdfs\`, for example
   `source_pdfs\HowToInstallClient.pdf`.
3. Open Command Prompt inside the `daiq-docs` folder. Easiest way: in File
   Explorer, hold **Shift** and right-click the empty space inside the
   folder, then choose **Open in Terminal** (Windows 11) or
   **Open PowerShell window here** (Windows 10).
4. Run:

   ```cmd
   python scripts\pdf_to_markdown.py source_pdfs\HowToInstallClient.pdf docs --jekyll --nav-order 20
   ```

   - `--nav-order 20` controls sidebar position (lower = higher in the
     sidebar). Pick any integer. You can edit it later.
5. Open `docs\how-to-install-client\index.md` and give it a quick read.
   Fix any odd line breaks or stray images.

### Commit and publish

6. Open GitHub Desktop. It will show all the new files under **Changes**.
7. Type a summary like `Add article: How To Install Client`.
8. Click **Commit to main**.
9. Click **Push origin**.

Your site will update in 30–120 seconds.

---

## Batch-converting all 40–50 PDFs at once

Put every PDF in `source_pdfs\`, open PowerShell inside `daiq-docs\`
(Shift + right-click → **Open in Terminal**), and run:

```powershell
Get-ChildItem source_pdfs\*.pdf | ForEach-Object {
  python scripts\pdf_to_markdown.py $_.FullName docs --jekyll
}
```

Review the output folders, then commit + push in GitHub Desktop.

---

## Editing an article by hand

The converter is heuristic — it does a great job on most pages but you may
occasionally want to tidy something. To edit:

1. Open `docs\<slug>\index.md` in any text editor (Notepad, Notepad++,
   VS Code, etc.).
2. Make your change. Save.
3. In GitHub Desktop, commit and push.

Common small edits:

- Join two lines that were broken in the middle of a sentence.
- Delete an image that turned out to be decorative clutter.
- Add a **See also** link to a related article.

---

## Troubleshooting

**The site URL shows a 404.**
The first build can take up to 5 minutes. Also check **Settings → Pages**
again: the source must be "Deploy from a branch", branch `main`, folder `/`.

**Images are broken on the live site.**
Make sure you completed Step 8 (`url` and `baseurl` in `_config.yml`).
If those are missing, Jekyll may generate wrong absolute paths.

**GitHub Desktop says "This directory does not appear to be a Git repository."**
That's normal the very first time. Click the blue "create a repository" link
as described in Step 4.

**`python` not recognized in Command Prompt.**
You missed the "Add python.exe to PATH" checkbox during install. Re-run the
Python installer, choose **Modify**, make sure the PATH option is ticked,
and finish.

**`pip install pymupdf` fails.**
Try `python -m pip install --upgrade pip` first, then retry the install.

**I pushed a mistake and want to undo it.**
In GitHub Desktop, go to the **History** tab, right-click the bad commit, and
choose **Revert changes in commit**. Then push the revert.

---

## What to do when you get stuck

Come back here. Tell me exactly what you see on screen (or paste any error
message verbatim) and I'll walk you through the next step. There is no
situation where you're really stuck — every problem at this stage has a
quick fix.
