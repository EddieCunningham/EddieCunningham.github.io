# Next steps after replacing the site with al-folio

The branch `replace-with-al-folio` has been pushed. Complete the following to go live.

## 1. Backup the current site (if not done)

- On GitHub, open https://github.com/EddieCunningham/EddieCunningham.github.io
- Create a new branch **backup-old-site** from the default branch (e.g. `main`)
- This allows a one-click rollback if needed

## 2. GitHub Pages and Actions

- **Settings → Pages:** Set source to **GitHub Actions**
- **Settings → Actions → General:** Under "Workflow permissions", choose **Read and write**
- If Actions were disabled, enable them

## 3. Open a pull request and merge

- Open a PR from **replace-with-al-folio** into the default branch:  
  https://github.com/EddieCunningham/EddieCunningham.github.io/pull/new/replace-with-al-folio
- Merge the PR. After the deploy workflow completes, the live site will switch to al-folio.

## 4. Verify

- In the repo, open the **Actions** tab and confirm the latest workflow run succeeds
- Open https://EddieCunningham.github.io and hard refresh. Check name, photo, links, and publications.

## 5. Personalize (optional)

- **Email:** Replace `your.email@example.com` in `_data/socials.yml` with your real email
- **Google Scholar:** Add your `scholar_userid` in `_data/socials.yml` if you use it
- **Profile photo:** Replace `assets/img/prof_pic.jpg` with your photo (keep the filename)
- **Publications:** Replace the placeholder in `_bibliography/papers.bib` with your BibTeX entries

## 6. Clean up

- Delete the temporary clone on your machine:  
  `rm -rf /Users/edmondcunningham/al-folio-tmp`
- Keep the **backup-old-site** branch on GitHub for a while
